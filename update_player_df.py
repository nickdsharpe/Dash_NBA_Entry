import pandas as pd
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


    # Define ouptut path and write updated data to CSV
    output_path = f'game_data/{team}/Offense/{shot["player"]}'
    
    try:
        file = pd.read_csv(output_path, index_col='Shot Type')

    except(FileNotFoundError):
        file = empty
        
    file = file.add(player_data)
    file.to_csv(output_path)
    
    ### Code to write dataframes as loadable JSON ###
    '''
    json_file = file.to_dict(orient='index')
    with open(f'game_data/{team}/Offense/{shot["player"]}.json', 'w', encoding='utf-8') as f:
        json.dump(json_file, f, ensure_ascii=False, indent=4)
        '''

    return file

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
        
        

    output_path = f'game_data/{team}/Offense/{shot["player"]}'
  
    try:
        file = pd.read_csv(output_path, index_col='Shot Type')
  
    except(FileNotFoundError):
        file = empty
    
    file = file.add(player_data)
    file.to_csv(output_path)

    return file



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

    # Define ouptut path and write updated data to CSV
    output_path = f'game_data/{team}/Defense/{shot["defender"]}'
 
    try:
        file = pd.read_csv(output_path, index_col='Shot Type')

    except(FileNotFoundError):
        file = empty_defender
    
    file = file.add(player_data)
    file.to_csv(output_path)

    return file

## player_df.to_dict(orient='records')
