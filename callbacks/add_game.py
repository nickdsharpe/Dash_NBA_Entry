from maindash import app
from dash import Input, Output, no_update
from datetime import datetime
from splinter import Browser
from sqlalchemy import create_engine
import pandas as pd
import configparser


@app.callback(
    Output('add-game-input-container', 'style', allow_duplicate=True),
    Output('add-game-output', 'children', allow_duplicate=True),
    
    Input('add-game-button', 'n_clicks')
)
def AddGame(click):
    
    if click:
        if click % 2 ==0:
            
            return {'display': 'none'}, ''

        else:
            return {'display': 'block'}, ''
    
    return no_update, no_update


@app.callback(
    Output('add-game-input-container', 'style', allow_duplicate=True),
    Output('add-game-output', 'children', allow_duplicate=True),
    
    Input('add-game-input-button', 'n_clicks'),
    Input('add-game-input-date', 'value'),
    Input('add-game-input-home', 'value'),
    Input('add-game-input-away', 'value'),
)
def CreateGame(click, date, home, away):

    if click:
        config = configparser.ConfigParser()
        config.read('assets/database.ini')
        
        # Accessing database connection details
        name = config['Database']['name']
        host = config['Database']['host']
        username = config['Database']['username']
        password = config['Database']['password']

        # Create the connection string
        connection_str = f'postgresql+psycopg2://{username}:{password}@{host}:5432/{name}'

        # Create the SQLAlchemy engine
        engine = create_engine(connection_str)
        
        # Fetch data from Database
        result = engine.execute('SELECT * FROM "Teams"')
        rows = result.fetchall()
        columns = result.keys()
        teams = pd.DataFrame(rows, columns=columns)
        
        if (teams['name'].isin([home]).any()) and (teams['name'].isin([away]).any()):
            
            home_data = teams[teams['name'] == home]
            away_data = teams[teams['name'] == away]
            
            home_id = home_data['id'].values[0]
            away_id = away_data['id'].values[0]
            
            query = f'insert into "Games" (date, home_team, away_team) values (\'{date}\', {home_id}, {away_id});'
            engine.execute(query)
            
            return {'display': 'none'}, 'Game Created'
        
        else:
            return {'display': 'none'}, 'Incorrect Data'
    
    return no_update, no_update