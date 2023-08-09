from maindash import app
import dash
from dash.dependencies import Input, Output 
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
    
    prevent_initial_call=True,
)
def teamOne_RecordShot(team_one_n_clicks, team_two_n_clicks, shot_type, shot_result, play_type, player, defender, shot_coordinates, shot_quality, free_throws):

    cleared = [{}, {}]
    
    shot_type = shot_type.copy()
    shot_result = shot_result.copy()
    play_type = play_type.copy()
    player = player.copy()
    defender = defender.copy()
    shot_coordinates = shot_coordinates.copy()
    shot_quality = shot_quality.copy()
    free_throws = free_throws.copy()

    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(defender)
    # Team One
    if triggered_input_id == "team-one-record-shot-button" and team_one_n_clicks is not None:
    
        try:
            team_one_shooter = {'result': shot_result[0]['shooter'],
                            'shot_type': shot_type[0]['shooter'],
                            'play_type': play_type[0]['shooter'],
                            'player': player[0]['shooter'],
                            'shot_coordinates': shot_coordinates[0],
                            'shot_quality': shot_quality[0]['shooter'],
                            'free_throws': free_throws[0]['shooter'],}
            
            updated_shooter_df = UpdateShooterDF(team_one_shooter, 'team_one')
            print(team_one_shooter['player'], updated_shooter_df)
            
        except:
            try:
                team_one_shooter = {'result': shot_result[0]['shooter'],
                            'shot_type': shot_type[0]['shooter'],
                            'play_type': play_type[0]['shooter'],
                            'player': player[0]['shooter'],
                            'shot_coordinates': shot_coordinates[0],
                            'shot_quality': shot_quality[0]['shooter'],}
    
                updated_shooter_df = UpdateShooterDF(team_one_shooter, 'team_one')
                print(team_one_shooter['player'], updated_shooter_df)
                
            except:
                return 'Data Incomplete', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
        
        ### DEFENDER ###
        if defender[0]['shooter']:
            print('Defender logic reached')
            try:
                team_one_defender = {'result': shot_result[0]['shooter'],
                                'shot_type': shot_type[0]['shooter'],
                                'play_type': play_type[0]['shooter'],
                                'player': defender[0]['shooter'],
                                'shot_coordinates': shot_coordinates[0],
                                'shot_quality': shot_quality[0]['shooter'],
                                'free_throws': free_throws[0]['shooter'],}
                
                updated_shooter_df = UpdateDefenderDF(team_one_defender, 'team_one')
                print(team_one_defender['player'], updated_shooter_df)
                
            except:
                try:
                    team_one_defender = {'result': shot_result[0]['shooter'],
                                'shot_type': shot_type[0]['shooter'],
                                'play_type': play_type[0]['shooter'],
                                'player': defender[0]['shooter'],
                                'shot_coordinates': shot_coordinates[0],
                                'shot_quality': shot_quality[0]['shooter'],}
        
                    updated_shooter_df = UpdateDefenderDF(team_one_defender, 'team_one')
                    print(team_one_defender['player'], updated_shooter_df)
                    
                except:
                    return 'Data Incomplete', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
    
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
                                    'free_throws': free_throws[0]['creator'],}
    
                    updated_creator_df = UpdateCreatorDF(team_one_creator, 'team_one')
                    print(team_one_creator['player'], updated_creator_df)
                    
                    team_one_n_clicks = None
                    return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
                
                except:
                    try:
                        team_one_creator = {'result': shot_result[0]['creator'],
                                    'shot_type': shot_type[0]['creator'],
                                    'play_type': play_type[0]['creator'],
                                    'player': player[0]['creator'],
                                    'shot_coordinates': shot_coordinates[0],
                                    'shot_quality': shot_quality[0]['creator'],}
      
                        updated_creator_df = UpdateCreatorDF(team_one_creator, 'team_one')
                        print(team_one_creator['player'], updated_creator_df)
                        
                        team_one_n_clicks = None
                        return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
                        
                    except:
                        return 'Data Incomplete', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
            else:
                
                team_one_n_clicks = None
                return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
        except:
            return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
        
        
        
        
    # Team Two
    if triggered_input_id == "team-two-record-shot-button" and team_two_n_clicks is not None:
    
        try:
            team_two_shooter = {'result': shot_result[1]['shooter'],
                            'shot_type': shot_type[1]['shooter'],
                            'play_type': play_type[1]['shooter'],
                            'player': player[1]['shooter'],
                            'shot_coordinates': shot_coordinates[1],
                            'shot_quality': shot_quality[1]['shooter'],
                            'free_throws': free_throws[1]['shooter'],}
            
            updated_shooter_df = UpdateShooterDF(team_two_shooter, 'team_two')
            print(team_two_shooter['player'], updated_shooter_df)
            
        except:
            try:
                team_two_shooter = {'result': shot_result[1]['shooter'],
                            'shot_type': shot_type[1]['shooter'],
                            'play_type': play_type[1]['shooter'],
                            'player': player[1]['shooter'],
                            'shot_coordinates': shot_coordinates[1],
                            'shot_quality': shot_quality[1]['shooter'],}
    
                updated_shooter_df = UpdateShooterDF(team_two_shooter, 'team_two')
                print(team_two_shooter['player'], updated_shooter_df)
                
            except:
                return None, 'Data Incomplete', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
            
        try:
            if player[1]['creator']:
                try:
                    team_two_creator = {'result': shot_result[1]['creator'],
                                    'shot_type': shot_type[1]['creator'],
                                    'play_type': play_type[1]['creator'],
                                    'player': player[1]['creator'],
                                    'shot_coordinates': shot_coordinates[1],
                                    'shot_quality': shot_quality[1]['creator'],
                                    'free_throws': free_throws[1]['creator'],}
    
                    updated_creator_df = UpdateCreatorDF(team_two_creator, 'team_two')
                    print(team_two_creator['player'], updated_creator_df)
                    
                    team_two_n_clicks = None
                    return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
                
                except:
                    try:
                        team_two_creator = {'result': shot_result[1]['creator'],
                                    'shot_type': shot_type[1]['creator'],
                                    'play_type': play_type[1]['creator'],
                                    'player': player[1]['creator'],
                                    'shot_coordinates': shot_coordinates[1],
                                    'shot_quality': shot_quality[1]['creator'],}
      
                        updated_creator_df = UpdateCreatorDF(team_two_creator, 'team_two')
                        print(team_two_creator['player'], updated_creator_df)
                        
                        team_two_n_clicks = None
                        return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
                        
                    except:
                        return None, 'Data Incomplete', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
            else:
                
                team_two_n_clicks = None
                return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
        except:
            return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared
            
    
    return None, None, shot_type, shot_result, play_type, player, defender, shot_coordinates, shot_quality, free_throws