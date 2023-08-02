from maindash import app
import callbacks.add_marker, callbacks.shot_result, callbacks.free_throw_input, callbacks.record_coordinates, callbacks.shot_type, callbacks.player_and_play_type
import dash
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from components import MakePlayerDictionaries, PassingPlayerDropdown, PasserHeader, PassingPlayTypeDropdown
from update_player_df import UpdateShooterDF, UpdateCreatorDF
from layout import make_layout

player_dfs = MakePlayerDictionaries()
shot, passer = {}, {}
fig = go.Figure()

# Layout
app.layout = make_layout()

# Callback to display Creation dropdowns
@app.callback(
        Output('team-one-creation-inputs-container', 'style'),
        Input('team-one-creation-checklist', 'value'),
        prevent_initial_call=True
)
def teamOne_CreatorInputs(value):
    if value:
        return {'display': 'block'}
    else:
        return {'display': 'none'}

# Record shot callback
@app.callback(
    Output("team-one-record-shot-output", "children"),
    Input("team-one-record-shot-button", "n_clicks"),
    prevent_initial_call=True,
)
def teamOne_RecordShot(n_clicks, data):
    updated_data = data.copy()
    shooter = updated_data['team-one-shooter']
    creator = updated_data['team-one-creator']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print('Record Shot Pressed')

    if triggered_input_id == "team-one-record-shot-button":
        try:
            updated_shooter_df = UpdateShooterDF(shooter)
            updated_creator_df = UpdateCreatorDF(creator)
            print('Shooter:', updated_shooter_df)
            print('Creator', updated_creator_df)
            updated_data = {'team-one-shooter' : {}, 'team-one-creator': {}, 'team-two-shooter' : {}, 'team-two-creator': {}}
            return 'Shot Recorded', updated_data
        except:
            return 'Data Incomplete.', updated_data
    return '', updated_data
    
# Clear values in dropdowns and checklist when record shot button is pressed
@app.callback(    
    Output("team-one-shot-checklist", 'value', allow_duplicate=True),
    Output("team-one-player-dropdown", 'value'),
    Output('team-one-play-type-dropdown', 'value'),
    Output('team-one-passing-player-dropdown', 'value'),
    Output('team-one-passing-play-type-dropdown', 'value'),
    Output('team-one-creation-checklist', 'value'),
    [Input("team-one-record-shot-button", "n_clicks")],
    prevent_initial_call=True
)
def teamOne_ClearComponents(n_clicks):
    if n_clicks is not None:
        return [[], '', '', '', '', []]
    else:
        return [], None, None, None, None, []

'''TEAM-TWO CALLBACKS'''    

# Callback to display Creation dropdowns
@app.callback(
        Output('team-two-creation-inputs-container', 'style'),
        Input('team-two-creation-checklist', 'value'),
        prevent_initial_call=True
)
def teamTwo_CreatorInputs(value):
    if value:
        return {'display': 'block'}
    else:
        return {'display': 'none'}

# Record shot callback
@app.callback(
    Output("team-two-record-shot-output", "children"),
    Input("team-two-record-shot-button", "n_clicks"),
    prevent_initial_call=True,
)
def teamTwo_RecordShot(n_clicks, data):
    updated_data = data.copy()
    shooter = updated_data['team-two-shooter']
    creator = updated_data['team-two-creator']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if triggered_input_id == "team-two-record-shot-button":
        try:
            updated_shooter_df = UpdateShooterDF(shooter)
            updated_creator_df = UpdateCreatorDF(creator)
            print('Shooter:', updated_shooter_df)
            print('Creator', updated_creator_df)
            updated_data = {'team-one-shooter' : {}, 'team-one-creator': {}, 'team-two-shooter' : {}, 'team-two-creator': {}}
            return 'Shot Recorded', updated_data
        except:
            return 'Data Incomplete.', updated_data
    return '', updated_data
    
# Clear values in dropdowns and checklist when record shot button is pressed
@app.callback(    
    Output("team-two-shot-checklist", 'value', allow_duplicate=True),
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
