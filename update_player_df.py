import pandas as pd
import json

players = ['Jokic', 'Murray', 'Gordon', 'MPJ', 'KCP', 'Braun']
empty = pd.read_csv('empty.csv')
team_data = {player: empty for player in players}

def UpdatePlayerDF(shot):

    player_df = team_data[shot['player']]

    return player_df