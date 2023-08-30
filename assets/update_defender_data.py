import pandas as pd
import os
import json

mapping = {'PNR Ball Handler': 'PNR BH', 'PNR Screener': 'PNR SC', 'DHO Ball Handler': 'DHO BH', 'DHO Screener': 'DHO SC',
           'Isolation': 'ISO', 'Transition': 'TRAN', 'Attacking Closeouts': 'ACO', 'Catch & Shoot': 'C/S', 'Off-Ball Screens': 'OBS',
           'Cutting': 'CUT', 'Offensive Rebounds': 'OREB'}

empty_defender = pd.read_csv('assets/empty_defender.csv', index_col='Shot Type')

def UpdateDefenderDF(shot, team):
   
    player_data = empty_defender.copy()

    # Handle shot makes
    if shot['result'] == 1:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['shoot2FGA'], [shot['play_type']]] += 1
            player_data.loc[['shoot2FGM'], [shot['play_type']]] += 1
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['shoot3FGA'], [shot['play_type']]] += 1
            player_data.loc[['shoot3FGM'], [shot['play_type']]] += 1

    # Handle shot misses
    if shot['result'] == 0:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['shoot2FGA'], [shot['play_type']]] += 1
            player_data.loc[['shoot2FGM'], [shot['play_type']]] += 0
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['shoot3FGA'], [shot['play_type']]] += 1
            player_data.loc[['shoot3FGM'], [shot['play_type']]] += 0

    # Handle Free Throws
    if shot['result'] == 11:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['shoot2FTA'], [shot['play_type']]] += 2
            player_data.loc[['shoot2FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['shoot3FTA'], [shot['play_type']]] += 3
            player_data.loc[['shoot3FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
            
    # Handle And-1
    if shot['result'] == 30:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['shoot2FGA'], [shot['play_type']]] += 1
            player_data.loc[['shoot2FGM'], [shot['play_type']]] += 1
            player_data.loc[['shoot2FTA'], [shot['play_type']]] += 1
            player_data.loc[['shoot2FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['shoot3FGA'], [shot['play_type']]] += 1
            player_data.loc[['shoot3FGM'], [shot['play_type']]] += 1
            player_data.loc[['shoot3FTA'], [shot['play_type']]] += 1
            player_data.loc[['shoot3FTM'], [
                shot['play_type']]] += int(shot['free_throws'])

    # Handle Turnovers
    if shot['result'] == 20:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[['shoot2TO'], [shot['play_type']]] += 1
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[['shoot3TO'], [shot['play_type']]] += 1
               
    # Handle Shot Quality
    if shot['shot_type'] == '2pt FG' and (shot['result'] != 11 or 30):
        
        player_data.loc[['shootSQ2'], [shot['play_type']]] += shot['shot_quality']  
        
    if shot['shot_type'] == '3pt FG' and (shot['result'] != 11 or 30):
        player_data.loc[['shootSQ3'], [shot['play_type']]] += shot['shot_quality']      

    # Declare output paths for Defender and Team overall and shot zone data
    defender_output_path = f'game_data/{team}/Defense/{shot["defender"]}'
    defender_shot_zone_output_path = f'game_data/{team}/Defense/{shot["defender"]}/{shot["defender"]}_{shot["shot_zone"]}.json'
    team_output_path = f'game_data/{team}/Defense/Team'
    team_shot_zone_output_path = f'game_data/{team}/Defense/Team/Team_{shot["shot_zone"]}.json'
    
    # Check if Defender output path exists and make a new directory if it doesn't
    if not os.path.exists(defender_output_path):
        os.makedirs(defender_output_path)
    # Check if Team output path exists and make a new directory if it doesn't    
    if not os.path.exists(team_output_path):
        os.makedirs(team_output_path)
    
    # Try to load Defender shot zone data, create empty JSON file of not
    try:
        with open(defender_shot_zone_output_path, 'r', encoding='utf-8') as f:
            defender_shot_zone_file = json.load(f)
            defender_shot_zone_file['data'] = pd.DataFrame(defender_shot_zone_file['data']).transpose()
     
    except(FileNotFoundError):
        defender_shot_zone_file = {'data' :empty_defender, 'locations': []}
    # Try to load Team shot zone data, create empty JSON file of not
    try:
        with open(team_shot_zone_output_path, 'r', encoding='utf-8') as f:
            team_shot_zone_file = json.load(f)
            team_shot_zone_file['data'] = pd.DataFrame(team_shot_zone_file['data']).transpose()
     
    except(FileNotFoundError):
        team_shot_zone_file = {'data' :empty_defender, 'locations': []}
        
    # Unpack Shot coordinates
    x = shot['shot_coordinates']['x']
    y =shot['shot_coordinates']['y']
    
    # Add data to the Shot Zone Data and change dataframe to dict
    defender_shot_zone_file['data'] = defender_shot_zone_file['data'].add(player_data)
    defender_shot_zone_file['data'] = defender_shot_zone_file['data'].to_dict(orient='index')
    defender_shot_zone_file['locations'].append(((x, y), shot['result']))
    team_shot_zone_file['data'] = team_shot_zone_file['data'].add(player_data)
    team_shot_zone_file['data'] = team_shot_zone_file['data'].to_dict(orient='index')
    team_shot_zone_file['locations'].append(((x, y), shot['result']))
    
    # Write updated Player shot zone data to shot zone output path
    with open(defender_shot_zone_output_path, 'w', encoding='utf-8') as f:
        json.dump(defender_shot_zone_file, f, ensure_ascii=False, indent=4)
    # Write updated Team shot zone data to shot zone output path
    with open(team_shot_zone_output_path, 'w', encoding='utf-8') as f:
        json.dump(team_shot_zone_file, f, ensure_ascii=False, indent=4)
        
    # Try to load overall Player data file, create empty JSON file if not
    try:
        with open(f'{defender_output_path}/{shot["defender"]}_Defense.json', 'r', encoding='utf-8') as f:
            defender_overall_file = json.load(f)
            defender_overall_file['data'] = pd.DataFrame(defender_overall_file['data']).transpose()
    except(FileNotFoundError):
        defender_overall_file = {'data' :empty_defender, 'locations': []}
    # Try to load overall Team data file, create empty JSON file if not
    try:
        with open(f'{team_output_path}/Team_Defense.json', 'r', encoding='utf-8') as f:
            team_overall_file = json.load(f)
            team_overall_file['data'] = pd.DataFrame(team_overall_file['data']).transpose()
    except(FileNotFoundError):
        team_overall_file = {'data' :empty_defender, 'locations': []}
        
    # Add data to overall data and change DF back to dict
    defender_overall_file['data'] = defender_overall_file['data'].add(player_data)
    defender_overall_file['data'] = defender_overall_file['data'].to_dict(orient='index')
    defender_overall_file['locations'].append(((x, y), shot['result']))
    team_overall_file['data'] = team_overall_file['data'].add(player_data)
    team_overall_file['data'] = team_overall_file['data'].to_dict(orient='index')
    team_overall_file['locations'].append(((x, y), shot['result']))
    
    # Write updated overall Player file to output path
    with open(f'{defender_output_path}/{shot["defender"]}_Defense.json', 'w', encoding='utf-8') as f:
        json.dump(defender_overall_file, f, ensure_ascii=False, indent=4)
    # Write updated overall Team file to output path
    with open(f'{team_output_path}/Team_Defense.json', 'w', encoding='utf-8') as f:
        json.dump(team_overall_file, f, ensure_ascii=False, indent=4)

    return defender_overall_file