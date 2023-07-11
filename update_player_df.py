import pandas as pd
import json

mapping = {'PNR Ball Handler': 'PNR BH', 'PNR Screener': 'PNR SC', 'DHO Ball Handler': 'DHO BH', 'DHO Screener': 'DHO SC',
           'Isolation': 'ISO', 'Transition': 'TRAN', 'Attacking Closeouts': 'ACO', 'Catch & Shoot': 'C/S', 'Off-Ball Screens': 'OBS',
           'Cutting': 'Cut', 'Offensive Rebounds': 'OREB'}

players = ['Jokic', 'Murray', 'Gordon', 'MPJ', 'KCP', 'Braun']
empty = pd.read_csv('empty.csv', index_col='Shot Type')
team_data = {player: empty for player in players}

def UpdatePlayerDF(shot):
    player_df = team_data[shot['player']]
    shot['play_type'] = mapping[shot['play_type']]

    # Handle shot makes
    if shot['result'] == 1:
        if shot['shot_type'] == '2pt FG':
            player_df.loc[['shoot2FGA'], [shot['play_type']]] += 1
            player_df.loc[['shoot2FGM'], [shot['play_type']]] += 1
        elif shot['shot_type'] == '3pt FG':
            player_df.loc[['shoot3FGA'], [shot['play_type']]] += 1
            player_df.loc[['shoot3FGM'], [shot['play_type']]] += 1

    # Handle shot misses
    if shot['result'] == 0:
        if shot['shot_type'] == '2pt FG':
            player_df.loc[['shoot2FGA'], [shot['play_type']]] += 1
            player_df.loc[['shoot2FGM'], [shot['play_type']]] += 0
        elif shot['shot_type'] == '3pt FG':
            player_df.loc[['shoot3FGA'], [shot['play_type']]] += 1
            player_df.loc[['shoot3FGM'], [shot['play_type']]] += 0
    return player_df