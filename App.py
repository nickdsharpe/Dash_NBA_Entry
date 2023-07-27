import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_daq as daq
import dash_bootstrap_components as dbc
from components import PlayerDropdown, PlayTypeDropdown, ShooterHeader, MakePlayerDictionaries, RecordShotButton, ShotChecklist, FreeThrowInput, ClearLocationDataButton, PassingPlayerDropdown, PasserHeader, PassingPlayTypeDropdown
from update_player_df import UpdateShooterDF, UpdateCreatorDF
from court import draw_plotly_court, draw_scatter_trace, is_inside_three_point_line
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json

with open('initial_state.json', "r") as file:
    initial_state = json.load(file)

player_dfs = MakePlayerDictionaries()
shot, passer = {}, {}
fig = go.Figure()
# Dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Layout
app.layout = html.Div( id='main-container',
    children=[
        html.Div(id='team-one-container',
            children=[
                html.Div(draw_plotly_court(fig, 'team-one'), id='team-one-court-plot'),
                ClearLocationDataButton('team-one'),
                ShotChecklist('team-one'),
                ShooterHeader('team-one'),
                html.Div(id='team-one-shot-checklist-result'),
                html.Div(id='team-one-free-throw-result'),
                PlayerDropdown('team-one'),
                PlayTypeDropdown('team-one'),
                html.Div(id='team-one-creation-inputs-container'),
                RecordShotButton('team-one'),
                html.Div(id='team-one-click-coordinates'),
                html.Div(id='team-one-output-message')
            ]
        ),
        html.Div(id='team-two-container',
            children=[
                html.Div(draw_plotly_court(fig, 'team-two'), id='team-two-court-plot'),
                ClearLocationDataButton('team-two'),
                ShotChecklist('team-two'),
                ShooterHeader('team-two'),
                html.Div(id='team-two-shot-checklist-result'),
                html.Div(id='team-two-free-throw-result'),
                PlayerDropdown('team-two'),
                PlayTypeDropdown('team-two'),
                html.Div(id='team-two-creation-inputs-container'),
                RecordShotButton('team-two'),
                html.Div(id='team-two-click-coordinates'),
                html.Div(id='team-two-output-message')
            ]
        )
    ], style={'display': 'flex'}
)

# Make | Miss | Free Throws | And-1 | Turnover checklist callback
@app.callback(
    Output("team-one-shot-checklist-result", "children"),
    [Input("team-one-shot-checklist", "value")]
)
def update_shot_result(value):
    if value == ['Miss']:
        shot['result'] = 0
        passer['result'] = 0
        return
    elif value == ['Make']:
        shot['result'] = 1
        passer['result'] = 1
        return
    elif value == ['Free Throws']:
        shot['result'] = 11
        passer['result'] = 11
        return FreeThrowInput('free-throw-input')
    elif value == ['And-1']:
        shot['result'] = 30
        passer['result'] = 30
        return FreeThrowInput('free-throw-input')
    elif value == ['Turnover']:
        shot['result'] = 20
        passer['result'] = 20
        return

# Free Throws made callback
@app.callback(
    Output("team-one-free-throw-result", "children"),
    Input("team-one-free-throw-input", "value"),
)
def updateFreeThrows(value):
    shot['ftm'] = value
    passer['ftm'] = value
    return

# Player Dropdown callback
@app.callback(
    Output('player-dropdown-output-container', 'children'),
    Input('team-one-player-dropdown', 'value')
)
def update_player(value):
    shot['player'] = value
    return

# Play-Type Dropdown callback
@app.callback(
    Output('play-type-dropdown-output-container', 'children'),
    Input('team-one-play-type-dropdown', 'value')
)
def update_play_type(value):
    shot['play_type'] = value
    return

# Track click events
@app.callback(
    Output('team-one-click-coordinates', 'children'),
    Input('team-one-court-graph', 'clickData')
)
def record_coordinates(clickData):
    if clickData is not None:
        x = clickData['points'][0]['x']
        y = clickData['points'][0]['y']
        shot['x'] = x
        passer['x'] = x
        shot['y'] = y
        passer['y'] = y
        return None
    else:
        return None
    
