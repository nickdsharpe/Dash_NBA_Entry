import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_daq as daq
from entry_from import ToggleSwitch, PlayerDropdown, PlayTypeDropdown, ShooterHeader, ShotTypeDropdown, MakePlayerDictionaries, RecordShotButton
from update_player_df import UpdatePlayerDF
from court import draw_plotly_court
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

player_dfs = MakePlayerDictionaries()
shot = {}
shot_df = pd.DataFrame(
    columns=['player', 'play_type', 'shot_type', 'make_miss'])
fig = go.Figure()
# Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    children=[
        html.H2("PPP Entry Form"),
        html.Div(draw_plotly_court(fig), id='court-plot'),
        html.Div(id='click-coordinates'),
        ToggleSwitch(),
        # ShooterHeader(),
        PlayerDropdown(),
        PlayTypeDropdown(),
        ShotTypeDropdown(),
        html.Div(id='shot-switch-result'),
        RecordShotButton(),
    ]
)

# Make or Miss Toggle callback
@app.callback(
    Output("shot-switch-result", "children"),
    [Input("shot-switch", "value")]
)
# Make or Miss Toggle switch logic
def update_shot_result(value):
    if value:
        shot['result'] = 0
        return "Miss"
    else:
        shot['result'] = 1
        return "Make"

# Player Dropdown callback
@app.callback(
    Output('player-dropdown-output-container', 'children'),
    Input('player-dropdown', 'value')
)
# Player Dropdown logic
def update_player(value):
    shot['player'] = value
    return value

# Play-Type Dropdown callback
@app.callback(
    Output('play-type-dropdown-output-container', 'children'),
    Input('play-type-dropdown', 'value')
)
# Play-Type Dropdown logic
def update_play_type(value):
    shot['play_type'] = value
    return f'You have selected {value}'

# Shot-Type Dropdown callback
@app.callback(
    Output('shot-type-dropdown-output-container', 'children'),
    Input('shot-type-dropdown', 'value')
)
# Shot-Type Dropdown logic
def update_shot_type(value):
    shot['shot_type'] = value
    return f'You have selected {value}'

# Track click events
@app.callback(
    Output('click-coordinates', 'children'),
    Input('court-graph', 'clickData')
)
def record_coordinates(clickData):
    print('Click registered')
    if clickData is not None:
        x = clickData['points'][0]['x']
        y = clickData['points'][0]['y']
        return f'Shot coordinates: ({x}, {y})'
    else:
        return ''

# Record shot callback
@app.callback(
    Output("record-shot-output", "children"),
    [Input("record-shot-button", "n_clicks")]
)
def record_shot(value):
    if shot['player'] is not None:
        updated_player_df = UpdatePlayerDF(shot)
        print(updated_player_df)
        return f'Recorded shot'


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
