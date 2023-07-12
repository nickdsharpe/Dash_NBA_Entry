import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_daq as daq
from entry_form import PlayerDropdown, PlayTypeDropdown, ShooterHeader, ShotTypeDropdown, MakePlayerDictionaries, RecordShotButton, ShotChecklist, FreeThrows
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
        ShotChecklist(),
        html.Div(id='shot-checklist-result'),
        FreeThrows(),
        html.Div(id='free-throw-result'),
        # ShooterHeader(),
        PlayerDropdown(),
        PlayTypeDropdown(),
        ShotTypeDropdown(),
        RecordShotButton(),
        html.Div(id='clear-components-output'),
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
        return
    elif value == ['Turnover']:
        shot['result'] = 20
        return

# Free Throws made callback
@app.callback(
    Output("free-throw-result", "children"),
    Input("free-throw-input", "value"),
)
def update_output(value):
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
