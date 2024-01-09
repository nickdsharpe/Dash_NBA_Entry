from maindash import app
from dash import Input, Output, no_update
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
    Output('game-id', 'data', allow_duplicate=True),
    Output('team-ids', 'data', allow_duplicate=True),
    
    Input('add-game-input-button', 'n_clicks'),
    Input('enter-game-input-button', 'n_clicks'),
    Input('add-game-input-date', 'value'),
    Input('add-game-input-home', 'value'),
    Input('add-game-input-away', 'value'),
    
    Input('game-id', 'data'),
    Input('team-ids', 'data')
)
def CreateGame(create_game_click, enter_game_click, date, home, away, game_id_store, team_ids_store):
    
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

    if create_game_click:
        
        if (teams['name'].isin([home]).any()) and (teams['name'].isin([away]).any()):
            
            home_data = teams[teams['name'] == home]
            away_data = teams[teams['name'] == away]
            
            home_id = home_data['id'].values[0]
            away_id = away_data['id'].values[0]
            
            team_ids_store[0]['home'] = home_id
            team_ids_store[0]['away'] = away_id
            
            insert_query = f'insert into "Games" (date, home_team, away_team) values (\'{date}\', {home_id}, {away_id});'
            engine.execute(insert_query)
            
            game_query = f'select * from "Games" where "date" = \'{date}\''
            
            game_result = engine.execute(game_query)
            game_rows = game_result.fetchall()
            game_columns = game_result.keys()
            game = pd.DataFrame(game_rows, columns=game_columns)
            
            game_id = game['id'].values[0]
            
            game_id_store[0]['id'] = game_id
            
            return {'display': 'none'}, 'Game Created', game_id_store, team_ids_store
        else:
            return {'display': 'none'}, 'Incorrect Data', no_update, no_update
        
    elif enter_game_click:
        
        home_data = teams[teams['name'] == home]
        away_data = teams[teams['name'] == away]
        
        home_id = home_data['id'].values[0]
        away_id = away_data['id'].values[0]
        
        team_ids_store[0]['home'] = home_id
        team_ids_store[0]['away'] = away_id
        
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
        
        game_query = f'select * from "Games" where "date" = \'{date}\''
        
        game_result = engine.execute(game_query)
        game_rows = game_result.fetchall()
        game_columns = game_result.keys()
        game = pd.DataFrame(game_rows, columns=game_columns)
        
        game_id = game['id'].values[0]
        
        game_id_store[0]['id'] = game_id
        
        return {'display': 'none'}, 'Game Entered', game_id_store, team_ids_store
        
    return no_update, no_update, no_update, no_update