# Callback to handle click events and update the scatter trace with markers
@app.callback(
    Output('team-one-court-graph', 'figure'),
    Input('team-one-court-graph', 'clickData'),
    Input("team-one-clear-shot-button", "n_clicks"),
    [Input("team-one-record-shot-button", "n_clicks")],
    State('team-one-court-graph', 'figure'),
    prevent_initial_call=True,
    allow_duplicate=True
)
def add_marker(clickData, n_clicks, rec_n_clicks, figure):
    ctx = dash.callback_context
    
    # If the clear button is clicked, remove the marker trace
    if (ctx.triggered[0]['prop_id'] == "team-one-clear-shot-button.n_clicks") or (ctx.triggered[0]['prop_id'] == "team-one-record-shot-button.n_clicks"):
        figure['data'] = initial_state
    else:
        if clickData:
            x = clickData['points'][0]['x']
            y = clickData['points'][0]['y']

            # Remove all marker traces from the figure
            figure['data'] = [trace for trace in figure['data'] if trace['mode'] != 'markers']

            # Create a new marker trace
            new_marker_trace = go.Scatter(
                x=[x],
                y=[y],
                mode="markers",
                marker=dict(
                    color='#4fafa9',
                    size=18,
                    opacity=0.9,
                    symbol='x',
                ),
                hoverinfo='none'
            )

            # Add the new marker trace to the figure
            figure['data'].append(new_marker_trace)

            # Update the layout to enable click events again
            figure['layout']['clickmode'] = 'event+select'

    return figure

# Callback to handle shot type
@app.callback(
        Output('team-one-output-message', 'children'), 
        Input('team-one-court-graph', 'clickData'),
        prevent_initial_call=True
    )
def handle_click(click_data):
    if is_inside_three_point_line(click_data):
        shot['shot_type'] = '2pt FG'
        passer['shot_type'] = '2pt FG'
        return
    else:
        shot['shot_type'] = '3pt FG'
        passer['shot_type'] = '3pt FG'
        return

# Callback to display Creation dropdowns
@app.callback(
        Output('team-one-creation-inputs-container', 'children'),
        Input('team-one-creation-checklist', 'value')
)
def passingPlayerInputs(value):
    if value:
        return PasserHeader('team-one') ,PassingPlayerDropdown('team-one'), PassingPlayTypeDropdown('team-one')

# Record Creator player dropdown
@app.callback(
        Output('team-one-passing-player-dropdown-output-container', 'children'),
        Input('team-one-passing-player-dropdown', 'value'),
        prevent_initial_call=True
)
def update_passing_player(value):
    if value:
        passer['player'] = value
    return None

# Record Creator Play Type dropdown
@app.callback(
        Output('team-one-passing-play-type-dropdown-output-container', 'children'),
        Input('team-one-passing-play-type-dropdown', 'value'),
        prevent_initial_call=True
)
def update_passing_player(value):
    if value:
        passer['play_type'] = value
    return None

# Record shot callback
@app.callback(
    Output("team-one-record-shot-output", "children"),
    [Input("team-one-record-shot-button", "n_clicks")],
    prevent_initial_call=True,
)
def record_shot(value):
    try:
        if 'player' and 'play_type' and 'x' and 'y' and 'shot_type' and 'result' in shot:
            print(shot)
            updated_shooter_df = UpdateShooterDF(shot)
            updated_passer_df = UpdateCreatorDF(passer)
            print('Shooter:', updated_shooter_df)
            print('Creator', updated_passer_df)
            return
    except:
        return 'Data Incomplete.'
    
# Clear values in dropdowns and checklist when record shot button is pressed
@app.callback(    
    Output("team-one-shot-checklist", 'value'),
    Output("team-one-player-dropdown", 'value'),
    Output('team-one-play-type-dropdown', 'value'),
    Output('team-one-creation-checklist', 'value'),
    [Input("team-one-record-shot-button", "n_clicks")],
    allow_duplicate=True
)
def clear_components(value):
    if value is not None:
        return [[], '', '', []]
    else:
        return [], None, None, []
    
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
