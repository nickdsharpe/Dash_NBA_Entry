from maindash import app
import dash
from dash.dependencies import Input, Output
from unidecode import unidecode

play_type_ids = {'PNR Ball Handler': 1, "PNR Screener": 2, "DHO Ball Handler": 3, "DHO Ball Screener": 4, "Isolation": 5, "Transition": 6, "Attacking Closeouts": 7, "Catch & Shoot": 8, "Off Ball Screens": 9, "Cutting": 10, "Offensive Rebounds": 11}

# Record Creator player dropdown
@app.callback(
        Output('player', 'data', allow_duplicate=True),
        
        Input('team-one-player-dropdown', 'value'),
        Input('team-two-player-dropdown', 'value'),
        Input('team-one-passing-player-dropdown', 'value'),
        Input('team-two-passing-player-dropdown', 'value'),
        Input('player', 'data'),
        Input('player-ids', 'data'),
        prevent_initial_call=True
)
def teamOne_UpdateCreatorPlayer(team_one_shooter, team_two_shooter, team_one_creator, team_two_creator, data, player_ids):
    
    updated_data = data.copy()
 
    team_one = updated_data[0]
    team_two = updated_data[1]
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-player-dropdown":
        
        if team_one_shooter:
            team_one_shooter = unidecode(team_one_shooter)
            team_one['shooter'] = player_ids[0]['home'][team_one_shooter]
            
            return updated_data
        
    elif triggered_input_id == "team-two-player-dropdown":
        
        if team_two_shooter:
            team_two_shooter = unidecode(team_two_shooter)
            team_two['shooter'] = player_ids[1]['away'][team_two_shooter]
            
            return updated_data

    
    if triggered_input_id == "team-one-passing-player-dropdown":
        
        if team_one_creator:
            team_one_creator = unidecode(team_one_creator)
            team_one['creator'] = player_ids[0]['home'][team_one_creator]
            
            return updated_data
        
    elif triggered_input_id == "team-two-passing-player-dropdown":
        
        if team_two_creator:
            team_two_creator = unidecode(team_two_creator)
            team_two['creator'] = player_ids[1]['away'][team_two_creator]
            
            return updated_data
        
    return updated_data

# Record Play-Type dropdown
@app.callback(
        Output('play-type', 'data', allow_duplicate=True),
        
        Input('team-one-play-type-dropdown', 'value'),
        Input('team-two-play-type-dropdown', 'value'),
        Input('team-one-passing-play-type-dropdown', 'value'),
        Input('team-two-passing-play-type-dropdown', 'value'),
        Input('play-type', 'data'),
        prevent_initial_call=True
)
def teamOne_UpdateCreatorPlayer(team_one_shooter, team_two_shooter, team_one_creator, team_two_creator, data):
    
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]

    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-play-type-dropdown":
        
        if team_one_shooter:
            team_one['shooter'] = play_type_ids[team_one_shooter]
            
            return updated_data
        
    elif triggered_input_id == "team-two-play-type-dropdown":
        
        if team_two_shooter:
            team_two['shooter'] = play_type_ids[team_two_shooter]
            
            return updated_data

    
    if triggered_input_id == "team-one-passing-play-type-dropdown":
        
        if team_one_creator:
            team_one['creator'] = play_type_ids[team_one_creator]
            
            return updated_data
        
    elif triggered_input_id == "team-two-passing-play-type-dropdown":
        
        if team_two_creator:
            team_two['creator'] = play_type_ids[team_two_creator]
            
            return updated_data
        
    return updated_data