import pandas as pd
import json

mapping = {'PNR Ball Handler': 'PNR BH', 'PNR Screener': 'PNR SC', 'DHO Ball Handler': 'DHO BH', 'DHO Screener': 'DHO SC',
           'Isolation': 'ISO', 'Transition': 'TRAN', 'Attacking Closeouts': 'ACO', 'Catch & Shoot': 'C/S', 'Off-Ball Screens': 'OBS',
           'Cutting': 'CUT', 'Offensive Rebounds': 'OREB'}

empty_defender = pd.read_csv('assets/empty_defender.csv', index_col='Shot Type')

def UpdateDefenderDF(shot, team, defense):

    player_data = empty_defender.copy()
    
    try:
        shot['play_type'] = mapping[shot['play_type']]
    except:
        pass
    
    # Handle shot makes
    if shot['result'] == 1:
        
        if shot['shot_type'] == '2pt FG':
            player_data.loc[[f'{defense}2FGA'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}2FGM'], [shot['play_type']]] += 1
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[[f'{defense}3FGA'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}3FGM'], [shot['play_type']]] += 1
    
    # Handle shot misses
    if shot['result'] == 0:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[[f'{defense}2FGA'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}2FGM'], [shot['play_type']]] += 0
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[[f'{defense}3FGA'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}3FGM'], [shot['play_type']]] += 0
    
    # Handle Free Throws
    if shot['result'] == 11:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[[f'{defense}2FTA'], [shot['play_type']]] += 2
            player_data.loc[[f'{defense}2FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[[f'{defense}3FTA'], [shot['play_type']]] += 3
            player_data.loc[[f'{defense}3FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
          
    # Handle And-1
    if shot['result'] == 30:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[[f'{defense}2FGA'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}2FGM'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}2FTA'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}2FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[[f'{defense}3FGA'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}3FGM'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}3FTA'], [shot['play_type']]] += 1
            player_data.loc[[f'{defense}3FTM'], [
                shot['play_type']]] += int(shot['free_throws'])
    
    # Handle Turnovers
    if shot['result'] == 20:
        if shot['shot_type'] == '2pt FG':
            player_data.loc[[f'{defense}2TO'], [shot['play_type']]] += 1
        elif shot['shot_type'] == '3pt FG':
            player_data.loc[[f'{defense}3TO'], [shot['play_type']]] += 1
      
    # Handle Steals and Blocks
    if shot['stl/blk'] is not None:
        if shot['shot_type'] == '2pt FG':
            if shot['stl/blk'] == 'STL':
                player_data.loc[[f'{defense}2STL'], [shot['play_type']]] +=1
            if shot['stl/blk'] == 'BLK':
                player_data.loc[[f'{defense}2BLK'], [shot['play_type']]] +=1
        if shot['shot_type'] == '3pt FG':
            if shot['stl/blk'] == 'STL':
                player_data.loc[[f'{defense}3STL'], [shot['play_type']]] +=1
            if shot['stl/blk'] == 'BLK':
                player_data.loc[[f'{defense}3BLK'], [shot['play_type']]] +=1
              
    # Handle Shot Quality
    if (shot['shot_type'] == '2pt FG') and (shot['result'] < 11):
        player_data.loc[[f'{defense}SQ2'], [shot['play_type']]] += shot['shot_quality']  
        
    if (shot['shot_type'] == '3pt FG') and (shot['result'] < 11):
        player_data.loc[[f'{defense}SQ3'], [shot['play_type']]] += shot['shot_quality'] 
        
        
             
    
    # Declare output paths for defender and Team overall
    defender_output_path = f'game_data/{team}/Defense/{shot["defender"]}.json'
    team_output_path = f'game_data/{team}/Defense/Team.json'
    
    # Try to load OVERALL defender data, create empty JSON file of not
    try:
        with open(defender_output_path, 'r', encoding='utf-8') as f:
            defender_file = json.load(f)
            defender_file['ovr_data']['data'] = pd.DataFrame(defender_file['ovr_data']['data']).transpose()
    except:
        defender_file = {'ovr_data': {'data': empty_defender, 'shooting_locations': []}}
 
    # Try to load OVERALL Team data, create empty JSON file of not
    try:
        with open(team_output_path, 'r', encoding='utf-8') as f:
            team_file = json.load(f)
            team_file['ovr_data']['data'] = pd.DataFrame(team_file['ovr_data']['data']).transpose()
    except:
        team_file = {'ovr_data': {'data': empty_defender, 'shooting_locations': []}}
   
    # Unpack Shot coordinates
    x = shot['shot_coordinates']['x']
    y =shot['shot_coordinates']['y']
    
    # Add data to the OVERALL Data and change dataframe to dict
    defender_file['ovr_data']['data'] = defender_file['ovr_data']['data'].add(player_data)
    defender_file['ovr_data']['data'] = defender_file['ovr_data']['data'].to_dict(orient='index')
    defender_file['ovr_data']['shooting_locations'].append(((x, y), shot['result']))
    team_file['ovr_data']['data'] = team_file['ovr_data']['data'].add(player_data)
    team_file['ovr_data']['data'] = team_file['ovr_data']['data'].to_dict(orient='index')
    team_file['ovr_data']['shooting_locations'].append(((x, y), shot['result']))
    
    # Write updated Defender OVERALL data to output path
    with open(defender_output_path, 'w', encoding='utf-8') as f:
        json.dump(defender_file, f, ensure_ascii=False, indent=4)
    # Write updated Team OVERALL data to output path
    with open(team_output_path, 'w', encoding='utf-8') as f:
        json.dump(team_file, f, ensure_ascii=False, indent=4)

    # Try to load SHOT ZONE Defender data file, create empty JSON file if not
    try:
        with open(defender_output_path, 'r', encoding='utf-8') as f:
            defender_file = json.load(f)
            defender_file[f'{shot["shot_zone"]}']['data'] = pd.DataFrame(defender_file[f'{shot["shot_zone"]}']['data']).transpose()
    except:
      
        defender_file[f'{shot["shot_zone"]}'] = {'data': empty_defender, 'shooting_locations': []}
        
    # Try to load SHOT ZONE Team data file, create empty JSON file if not
    try:
        with open(team_output_path, 'r', encoding='utf-8') as f:
            team_file = json.load(f)
            team_file[f'{shot["shot_zone"]}']['data'] = pd.DataFrame(team_file[f'{shot["shot_zone"]}']['data']).transpose()
    except:
        team_file[f'{shot["shot_zone"]}'] = {'data': empty_defender, 'shooting_locations': []}
  
    # Add data to SHOT ZONE data and change DF back to dict
    defender_file[f'{shot["shot_zone"]}']['data'] = defender_file[f'{shot["shot_zone"]}']['data'].add(player_data)
    defender_file[f'{shot["shot_zone"]}']['data'] = defender_file[f'{shot["shot_zone"]}']['data'].to_dict(orient='index')
    defender_file[f'{shot["shot_zone"]}']['shooting_locations'].append(((x, y), shot['result']))
    team_file[f'{shot["shot_zone"]}']['data'] = team_file[f'{shot["shot_zone"]}']['data'].add(player_data)
    team_file[f'{shot["shot_zone"]}']['data'] = team_file[f'{shot["shot_zone"]}']['data'].to_dict(orient='index')
    team_file[f'{shot["shot_zone"]}']['shooting_locations'].append(((x, y), shot['result']))
    
    # Write updated overall Player file to output path
    with open(defender_output_path, 'w', encoding='utf-8') as f:
        json.dump(defender_file, f, ensure_ascii=False, indent=4)
    # Write updated overall Team file to output path
    with open(team_output_path, 'w', encoding='utf-8') as f:
        json.dump(team_file, f, ensure_ascii=False, indent=4)

    return defender_file