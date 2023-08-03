from maindash import app
import dash
from dash.dependencies import Input, Output 
from update_player_df import UpdateShooterDF, UpdateCreatorDF


# Record shot callback
@app.callback(
    Output("team-one-record-shot-output", "children"),
    Output("team-two-record-shot-output", "children"),
    
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

    shot_type = shot_type.copy()
    shot_result = shot_result.copy()
    play_type = play_type.copy()
    player = player.copy()
    shot_coordinates = shot_coordinates.copy()
    free_throws = free_throws.copy()
    
    if team_one_n_clicks is not None:
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
                print('Data Incomplete')

        if creation_checklist:
            print('Creator Reached')
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
                    
                except:
                    print('Data Incomplete')
    
    return None, None