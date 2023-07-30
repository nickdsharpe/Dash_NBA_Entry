from maindash import app
import callbacks.add_marker, callbacks.shot_result, callbacks.free_throw_input, callbacks.shooter_dropdown, callbacks.shooter_play_type, callbacks.record_coordinates, callbacks.shot_type
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from components import PlayerDropdown, PlayTypeDropdown, ShooterHeader, MakePlayerDictionaries, RecordShotButton, ShotChecklist, FreeThrowInput, ClearLocationDataButton, PassingPlayerDropdown, PasserHeader, PassingPlayTypeDropdown
from update_player_df import UpdateShooterDF, UpdateCreatorDF
from assets.court import is_inside_three_point_line
from layout import make_layout

player_dfs = MakePlayerDictionaries()
shot, passer = {}, {}
fig = go.Figure()

# Layout
app.layout = make_layout()

# Callback to display Creation dropdowns
@app.callback(
        Output('team-one-creation-inputs-container', 'children'),
        Input('team-one-creation-checklist', 'value')
)
def teamOne_CreatorInputs(value):
    if value:
        return PasserHeader('team-one') ,PassingPlayerDropdown('team-one'), PassingPlayTypeDropdown('team-one')

# Record Creator player dropdown
@app.callback(
        Output('team-one-passing-player-dropdown-output-container', 'children'),
        Input('team-one-passing-player-dropdown', 'value'),
        prevent_initial_call=True
)
def teamOne_UpdateCreatorPlayer(value):
    if value:
        passer['player'] = value
    return None

# Record Creator Play Type dropdown
@app.callback(
        Output('team-one-passing-play-type-dropdown-output-container', 'children'),
        Input('team-one-passing-play-type-dropdown', 'value'),
        prevent_initial_call=True
)
def teamOne_UpdateCreatorPlayType(value):
    if value:
        passer['play_type'] = value
    return None

# Record shot callback
@app.callback(
    Output("team-one-record-shot-output", "children"),
    [Input("team-one-record-shot-button", "n_clicks")],
    prevent_initial_call=True,
)
def teamOne_RecordShot(value):
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
def teamOne_ClearComponents(value):
    if value is not None:
        return [[], '', '', []]
    else:
        return [], None, None, []

'''TEAM-TWO CALLBACKS'''    

# Callback to display Creation dropdowns
@app.callback(
        Output('team-two-creation-inputs-container', 'children'),
        Input('team-two-creation-checklist', 'value')
)
def teamTwo_CreatorInputs(value):
    if value:
        return PasserHeader('team-two') ,PassingPlayerDropdown('team-two'), PassingPlayTypeDropdown('team-two')

# Record Creator player dropdown
@app.callback(
        Output('team-two-passing-player-dropdown-output-container', 'children'),
        Input('team-two-passing-player-dropdown', 'value'),
        prevent_initial_call=True
)
def teamTwo_CreatorPlayer(value):
    if value:
        passer['player'] = value
    return None

# Record Creator Play Type dropdown
@app.callback(
        Output('team-two-passing-play-type-dropdown-output-container', 'children'),
        Input('team-two-passing-play-type-dropdown', 'value'),
        prevent_initial_call=True
)
def teamTwo_CreatorPlayType(value):
    if value:
        passer['play_type'] = value
    return None

# Record shot callback
@app.callback(
    Output("team-two-record-shot-output", "children"),
    [Input("team-two-record-shot-button", "n_clicks")],
    prevent_initial_call=True,
)
def teamTwo_RecordShot(value):
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
    Output("team-two-shot-checklist", 'value'),
    Output("team-two-player-dropdown", 'value'),
    Output('team-two-play-type-dropdown', 'value'),
    Output('team-two-creation-checklist', 'value'),
    [Input("team-two-record-shot-button", "n_clicks")],
    allow_duplicate=True
)
def teamTwo_ClearClearComponents(value):
    if value is not None:
        return [[], '', '', []]
    else:
        return [], None, None, []

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
