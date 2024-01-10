from maindash import app
import dash
from dash import no_update
from dash.dependencies import Input, Output
import csv

def append_to_csv(file_path, row):
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(row)

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
    Output('defender-type', 'data', allow_duplicate=True),
    Output('steals-blocks', 'data', allow_duplicate=True),
    Output('clear-components-flag', 'data', allow_duplicate=True),
    
    Input("team-one-record-shot-button", "n_clicks"),
    Input("team-two-record-shot-button", "n_clicks"),
    Input('game-id', 'data'),
    Input('team-ids', 'data'),
    Input('shot-type', 'data'),
    Input('shot-result', 'data'),
    Input('play-type', 'data'),
    Input('player', 'data'),
    Input('defender', 'data'),
    Input('shot-coordinates', 'data'),
    Input('shot-quality', 'data'),
    Input('free-throws', 'data'),
    Input('shot-zone', 'data'),
    Input('defender-type', 'data'),
    Input('steals-blocks', 'data'),
    
    prevent_initial_call=True,
)
def teamOne_RecordShot(team_one_n_clicks, team_two_n_clicks, game_id, team_ids, shot_type, shot_result, play_type, player, defender, shot_coordinates, shot_quality, free_throws, shot_zone, defender_type, steals_blocks):

    cleared = [{}, {}]
    none_cleared = [{'shooter': None}, {'shooter': None}]
    poa_reset = [{'shooter': 'POA'}, {'shooter': 'POA'}]
    file_path = 'game_data/events.csv'
    
    game_id = game_id.copy()
    shot_type = shot_type.copy()
    play_type = play_type.copy()
    player = player.copy()
    defender = defender.copy()
    shot_coordinates = shot_coordinates.copy()
    shot_quality = shot_quality.copy()
    free_throws = free_throws.copy()
    shot_zone = shot_zone.copy()
    defender_type = defender_type.copy()
    steals_blocks = steals_blocks.copy()

    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Team One
    if triggered_input_id == "team-one-record-shot-button" and team_one_n_clicks is not None:
        
        # Create event list with 12 empty slots and set game id
        event_list = []
        event_list += [None] * 13
        event_list[0] = game_id[0]['id']
        home_team_id = team_ids[0]['home']
        event_list[12] = f'"{home_team_id}"'
        
        # Handle a Passing Turnover
        if shot_result[0]['shooter'] == 99:
            
            event_list[3] = 99
            event_list[10] = player[0]['creator']
            event_list[11] = play_type[0]['creator']
            
            # Add shot coordinates
            if ('x' and 'y') in shot_coordinates[0].keys():
                event_list[4] = shot_coordinates[0]['x']
                event_list[5] = shot_coordinates[0]['y']
            
            # Add defender and defense type ids
            if 'shooter' in defender[0].keys():
                event_list[6] = defender[0]['shooter']
                event_list[7] = defender_type[0]['shooter']
            
            # Add shot zone id
            if 'shooter' in shot_zone[0].keys():
                event_list[8] = shot_zone[0]['shooter']
            
            append_to_csv(file_path, event_list)
        
            return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, poa_reset, none_cleared, True
        
        
        
        # Add shooter id if result isnt passing turnover
        if shot_result != 99:
            event_list[3] = shot_result[0]['shooter']
        
        # add the shooter id
        if 'shooter' in player[0].keys():
            player_id = player[0]['shooter']
            event_list[1] = player_id
            
        # Add the shooting play type id
        if 'shooter' in play_type[0].keys():
            play_type_id = play_type[0]['shooter']
            event_list[2] = play_type_id
            
        # Add the creator id
        if 'creator' in player[0].keys():
            creator_id = player[0]['creator']
            event_list[10] = creator_id
            
        # Add the creator play type id
        if 'creator' in play_type[0].keys():
            creator_play_type_id = play_type[0]['creator']
            event_list[11] = creator_play_type_id
        
        # Add shot coordinates
        if ('x' and 'y') in shot_coordinates[0].keys():
            event_list[4] = shot_coordinates[0]['x']
            event_list[5] = shot_coordinates[0]['y']
            
        # Add defender and defense type ids
        if 'shooter' in defender[0].keys():
            event_list[6] = defender[0]['shooter']
            event_list[7] = defender_type[0]['shooter']
            
        # Add shot zone id
        if 'shooter' in shot_zone[0].keys():
            event_list[8] = shot_zone[0]['shooter']
        
        # Add shot quality ids
        if 'shooter' in shot_quality[0].keys():
            event_list[9] = shot_quality[0]['shooter']    
        
        append_to_csv(file_path, event_list)
        
        return 'Shot Recorded', None, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, poa_reset, none_cleared, True
    
    # Team Two
    if triggered_input_id == "team-two-record-shot-button" and team_two_n_clicks is not None:
        
        # Create event list with 12 empty slots and set game id
        event_list = []
        event_list += [None] * 13
        event_list[0] = game_id[0]['id']
        away_team_id = team_ids[0]['away']
        event_list[12] = f'"{away_team_id}"'
        
        # Handle a Passing Turnover
        if shot_result[1]['shooter'] == 99:
            
            event_list[3] = 99
            event_list[10] = player[1]['creator']
            event_list[11] = play_type[1]['creator']
            
            # Add shot coordinates
            if ('x' and 'y') in shot_coordinates[1].keys():
                event_list[4] = shot_coordinates[1]['x']
                event_list[5] = shot_coordinates[1]['y']
            
            # Add defender and defense type ids
            if 'shooter' in defender[1].keys():
                event_list[6] = defender[1]['shooter']
                event_list[7] = defender_type[1]['shooter']
            
            # Add shot zone id
            if 'shooter' in shot_zone[1].keys():
                event_list[8] = shot_zone[1]['shooter']
            
            append_to_csv(file_path, event_list)
        
            return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, poa_reset, none_cleared, True
        
        
        
        # Add shooter id if result isnt passing turnover
        if shot_result != 99:
            event_list[3] = shot_result[1]['shooter']
        
        # add the shooter id
        if 'shooter' in player[1].keys():
            player_id = player[1]['shooter']
            event_list[1] = player_id
            
        # Add the shooting play type id
        if 'shooter' in play_type[1].keys():
            play_type_id = play_type[1]['shooter']
            event_list[2] = play_type_id
            
        # Add the creator id
        if 'creator' in player[1].keys():
            creator_id = player[1]['creator']
            event_list[10] = creator_id
            
        # Add the creator play type id
        if 'creator' in play_type[1].keys():
            creator_play_type_id = play_type[1]['creator']
            event_list[11] = creator_play_type_id
        
        # Add shot coordinates
        if ('x' and 'y') in shot_coordinates[1].keys():
            event_list[4] = shot_coordinates[1]['x']
            event_list[5] = shot_coordinates[1]['y']
            
        # Add defender and defense type ids
        if 'shooter' in defender[1].keys():
            event_list[6] = defender[1]['shooter']
            event_list[7] = defender_type[1]['shooter']
            
        # Add shot zone id
        if 'shooter' in shot_zone[1].keys():
            event_list[8] = shot_zone[1]['shooter']
        
        # Add shot quality ids
        if 'shooter' in shot_quality[1].keys():
            event_list[9] = shot_quality[1]['shooter']    
            
        append_to_csv(file_path, event_list)

        return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, poa_reset, none_cleared, True
     
    return None, '', no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, False