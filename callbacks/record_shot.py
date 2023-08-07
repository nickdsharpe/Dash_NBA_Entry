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
    Input('shot-type', 'data'),
    Input('shot-result', 'data'),
    Input('play-type', 'data'),
    Input('player', 'data'),
    Input('shot-coordinates', 'data'),
    Input('free-throws', 'data'),
    
    prevent_initial_call=True,
)
def teamOne_RecordShot(team_one_n_clicks, team_two_n_clicks, shot_type, shot_result, play_type, player, shot_coordinates, free_throws):

    cleared = [{}, {}]
    
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
            team_one_shooter = {'result': shot_result[0]['shooter'],
                            'shot_type': shot_type[0]['shooter'],
                            'play_type': play_type[0]['shooter'],
                            'player': player[0]['shooter'],
                            'shot_coordinates': shot_coordinates[0],
                            'free_throws': free_throws[0]['shooter'],}
            
            updated_shooter_df = UpdateShooterDF(team_one_shooter)
            print(team_one_shooter['player'], updated_shooter_df)
            
        except:
            try:
                team_one_shooter = {'result': shot_result[0]['shooter'],
                            'shot_type': shot_type[0]['shooter'],
                            'play_type': play_type[0]['shooter'],
                            'player': player[0]['shooter'],
                            'shot_coordinates': shot_coordinates[0]}
    
                updated_shooter_df = UpdateShooterDF(team_one_shooter)
                print(team_one_shooter['player'], updated_shooter_df)
                
            except:
                return 'Data Incomplete', None, cleared, cleared, cleared, cleared, cleared, cleared
            
        try:
            if player[0]['creator']:
                try:
                    team_one_creator = {'result': shot_result[0]['creator'],
                                    'shot_type': shot_type[0]['creator'],
                                    'play_type': play_type[0]['creator'],
                                    'player': player[0]['creator'],
                                    'shot_coordinates': shot_coordinates[0],
                                    'free_throws': free_throws[0]['creator'],}
    
                    updated_creator_df = UpdateCreatorDF(team_one_creator)
                    print(team_one_creator['player'], updated_creator_df)
                    
                    team_one_n_clicks = None
                    return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared
                
                except:
                    try:
                        team_one_creator = {'result': shot_result[0]['creator'],
                                    'shot_type': shot_type[0]['creator'],
                                    'play_type': play_type[0]['creator'],
                                    'player': player[0]['creator'],
                                    'shot_coordinates': shot_coordinates[0]}
      
                        updated_creator_df = UpdateCreatorDF(team_one_creator)
                        print(team_one_creator['player'], updated_creator_df)
                        
                        team_one_n_clicks = None
                        return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared
                        
                    except:
                        return 'Data Incomplete', None, cleared, cleared, cleared, cleared, cleared, cleared
            else:
                
                team_one_n_clicks = None
                return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared
        except:
            return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared
        
        
        
        
    # Team Two
    if triggered_input_id == "team-two-record-shot-button" and team_two_n_clicks is not None:
    
        try:
            team_two_shooter = {'result': shot_result[1]['shooter'],
                            'shot_type': shot_type[1]['shooter'],
                            'play_type': play_type[1]['shooter'],
                            'player': player[1]['shooter'],
                            'shot_coordinates': shot_coordinates[1],
                            'free_throws': free_throws[1]['shooter'],}
            
            updated_shooter_df = UpdateShooterDF(team_two_shooter)
            print(team_two_shooter['player'], updated_shooter_df)
            
        except:
            try:
                team_two_shooter = {'result': shot_result[1]['shooter'],
                            'shot_type': shot_type[1]['shooter'],
                            'play_type': play_type[1]['shooter'],
                            'player': player[1]['shooter'],
                            'shot_coordinates': shot_coordinates[1]}
    
                updated_shooter_df = UpdateShooterDF(team_two_shooter)
                print(team_two_shooter['player'], updated_shooter_df)
                
            except:
                return None, 'Data Incomplete', cleared, cleared, cleared, cleared, cleared, cleared
            
        try:
            if player[1]['creator']:
                try:
                    team_two_creator = {'result': shot_result[1]['creator'],
                                    'shot_type': shot_type[1]['creator'],
                                    'play_type': play_type[1]['creator'],
                                    'player': player[1]['creator'],
                                    'shot_coordinates': shot_coordinates[1],
                                    'free_throws': free_throws[1]['creator'],}
    
                    updated_creator_df = UpdateCreatorDF(team_two_creator)
                    print(team_two_creator['player'], updated_creator_df)
                    
                    team_two_n_clicks = None
                    return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared
                
                except:
                    try:
                        team_two_creator = {'result': shot_result[1]['creator'],
                                    'shot_type': shot_type[1]['creator'],
                                    'play_type': play_type[1]['creator'],
                                    'player': player[1]['creator'],
                                    'shot_coordinates': shot_coordinates[1]}
      
                        updated_creator_df = UpdateCreatorDF(team_two_creator)
                        print(team_two_creator['player'], updated_creator_df)
                        
                        team_two_n_clicks = None
                        return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared
                        
                    except:
                        return None, 'Data Incomplete', cleared, cleared, cleared, cleared, cleared, cleared
            else:
                
                team_two_n_clicks = None
                return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared
        except:
            return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared
            
    
    return None, None, shot_type, shot_result, play_type, player, shot_coordinates, free_throws