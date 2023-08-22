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
        
    # Update Shot Zone Data
    output_path = f'game_data/{team}/Offense/{shot["player"]}'
    shot_zone_output = f'game_data/{team}/Offense/{shot["player"]}/{shot["player"]}_{shot["shot_zone"]}.json'
 
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    try:
        with open(shot_zone_output, 'r', encoding='utf-8') as f:
            shot_zone_file = json.load(f)
            shot_zone_file['data'] = pd.DataFrame(shot_zone_file['data']).transpose()
     
    except(FileNotFoundError):
        shot_zone_file = {'data' :empty, 'locations': []}
        
    # Unpack Shot coordinates
    x = shot['shot_coordinates']['x']
    y =shot['shot_coordinates']['y']
    
    # Add data to the Shot Zone Data and change dataframe to dict
    shot_zone_file['data'] = shot_zone_file['data'].add(player_data)
    shot_zone_file['data'] = shot_zone_file['data'].to_dict(orient='index')
    shot_zone_file['locations'].append(tuple((x, y)))

    with open(shot_zone_output, 'w', encoding='utf-8') as f:
        json.dump(shot_zone_file, f, ensure_ascii=False, indent=4)

    # Define output path and write updated data to JSON
    try:
        with open(f'{output_path}/{shot["player"]}_Overall.json', 'r', encoding='utf-8') as f:
            overall_file = json.load(f)
            overall_file['data'] = pd.DataFrame(overall_file['data']).transpose()
    
    except(FileNotFoundError):
        overall_file = {'data' :empty, 'locations': []}
    
    overall_file['data'] = overall_file['data'].add(player_data)
    overall_file['data'] = overall_file['data'].to_dict(orient='index')
    overall_file['locations'].append(tuple((x, y)))
    
    with open(f'{output_path}/{shot["player"]}_Overall.json', 'w', encoding='utf-8') as f:
        json.dump(overall_file, f, ensure_ascii=False, indent=4)

    return overall_file

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
        
    # Update Shot Zone Data
    output_path = f'game_data/{team}/Offense/{shot["player"]}'
    shot_zone_output = f'game_data/{team}/Offense/{shot["player"]}/{shot["player"]}_{shot["shot_zone"]}.json'
    
    # If player folder does not exist, make one
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Try to load shot zone data for game, use empty if none exists
    try:
        with open(shot_zone_output, 'r', encoding='utf-8') as f:
            shot_zone_file['data'] = json.load(f)
            shot_zone_file['data'] = pd.DataFrame(shot_zone_file['data']).transpose()
      
    except(FileNotFoundError):
        shot_zone_file = {'data' :empty, 'locations': []}
        
    # Unpack Shot coordinates
    x = shot['shot_coordinates']['x']
    y =shot['shot_coordinates']['y']
 
    # Add data to the overall and change dataframe to dict
    shot_zone_file['data'] = shot_zone_file['data'].add(player_data)
    shot_zone_file['data'] = shot_zone_file['data'].to_dict(orient='index')
    shot_zone_file['locations'].append(tuple((x, y)))

    with open(shot_zone_output, 'w', encoding='utf-8') as f:
        json.dump(shot_zone_file, f, ensure_ascii=False, indent=4)
  
     # Define output path and write updated data to JSON
    try:
        with open(f'{output_path}/{shot["player"]}_Overall.json', 'r', encoding='utf-8') as f:
            overall_file = json.load(f)
            overall_file['data'] = pd.DataFrame(overall_file['data']).transpose()
    
    except(FileNotFoundError):
        overall_file = {'data' :empty, 'locations': []}
    
    overall_file['data'] = overall_file['data'].add(player_data)
    overall_file['data'] = overall_file['data'].to_dict(orient='index')
    overall_file['locations'].append(tuple((x, y)))
    
    with open(f'{output_path}/{shot["player"]}_Overall.json', 'w', encoding='utf-8') as f:
        json.dump(overall_file, f, ensure_ascii=False, indent=4)

    return overall_file



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

    # Update Shot Zone Data
    output_path = f'game_data/{team}/Defense/{shot["defender"]}'
    shot_zone_output = f'game_data/{team}/Defense/{shot["defender"]}/{shot["defender"]}_Defense_{shot["shot_zone"]}.json'
    
    # If player folder does not exist, make one
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Try to load shot zone data for game, use empty if none exists
    try:
        with open(shot_zone_output, 'r', encoding='utf-8') as f:
            shot_zone_file['data'] = json.load(f)
            shot_zone_file['data'] = pd.DataFrame(shot_zone_file['data']).transpose()
      
    except(FileNotFoundError):
        shot_zone_file = {'data' :empty_defender, 'locations': []}
        
    # Unpack Shot coordinates
    x = shot['shot_coordinates']['x']
    y =shot['shot_coordinates']['y']
 
    # Add data to the overall and change dataframe to dict
    shot_zone_file['data'] = shot_zone_file['data'].add(player_data)
    shot_zone_file['data'] = shot_zone_file['data'].to_dict(orient='index')
    shot_zone_file['locations'].append(tuple((x, y)))

    with open(shot_zone_output, 'w', encoding='utf-8') as f:
        json.dump(shot_zone_file, f, ensure_ascii=False, indent=4)
  
     # Define output path and write updated data to JSON
    try:
        with open(f'{output_path}/{shot["defender"]}_Defense.json', 'r', encoding='utf-8') as f:
            overall_file = json.load(f)
            overall_file['data'] = pd.DataFrame(overall_file['data']).transpose()
    
    except(FileNotFoundError):
        overall_file = {'data' :empty_defender, 'locations': []}
    
    overall_file['data'] = overall_file['data'].add(player_data)
    overall_file['data'] = overall_file['data'].to_dict(orient='index')
    overall_file['locations'].append(tuple((x, y)))
    
    with open(f'{output_path}/{shot["defender"]}_Defense.json', 'w', encoding='utf-8') as f:
        json.dump(overall_file, f, ensure_ascii=False, indent=4)

    return overall_file

## player_df.to_dict(orient='records')
