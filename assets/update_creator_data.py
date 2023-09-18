import pandas as pd
import os
import json

mapping = {'PNR Ball Handler': 'PNR BH', 'PNR Screener': 'PNR SC', 'DHO Ball Handler': 'DHO BH', 'DHO Screener': 'DHO SC',
           'Isolation': 'ISO', 'Transition': 'TRAN', 'Attacking Closeouts': 'ACO', 'Catch & Shoot': 'C/S', 'Off-Ball Screens': 'OBS',
           'Cutting': 'CUT', 'Offensive Rebounds': 'OREB'}

empty = pd.read_csv('assets/empty.csv', index_col='Shot Type')

def UpdateCreatorDF(shot, team):
    player_data = empty.copy()

    shot['play_type'] = mapping[shot['play_type']]

    # Handle shot makes
    if shot['result'] == 1:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['pass2FGA'], [shot['play_type']]] += 1
            player_data.loc[['pass2FGM'], [shot['play_type']]] += 1
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['pass3FGA'], [shot['play_type']]] += 1
            player_data.loc[['pass3FGM'], [shot['play_type']]] += 1

    # Handle shot misses
    if shot['result'] == 0:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['pass2FGA'], [shot['play_type']]] += 1
            player_data.loc[['pass2FGM'], [shot['play_type']]] += 0
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['pass3FGA'], [shot['play_type']]] += 1
            player_data.loc[['pass3FGM'], [shot['play_type']]] += 0

    # Handle Free Throws
    if shot['result'] == 11:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['pass2FTA'], [shot['play_type']]] += 2
            player_data.loc[['pass2FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['pass3FTA'], [shot['play_type']]] += 3
            player_data.loc[['pass3FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
            
    # Handle And-1
    if shot['result'] == 30:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['pass2FGA'], [shot['play_type']]] += 1
            player_data.loc[['pass2FGM'], [shot['play_type']]] += 1
            player_data.loc[['pass2FTA'], [shot['play_type']]] += 1
            player_data.loc[['pass2FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['pass3FGA'], [shot['play_type']]] += 1
            player_data.loc[['pass3FGM'], [shot['play_type']]] += 1
            player_data.loc[['pass3FTA'], [shot['play_type']]] += 1
            player_data.loc[['pass3FTM'], [
                shot['play_type']]] += int(shot['free_throws'])

    # Handle Turnovers
    if shot['result'] == 20:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['pass2TO'], [shot['play_type']]] += 1
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['pass3TO'], [shot['play_type']]] += 1
            
    # Handle Shot Quality
    if shot['shot_type'] == '2pt FG' and (shot['result'] != 11 or 30 or 20):
        player_data.loc[['passSQ2'], [shot['play_type']]] += shot['shot_quality']  
        
    if shot['shot_type'] == '3pt FG' and (shot['result'] != 11 or 30 or 20):
        player_data.loc[['passSQ3'], [shot['play_type']]] += shot['shot_quality']   
        
    # Declare output paths for Player and Team overall
    player_output_path = f'game_data/{team}/Offense/{shot["player"]}.json'
    team_output_path = f'game_data/{team}/Offense/Team.json'

    # Try to load OVERALL Player data, create empty JSON file of not
    try:
        with open(player_output_path, 'r', encoding='utf-8') as f:
            player_file = json.load(f)
            player_file['ovr_data']['data'] = pd.DataFrame(player_file['ovr_data']['data']).transpose()
    except:
        player_file = {'ovr_data': {'data': empty, 'shooting_locations': [], 'created_locations': []}}
        
     # Try to load OVERALL Team data, create empty JSON file of not
    try:
        with open(team_output_path, 'r', encoding='utf-8') as f:
            team_file = json.load(f)
            team_file['ovr_data']['data'] = pd.DataFrame(team_file['ovr_data']['data']).transpose()
    except:
        team_file = {'ovr_data': {'data': empty, 'shooting_locations': [], 'created_locations': []}}
        
    # Unpack Shot coordinates
    x = shot['shot_coordinates']['x']
    y =shot['shot_coordinates']['y']
    
   # Add data to the OVERALL Data and change dataframe to dict
    player_file['ovr_data']['data'] = player_file['ovr_data']['data'].add(player_data)
    player_file['ovr_data']['data'] = player_file['ovr_data']['data'].to_dict(orient='index')
    player_file['ovr_data']['created_locations'].append(((x, y), shot['result']))
    team_file['ovr_data']['data'] = team_file['ovr_data']['data'].add(player_data)
    team_file['ovr_data']['data'] = team_file['ovr_data']['data'].to_dict(orient='index')
    team_file['ovr_data']['created_locations'].append(((x, y), shot['result']))
  
    # Write updated Player OVERALL data to output path
    with open(player_output_path, 'w', encoding='utf-8') as f:
        json.dump(player_file, f, ensure_ascii=False, indent=4)
    # Write updated Team OVERALL data to output path
    with open(team_output_path, 'w', encoding='utf-8') as f:
        json.dump(team_file, f, ensure_ascii=False, indent=4)
        
    # Try to load SHOT ZONE Player data file, create empty JSON file if not
    try:
        with open(player_output_path, 'r', encoding='utf-8') as f:
            player_file = json.load(f)
            player_file[f'{shot["shot_zone"]}']['data'] = pd.DataFrame(player_file[f'{shot["shot_zone"]}']['data']).transpose()
    except:
        player_file[f'{shot["shot_zone"]}'] = {'data': empty, 'shooting_locations': [], 'created_locations': []}
    
    # Try to load SHOT ZONE Team data file, create empty JSON file if not
    try:
        with open(team_output_path, 'r', encoding='utf-8') as f:
            team_file = json.load(f)
            team_file[f'{shot["shot_zone"]}']['data'] = pd.DataFrame(team_file[f'{shot["shot_zone"]}']['data']).transpose()
    except:
        team_file[f'{shot["shot_zone"]}'] = {'data': empty, 'shooting_locations': [], 'created_locations': []}
   
   # Add data to SHOT ZONE data and change DF back to dict
    player_file[f'{shot["shot_zone"]}']['data'] = player_file[f'{shot["shot_zone"]}']['data'].add(player_data)
    player_file[f'{shot["shot_zone"]}']['data'] = player_file[f'{shot["shot_zone"]}']['data'].to_dict(orient='index')
    player_file[f'{shot["shot_zone"]}']['created_locations'].append(((x, y), shot['result']))
    team_file[f'{shot["shot_zone"]}']['data'] = team_file[f'{shot["shot_zone"]}']['data'].add(player_data)
    team_file[f'{shot["shot_zone"]}']['data'] = team_file[f'{shot["shot_zone"]}']['data'].to_dict(orient='index')
    team_file[f'{shot["shot_zone"]}']['created_locations'].append(((x, y), shot['result']))
   
    # Write updated SHOT ZONE data to output path
    with open(player_output_path, 'w', encoding='utf-8') as f:
        json.dump(player_file, f, ensure_ascii=False, indent=4)
    # Write updated SHOT ZONE data to output path
    with open(team_output_path, 'w', encoding='utf-8') as f:
        json.dump(team_file, f, ensure_ascii=False, indent=4)
        
    return player_file
