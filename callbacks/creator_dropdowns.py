from maindash import app
from dash.dependencies import Input, Output

# Record Creator player dropdown
@app.callback(
        Output('store-data', 'data', allow_duplicate=True),
        Input('team-one-passing-player-dropdown', 'value'),
        Input('team-two-passing-player-dropdown', 'value'),
        Input('store-data', 'data'),
        prevent_initial_call=True
)
def teamOne_UpdateCreatorPlayer(team_one_value, team_two_value, data):
    updated_data = data.copy()
    team_one_creator = updated_data['team-one-creator']
    team_two_creator = updated_data['team-two-creator']
    
    if team_one_value:
        team_one_creator['player'] = team_one_value
        return updated_data
    
    if team_two_value:
        team_two_creator['player'] = team_two_value
        return updated_data
    return updated_data

# Record Creator Play Type dropdown
@app.callback(
        Output('store-data', 'data', allow_duplicate=True),
        Input('team-one-passing-play-type-dropdown', 'value'),
        Input('team-two-passing-play-type-dropdown', 'value'),   
        Input('store-data', 'data'),
        prevent_initial_call=True
)
def teamOne_UpdateCreatorPlayType(team_one_value, team_two_value, data):
    updated_data = data.copy()
    team_one_creator = updated_data['team-one-creator']
    team_two_creator = updated_data['team-two-creator']
    
    if team_one_value:
        team_one_creator['play_type'] = team_one_value
        return updated_data
    
    if team_two_value:
        team_two_creator['play_type'] = team_two_value
        return updated_data
    return updated_data