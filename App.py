import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_daq as daq
import dash_bootstrap_components as dbc
from entry_form import PlayerDropdown, PlayTypeDropdown, ShooterHeader, ShotTypeDropdown, MakePlayerDictionaries, RecordShotButton, ShotChecklist, FreeThrowInput, ClearLocationDataButton
from update_player_df import UpdatePlayerDF
from court import draw_plotly_court, draw_scatter_trace
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json

with open('initial_state.json', "r") as file:
    initial_state = json.load(file)

player_dfs = MakePlayerDictionaries()
shot = {}
fig = go.Figure()
# Dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Layout
app.layout = html.Div(
    children=[
        html.H2("PPP Entry Form", style={'textAlign': 'center', 'marginTop': 10}),
        html.Div(draw_plotly_court(fig), id='court-plot'),
        ClearLocationDataButton(),
        ShotChecklist(),
        html.Div(id='shot-checklist-result'),
        html.Div(id='free-throw-result'),
        ShooterHeader(),
        PlayerDropdown(),
        PlayTypeDropdown(),
        ShotTypeDropdown(),
        RecordShotButton(),
        html.Div(id='click-coordinates'),
    ]
)

# Make | Miss | Free Throws | Turnover checklist callback
@app.callback(
    Output("shot-checklist-result", "children"),
    [Input("shot-checklist", "value")]
)
#  Make | Miss | Free Throws | Turnover checklist logic
def update_shot_result(value):
    if value == ['Miss']:
        shot['result'] = 0
        return
    elif value == ['Make']:
        shot['result'] = 1
        return
    elif value == ['Free Throws']:
        shot['result'] = 11
        return FreeThrowInput()
    elif value == ['Turnover']:
        shot['result'] = 20
        return

# Free Throws made callback
@app.callback(
    Output("free-throw-result", "children"),
    Input("free-throw-input", "value"),
)
def updateFreeThrows(value):
    shot['ftm'] = value
    return

# Player Dropdown callback
@app.callback(
    Output('player-dropdown-output-container', 'children'),
    Input('player-dropdown', 'value')
)
# Player Dropdown logic
def update_player(value):
    shot['player'] = value
    return

# Play-Type Dropdown callback
@app.callback(
    Output('play-type-dropdown-output-container', 'children'),
    Input('play-type-dropdown', 'value')
)
# Play-Type Dropdown logic
def update_play_type(value):
    shot['play_type'] = value
    return

# Shot-Type Dropdown callback
@app.callback(
    Output('shot-type-dropdown-output-container', 'children'),
    Input('shot-type-dropdown', 'value')
)
# Shot-Type Dropdown logic
def update_shot_type(value):
    shot['shot_type'] = value
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
        shot['y'] = y
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
                    color='rgb(2, 196, 222)',
                    size=15,
                    opacity=0.8,
                    symbol='x'
                ),
            )

            # Add the new marker trace to the figure
            figure['data'].append(new_marker_trace)

            # Update the layout to enable click events again
            figure['layout']['clickmode'] = 'event+select'

    return figure

# Record shot callback
@app.callback(
    Output("record-shot-output", "children"),
    [Input("record-shot-button", "n_clicks")],
)
def record_shot(value):
    if ('player' in shot) and ('play_type' in shot) and ('result' in shot) and ('shot_type' in shot):
        print(shot)
        updated_player_df = UpdatePlayerDF(shot)
        print(updated_player_df)
        return f'Recorded shot'
    else:
        return None

# Clear values in dropdowns and checklist when record shot button is pressed
@app.callback(    
    Output("shot-checklist", 'value'),
    Output("player-dropdown", 'value'),
    Output('shot-type-dropdown', 'value'),
    Output('play-type-dropdown', 'value'),
    [Input("record-shot-button", "n_clicks")],
)
def clear_components(value):
    if value is not None:
        return [[], '', '', '']
    else:
        return [], None, None, None
    
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
