from maindash import app
import dash
from dash import no_update
from dash.dependencies import Input, Output , State
from update_player_df import UpdateShooterDF, UpdateCreatorDF, UpdateDefenderDF

# Record shot callback
@app.callback(
    Output("team-one-record-shot-output", "children"),
    Output("team-two-record-shot-output", "children"),
    Output('shot-type', 'data', allow_duplicate=True),
    Output('shot-result', 'data', allow_duplicate=True),
    Output('play-type', 'data', allow_duplicate=True),
    Output('player', 'data', allow_duplicate=True),
    Output('defender', 'data', allow_duplicate=True),
    Output('shot-coordinates', 'data', allow_duplicate=True),
    Output('shot-quality', 'data', allow_duplicate=True),
    Output('free-throws', 'data', allow_duplicate=True),
    Output('shot-zone', 'data', allow_duplicate=True),
    Output('clear-components-flag', 'data', allow_duplicate=True),
    
    Input("team-one-record-shot-button", "n_clicks"),
    Input("team-two-record-shot-button", "n_clicks"),
    Input('shot-type', 'data'),
    Input('shot-result', 'data'),
    Input('play-type', 'data'),
    Input('player', 'data'),
    Input('defender', 'data'),
    Input('shot-coordinates', 'data'),
    Input('shot-quality', 'data'),
    Input('free-throws', 'data'),
    Input('shot-zone', 'data'),
    
    prevent_initial_call=True,
)
def teamOne_RecordShot(team_one_n_clicks, team_two_n_clicks, shot_type, shot_result, play_type, player, defender, shot_coordinates, shot_quality, free_throws, shot_zone):

    cleared = [{}, {}]
    
    shot_type = shot_type.copy()
    shot_result = shot_result.copy()
    play_type = play_type.copy()
    player = player.copy()
    defender = defender.copy()
    shot_coordinates = shot_coordinates.copy()
    shot_quality = shot_quality.copy()
    free_throws = free_throws.copy()
    shot_zone = shot_zone.copy()

    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Team One
    if triggered_input_id == "team-one-record-shot-button" and team_one_n_clicks is not None:

        ### SHOOTER ###
        try:
            team_one_shooter = {'result': shot_result[0]['shooter'],
                            'shot_type': shot_type[0]['shooter'],
                            'play_type': play_type[0]['shooter'],
                            'player': player[0]['shooter'],
                            'shot_coordinates': shot_coordinates[0],
                            'shot_quality': shot_quality[0]['shooter'],
                            'free_throws': free_throws[0]['shooter'],
                            'shot_zone': shot_zone[0]['shooter'],}
            
            if defender[0]['shooter']:
                team_one_shooter['defender'] = defender[0]['shooter']
            
            updated_shooter_df = UpdateShooterDF(team_one_shooter, 'team_one')
            updated_defender_df = UpdateDefenderDF(team_one_shooter, 'team_two')
            
        except:
            try:
                team_one_shooter = {'result': shot_result[0]['shooter'],
                            'shot_type': shot_type[0]['shooter'],
                            'play_type': play_type[0]['shooter'],
                            'player': player[0]['shooter'],
                            'shot_coordinates': shot_coordinates[0],
                            'shot_quality': shot_quality[0]['shooter'],
                            'shot_zone': shot_zone[0]['shooter'],}
    
                if defender[0]['shooter']:
                    team_one_shooter['defender'] = defender[0]['shooter']
                updated_shooter_df = UpdateShooterDF(team_one_shooter, 'team_one')
                updated_defender_df = UpdateDefenderDF(team_one_shooter, 'team_two')
                
            except:
                return 'Data Incomplete', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
        
        ### CREATOR ###
        try:
            if player[0]['creator']:
                try:
                    team_one_creator = {'result': shot_result[0]['creator'],
                                    'shot_type': shot_type[0]['creator'],
                                    'play_type': play_type[0]['creator'],
                                    'player': player[0]['creator'],
                                    'shot_coordinates': shot_coordinates[0],
                                    'shot_quality': shot_quality[0]['creator'],
                                    'free_throws': free_throws[0]['creator'],
                                    'shot_zone': shot_zone[0]['creator'],}
    
                    updated_creator_df = UpdateCreatorDF(team_one_creator, 'team_one')
                    
                    team_one_n_clicks = None
                    return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
                
                except:
                    try:
                        team_one_creator = {'result': shot_result[0]['creator'],
                                    'shot_type': shot_type[0]['creator'],
                                    'play_type': play_type[0]['creator'],
                                    'player': player[0]['creator'],
                                    'shot_coordinates': shot_coordinates[0],
                                    'shot_quality': shot_quality[0]['creator'],
                                    'shot_zone': shot_zone[0]['creator'],}
      
                        updated_creator_df = UpdateCreatorDF(team_one_creator, 'team_one')
                        
                        team_one_n_clicks = None
                        return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
                        
                    except:
                        return 'Data Incomplete', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
            else:
                
                team_one_n_clicks = None
                return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
        except:
            return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
        
        
        
        
    # Team Two
    if triggered_input_id == "team-two-record-shot-button" and team_two_n_clicks is not None:

        ### SHOOTER ###
        try:
            team_two_shooter = {'result': shot_result[1]['shooter'],
                            'shot_type': shot_type[1]['shooter'],
                            'play_type': play_type[1]['shooter'],
                            'player': player[1]['shooter'],
                            'shot_coordinates': shot_coordinates[1],
                            'shot_quality': shot_quality[1]['shooter'],
                            'free_throws': free_throws[1]['shooter'],
                            'shot_zone': shot_zone[1]['shooter'],}

            if defender[1]['shooter']:
                team_two_shooter['defender'] = defender[1]['shooter']
            
            updated_shooter_df = UpdateShooterDF(team_two_shooter, 'team_two')
            updated_defender_df = UpdateDefenderDF(team_two_shooter, 'team_one')
            
        except:
            try:
                team_two_shooter = {'result': shot_result[1]['shooter'],
                            'shot_type': shot_type[1]['shooter'],
                            'play_type': play_type[1]['shooter'],
                            'player': player[1]['shooter'],
                            'shot_coordinates': shot_coordinates[1],
                            'shot_quality': shot_quality[1]['shooter'],
                            'shot_zone': shot_zone[1]['shooter'],}
    
                if defender[1]['shooter']:
                    team_two_shooter['defender'] = defender[1]['shooter']
                    
                updated_shooter_df = UpdateShooterDF(team_two_shooter, 'team_two')
                updated_defender_df = UpdateDefenderDF(team_two_shooter, 'team_one')
                
            except:
                return None, 'Data Incomplete', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
        
        ### CREATOR ###
        try:
            if player[1]['creator']:
                try:
                    team_two_creator = {'result': shot_result[1]['creator'],
                                    'shot_type': shot_type[1]['creator'],
                                    'play_type': play_type[1]['creator'],
                                    'player': player[1]['creator'],
                                    'shot_coordinates': shot_coordinates[1],
                                    'shot_quality': shot_quality[1]['creator'],
                                    'free_throws': free_throws[1]['creator'],
                                    'shot_zone': shot_zone[1]['shooter'],}
    
                    updated_creator_df = UpdateCreatorDF(team_two_creator, 'team_two')
                    
                    team_two_n_clicks = None
                    return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
                
                except:
                    try:
                        team_two_creator = {'result': shot_result[1]['creator'],
                                    'shot_type': shot_type[1]['creator'],
                                    'play_type': play_type[1]['creator'],
                                    'player': player[1]['creator'],
                                    'shot_coordinates': shot_coordinates[1],
                                    'shot_quality': shot_quality[1]['creator'],
                                    'shot_zone': shot_zone[1]['shooter'],}
      
                        updated_creator_df = UpdateCreatorDF(team_two_creator, 'team_two')
                        
                        team_two_n_clicks = None
                        return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
                        
                    except:
                        return None, 'Data Incomplete', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
            else:
                
                team_two_n_clicks = None
                return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
        except:
            return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, True
        
    return no_update
    