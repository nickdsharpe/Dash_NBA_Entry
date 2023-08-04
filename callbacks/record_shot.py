from maindash import app
import dash
from dash.dependencies import Input, Output 
from update_player_df import UpdateShooterDF, UpdateCreatorDF


# Record shot callback
@app.callback(
    Output("team-one-record-shot-output", "children"),
    Output("team-two-record-shot-output", "children"),
    Output('shot-type', 'data', allow_duplicate=True),
    Output('shot-result', 'data', allow_duplicate=True),
    Output('play-type', 'data', allow_duplicate=True),
    Output('player', 'data', allow_duplicate=True),
    Output('shot-coordinates', 'data', allow_duplicate=True),
    Output('free-throws', 'data', allow_duplicate=True),
    
    Input("team-one-record-shot-button", "n_clicks"),
    Input("team-two-record-shot-button", "n_clicks"),
    Input('team-one-creation-checklist', 'value'),
    Input('shot-type', 'data'),
    Input('shot-result', 'data'),
    Input('play-type', 'data'),
    Input('player', 'data'),
    Input('shot-coordinates', 'data'),
    Input('free-throws', 'data'),
    
    prevent_initial_call=True,
)
def teamOne_RecordShot(team_one_n_clicks, team_two_n_clicks, creation_checklist, shot_type, shot_result, play_type, player, shot_coordinates, free_throws):
    
    cleared = {'team-one': {}, 'team-two': {}}
    
    shot_type = shot_type.copy()
    shot_result = shot_result.copy()
    play_type = play_type.copy()
    player = player.copy()
    shot_coordinates = shot_coordinates.copy()
    free_throws = free_throws.copy()
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Team One
    if triggered_input_id == "team-one-record-shot-button" and team_one_n_clicks is not None:
    
        try:
            team_one_shooter = {'result': shot_result['team-one']['shooter'],
                            'shot_type': shot_type['team-one']['shooter'],
                            'play_type': play_type['team-one']['shooter'],
                            'player': player['team-one']['shooter'],
                            'shot_coordinates': shot_coordinates['team-one'],
                            'free_throws': free_throws['team-one']['shooter'],}
            print('Shooter', team_one_shooter)
            updated_shooter_df = UpdateShooterDF(team_one_shooter)
            print(updated_shooter_df)
            
        except:
            try:
                team_one_shooter = {'result': shot_result['team-one']['shooter'],
                            'shot_type': shot_type['team-one']['shooter'],
                            'play_type': play_type['team-one']['shooter'],
                            'player': player['team-one']['shooter'],
                            'shot_coordinates': shot_coordinates['team-one']}
                print('Shooter', team_one_shooter)
                updated_shooter_df = UpdateShooterDF(team_one_shooter)
                print(updated_shooter_df)
                
            except:
                return 'Data Incomplete', None, shot_type, shot_result, play_type, player, shot_coordinates, free_throws
            
            
        try:
            if player['team-one']['creator']:
                try:
                    team_one_creator = {'result': shot_result['team-one']['creator'],
                                    'shot_type': shot_type['team-one']['creator'],
                                    'play_type': play_type['team-one']['creator'],
                                    'player': player['team-one']['creator'],
                                    'shot_coordinates': shot_coordinates['team-one'],
                                    'free_throws': free_throws['team-one']['creator'],}
                    print('creator', team_one_creator)
                    updated_creator_df = UpdateCreatorDF(team_one_creator)
                    print(updated_creator_df)
                    
                    team_one_n_clicks = None
                    return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared
                
                except:
                    try:
                        team_one_creator = {'result': shot_result['team-one']['creator'],
                                    'shot_type': shot_type['team-one']['creator'],
                                    'play_type': play_type['team-one']['creator'],
                                    'player': player['team-one']['creator'],
                                    'shot_coordinates': shot_coordinates['team-one']}
                        print('creator', team_one_creator)
                        updated_creator_df = UpdateCreatorDF(team_one_creator)
                        print(updated_creator_df)
                        
                        team_one_n_clicks = None
                        return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared
                        
                    except:
                        print('Data Incomplete')
            else:
                
                team_one_n_clicks = None
                return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared
        except:
            return 'Shot Recorded', None, shot_type, shot_result, play_type, player, shot_coordinates, free_throws
        
        
        
        
    # Team Two
    if triggered_input_id == "team-two-record-shot-button" and team_two_n_clicks is not None:
    
        try:
            team_two_shooter = {'result': shot_result['team-two']['shooter'],
                            'shot_type': shot_type['team-two']['shooter'],
                            'play_type': play_type['team-two']['shooter'],
                            'player': player['team-two']['shooter'],
                            'shot_coordinates': shot_coordinates['team-two'],
                            'free_throws': free_throws['team-two']['shooter'],}
            print('Shooter', team_two_shooter)
            updated_shooter_df = UpdateShooterDF(team_two_shooter)
            print(updated_shooter_df)
            
        except:
            try:
                team_two_shooter = {'result': shot_result['team-two']['shooter'],
                            'shot_type': shot_type['team-two']['shooter'],
                            'play_type': play_type['team-two']['shooter'],
                            'player': player['team-two']['shooter'],
                            'shot_coordinates': shot_coordinates['team-two']}
                print('Shooter', team_two_shooter)
                updated_shooter_df = UpdateShooterDF(team_two_shooter)
                print(updated_shooter_df)
                
            except:
                return None, 'Data Incomplete', shot_type, shot_result, play_type, player, shot_coordinates, free_throws
            
            
        try:
            if player['team-two']['creator']:
                print('Creator Reached')
                try:
                    team_two_creator = {'result': shot_result['team-two']['creator'],
                                    'shot_type': shot_type['team-two']['creator'],
                                    'play_type': play_type['team-two']['creator'],
                                    'player': player['team-two']['creator'],
                                    'shot_coordinates': shot_coordinates['team-two'],
                                    'free_throws': free_throws['team-two']['creator'],}
                    print('creator', team_two_creator)
                    updated_creator_df = UpdateCreatorDF(team_two_creator)
                    print(updated_creator_df)
                    
                    team_two_n_clicks = None
                    return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared
                
                except:
                    try:
                        team_two_creator = {'result': shot_result['team-two']['creator'],
                                    'shot_type': shot_type['team-two']['creator'],
                                    'play_type': play_type['team-two']['creator'],
                                    'player': player['team-two']['creator'],
                                    'shot_coordinates': shot_coordinates['team-two']}
                        print('creator', team_two_creator)
                        updated_creator_df = UpdateCreatorDF(team_two_creator)
                        print(updated_creator_df)
                        
                        team_two_n_clicks = None
                        return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared
                        
                    except:
                        print('Data Incomplete')
            else:
                
                team_two_n_clicks = None
                return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared
        except:
            return None, 'Shot Recorded', shot_type, shot_result, play_type, player, shot_coordinates, free_throws
            
    
    return None, None, shot_type, shot_result, play_type, player, shot_coordinates, free_throws