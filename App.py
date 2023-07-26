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
app.layout = html.Div( id='team-one-container',
    children=[
        html.Div(draw_plotly_court(fig), id='court-plot'),
        ClearLocationDataButton(),
        ShotChecklist(),
        ShooterHeader(),
        html.Div(id='shot-checklist-result'),
        html.Div(id='free-throw-result'),
        PlayerDropdown(),
        PlayTypeDropdown(),
        html.Div(id='passing-player-dropdown-container'),
        RecordShotButton(),
        html.Div(id='click-coordinates'),
        html.Div(id='output-message')
    ]
)

# Make | Miss | Free Throws | Turnover checklist callback
@app.callback(
    Output("shot-checklist-result", "children"),
    [Input("shot-checklist", "value")]
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
        return FreeThrowInput()
    elif value == ['Turnover']:
        shot['result'] = 20
        passer['result'] = 20
        return

# Free Throws made callback
@app.callback(
    Output("free-throw-result", "children"),
    Input("free-throw-input", "value"),
)
def updateFreeThrows(value):
    shot['ftm'] = value
    passer['ftm'] = value
    return

# Player Dropdown callback
@app.callback(
    Output('player-dropdown-output-container', 'children'),
    Input('player-dropdown', 'value')
)
def update_player(value):
    shot['player'] = value
    return

# Play-Type Dropdown callback
@app.callback(
    Output('play-type-dropdown-output-container', 'children'),
    Input('play-type-dropdown', 'value')
)
def update_play_type(value):
    shot['play_type'] = value
    return

# Track click events
@app.callback(
    Output('click-coordinates', 'children'),
    Input('court-graph', 'clickData')
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
    Output('court-graph', 'figure'),
    Input('court-graph', 'clickData'),
    Input("clear-shot-button", "n_clicks"),
    [Input("record-shot-button", "n_clicks")],
    State('court-graph', 'figure'),
    prevent_initial_call=True,
    allow_duplicate=True
)
def add_marker(clickData, n_clicks, rec_n_clicks, figure):
    ctx = dash.callback_context
    
    # If the clear button is clicked, remove the marker trace
    if (ctx.triggered[0]['prop_id'] == "clear-shot-button.n_clicks") or (ctx.triggered[0]['prop_id'] == "record-shot-button.n_clicks"):
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
                    color='#a136ff',
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
        Output('output-message', 'children'), 
        Input('court-graph', 'clickData'),
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
        Output('passing-player-dropdown-container', 'children'),
        Input('creation-checklist', 'value'),
        prevent_initial_call=True
)
def passingPlayerDropdown(value):
    if value:
        return PasserHeader() ,PassingPlayerDropdown(), PassingPlayTypeDropdown()

# Record Creator player dropdown
@app.callback(
        Output('passing-player-dropdown-output-container', 'children'),
        Input('passing-player-dropdown', 'value'),
        prevent_initial_call=True
)
def update_passing_player(value):
    if value:
        passer['player'] = value
    return None

# Record Creator Play Type dropdown
@app.callback(
        Output('passing-play-type-dropdown-output-container', 'children'),
        Input('passing-play-type-dropdown', 'value'),
        prevent_initial_call=True
)
def update_passing_player(value):
    if value:
        passer['play_type'] = value
    return None

# Record shot callback
@app.callback(
    Output("record-shot-output", "children"),
    [Input("record-shot-button", "n_clicks")],
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
    Output("shot-checklist", 'value'),
    Output("player-dropdown", 'value'),
    Output('play-type-dropdown', 'value'),
    [Input("record-shot-button", "n_clicks")],
)
def clear_components(value):
    if value is not None:
        return [[], '', '']
    else:
        return [], None, None
    
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
