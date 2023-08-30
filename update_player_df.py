import pandas as pd
import os
import json

mapping = {'PNR Ball Handler': 'PNR BH', 'PNR Screener': 'PNR SC', 'DHO Ball Handler': 'DHO BH', 'DHO Screener': 'DHO SC',
           'Isolation': 'ISO', 'Transition': 'TRAN', 'Attacking Closeouts': 'ACO', 'Catch & Shoot': 'C/S', 'Off-Ball Screens': 'OBS',
           'Cutting': 'CUT', 'Offensive Rebounds': 'OREB'}

empty = pd.read_csv('assets/empty.csv', index_col='Shot Type')
empty_defender = pd.read_csv('assets/empty_defender.csv', index_col='Shot Type')

def UpdateShooterDF(shot, team):
    
    player_data = empty.copy()

    shot['play_type'] = mapping[shot['play_type']]
    
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
    if shot['shot_type'] == '2pt FG':
        player_data.loc[['shootSQ2'], [shot['play_type']]] += shot['shot_quality']  
        
    if shot['shot_type'] == '3pt FG':
        player_data.loc[['shootSQ3'], [shot['play_type']]] += shot['shot_quality']  
        
    # Declare output paths for Player and Team overall and shot zone data
    player_output_path = f'game_data/{team}/Offense/{shot["player"]}'
    player_shot_zone_output_path = f'game_data/{team}/Offense/{shot["player"]}/{shot["player"]}_{shot["shot_zone"]}.json'
    team_output_path = f'game_data/{team}/Offense/Team'
    team_shot_zone_output_path = f'game_data/{team}/Offense/Team/Team_{shot["shot_zone"]}.json'
    
    # Check if Player output path exists and make a new directory if it doesn't
    if not os.path.exists(player_output_path):
        os.makedirs(player_output_path)
    # Check if Team output path exists and make a new directory if it doesn't    
    if not os.path.exists(team_output_path):
        os.makedirs(team_output_path)
    
    # Try to load Player shot zone data, create empty JSON file of not
    try:
        with open(player_shot_zone_output_path, 'r', encoding='utf-8') as f:
            player_shot_zone_file = json.load(f)
            player_shot_zone_file['data'] = pd.DataFrame(player_shot_zone_file['data']).transpose()
     
    except(FileNotFoundError):
        player_shot_zone_file = {'data' :empty, 'locations': []}
        
    # Try to load Team shot zone data, create empty JSON file of not
    try:
        with open(team_shot_zone_output_path, 'r', encoding='utf-8') as f:
            team_shot_zone_file = json.load(f)
            team_shot_zone_file['data'] = pd.DataFrame(team_shot_zone_file['data']).transpose()
     
    except(FileNotFoundError):
        team_shot_zone_file = {'data' :empty, 'locations': []}
        
    # Unpack Shot coordinates
    x = shot['shot_coordinates']['x']
    y =shot['shot_coordinates']['y']
    
    # Add data to the Shot Zone Data and change dataframe to dict
    player_shot_zone_file['data'] = player_shot_zone_file['data'].add(player_data)
    player_shot_zone_file['data'] = player_shot_zone_file['data'].to_dict(orient='index')
    player_shot_zone_file['locations'].append(tuple((x, y)))
    team_shot_zone_file['data'] = team_shot_zone_file['data'].add(player_data)
    team_shot_zone_file['data'] = team_shot_zone_file['data'].to_dict(orient='index')
    team_shot_zone_file['locations'].append(tuple((x, y)))
    
    # Write updated Player shot zone data to shot zone output path
    with open(player_shot_zone_output_path, 'w', encoding='utf-8') as f:
        json.dump(player_shot_zone_file, f, ensure_ascii=False, indent=4)
    # Write updated Team shot zone data to shot zone output path
    with open(team_shot_zone_output_path, 'w', encoding='utf-8') as f:
        json.dump(team_shot_zone_file, f, ensure_ascii=False, indent=4)
        
    # Try to load overall Player data file, create empty JSON file if not
    try:
        with open(f'{player_output_path}/{shot["player"]}_Overall.json', 'r', encoding='utf-8') as f:
            player_overall_file = json.load(f)
            player_overall_file['data'] = pd.DataFrame(player_overall_file['data']).transpose()
    except(FileNotFoundError):
        player_overall_file = {'data' :empty, 'locations': []}
    # Try to load overall Team data file, create empty JSON file if not
    try:
        with open(f'{team_output_path}/Team_Overall.json', 'r', encoding='utf-8') as f:
            team_overall_file = json.load(f)
            team_overall_file['data'] = pd.DataFrame(team_overall_file['data']).transpose()
    except(FileNotFoundError):
        team_overall_file = {'data' :empty, 'locations': []}
        
    # Add data to overall data and change DF back to dict
    player_overall_file['data'] = player_overall_file['data'].add(player_data)
    player_overall_file['data'] = player_overall_file['data'].to_dict(orient='index')
    player_overall_file['locations'].append(tuple((x, y)))
    team_overall_file['data'] = team_overall_file['data'].add(player_data)
    team_overall_file['data'] = team_overall_file['data'].to_dict(orient='index')
    team_overall_file['locations'].append(tuple((x, y)))
    
    # Write updated overall Player file to output path
    with open(f'{player_output_path}/{shot["player"]}_Overall.json', 'w', encoding='utf-8') as f:
        json.dump(player_overall_file, f, ensure_ascii=False, indent=4)
    # Write updated overall Team file to output path
    with open(f'{team_output_path}/Team_Overall.json', 'w', encoding='utf-8') as f:
        json.dump(team_overall_file, f, ensure_ascii=False, indent=4)

    return player_overall_file

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
    if shot['shot_type'] == '2pt FG':
        player_data.loc[['passSQ2'], [shot['play_type']]] += shot['shot_quality']  
        
    if shot['shot_type'] == '3pt FG':
        player_data.loc[['passSQ3'], [shot['play_type']]] += shot['shot_quality']   
        
    # Declare output paths for Player and Team overall and shot zone data
    player_output_path = f'game_data/{team}/Offense/{shot["player"]}'
    player_shot_zone_output_path = f'game_data/{team}/Offense/{shot["player"]}/{shot["player"]}_{shot["shot_zone"]}.json'
    team_output_path = f'game_data/{team}/Offense/Team'
    team_shot_zone_output_path = f'game_data/{team}/Offense/Team/Team_{shot["shot_zone"]}.json'
    
    # Check if Player output path exists and make a new directory if it doesn't
    if not os.path.exists(player_output_path):
        os.makedirs(player_output_path)
    # Check if Team output path exists and make a new directory if it doesn't    
    if not os.path.exists(team_output_path):
        os.makedirs(team_output_path)
    
    # Try to load Player shot zone data, create empty JSON file of not
    try:
        with open(player_shot_zone_output_path, 'r', encoding='utf-8') as f:
            player_shot_zone_file = json.load(f)
            player_shot_zone_file['data'] = pd.DataFrame(player_shot_zone_file['data']).transpose()
     
    except(FileNotFoundError):
        player_shot_zone_file = {'data' :empty, 'locations': []}
        
    # Try to load Team shot zone data, create empty JSON file of not
    try:
        with open(team_shot_zone_output_path, 'r', encoding='utf-8') as f:
            team_shot_zone_file = json.load(f)
            team_shot_zone_file['data'] = pd.DataFrame(team_shot_zone_file['data']).transpose()
     
    except(FileNotFoundError):
        team_shot_zone_file = {'data' :empty, 'locations': []}
        
    # Unpack Shot coordinates
    x = shot['shot_coordinates']['x']
    y =shot['shot_coordinates']['y']
    
    # Add data to the Shot Zone Data and change dataframe to dict
    player_shot_zone_file['data'] = player_shot_zone_file['data'].add(player_data)
    player_shot_zone_file['data'] = player_shot_zone_file['data'].to_dict(orient='index')
    player_shot_zone_file['locations'].append(tuple((x, y)))
    team_shot_zone_file['data'] = team_shot_zone_file['data'].add(player_data)
    team_shot_zone_file['data'] = team_shot_zone_file['data'].to_dict(orient='index')
    team_shot_zone_file['locations'].append(tuple((x, y)))
    
    # Write updated Player shot zone data to shot zone output path
    with open(player_shot_zone_output_path, 'w', encoding='utf-8') as f:
        json.dump(player_shot_zone_file, f, ensure_ascii=False, indent=4)
    # Write updated Team shot zone data to shot zone output path
    with open(team_shot_zone_output_path, 'w', encoding='utf-8') as f:
        json.dump(team_shot_zone_file, f, ensure_ascii=False, indent=4)
        
    # Try to load overall Player data file, create empty JSON file if not
    try:
        with open(f'{player_output_path}/{shot["player"]}_Overall.json', 'r', encoding='utf-8') as f:
            player_overall_file = json.load(f)
            player_overall_file['data'] = pd.DataFrame(player_overall_file['data']).transpose()
    except(FileNotFoundError):
        player_overall_file = {'data' :empty, 'locations': []}
    # Try to load overall Team data file, create empty JSON file if not
    try:
        with open(f'{team_output_path}/Team_Overall.json', 'r', encoding='utf-8') as f:
            team_overall_file = json.load(f)
            team_overall_file['data'] = pd.DataFrame(team_overall_file['data']).transpose()
    except(FileNotFoundError):
        team_overall_file = {'data' :empty, 'locations': []}
        
    # Add data to overall data and change DF back to dict
    player_overall_file['data'] = player_overall_file['data'].add(player_data)
    player_overall_file['data'] = player_overall_file['data'].to_dict(orient='index')
    player_overall_file['locations'].append(tuple((x, y)))
    team_overall_file['data'] = team_overall_file['data'].add(player_data)
    team_overall_file['data'] = team_overall_file['data'].to_dict(orient='index')
    team_overall_file['locations'].append(tuple((x, y)))
    
    # Write updated overall Player file to output path
    with open(f'{player_output_path}/{shot["player"]}_Overall.json', 'w', encoding='utf-8') as f:
        json.dump(player_overall_file, f, ensure_ascii=False, indent=4)
    # Write updated overall Team file to output path
    with open(f'{team_output_path}/Team_Overall.json', 'w', encoding='utf-8') as f:
        json.dump(team_overall_file, f, ensure_ascii=False, indent=4)

    return player_overall_file

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
    defender_shot_zone_file['locations'].append(tuple((x, y)))
    team_shot_zone_file['data'] = team_shot_zone_file['data'].add(player_data)
    team_shot_zone_file['data'] = team_shot_zone_file['data'].to_dict(orient='index')
    team_shot_zone_file['locations'].append(tuple((x, y)))
    
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
    defender_overall_file['locations'].append(tuple((x, y)))
    team_overall_file['data'] = team_overall_file['data'].add(player_data)
    team_overall_file['data'] = team_overall_file['data'].to_dict(orient='index')
    team_overall_file['locations'].append(tuple((x, y)))
    
    # Write updated overall Player file to output path
    with open(f'{defender_output_path}/{shot["defender"]}_Defense.json', 'w', encoding='utf-8') as f:
        json.dump(defender_overall_file, f, ensure_ascii=False, indent=4)
    # Write updated overall Team file to output path
    with open(f'{team_output_path}/Team_Defense.json', 'w', encoding='utf-8') as f:
        json.dump(team_overall_file, f, ensure_ascii=False, indent=4)

    return defender_overall_file