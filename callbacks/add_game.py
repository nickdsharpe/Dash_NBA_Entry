from maindash import app
import os
from dash import DiskcacheManager, Input, Output, no_update
import diskcache
import time
from splinter import Browser
from bs4 import BeautifulSoup, Comment
from sqlalchemy import create_engine
import pandas as pd
import configparser
import os
import time
import requests
import json


@app.callback(
    Output('add-game-input-container', 'style'),
    Input('add-game-button', 'n_clicks')
)
def AddGame(click):
    
    if click:
        if click % 2 ==0:
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
            
            print(teams)
            
            return {'display': 'block'}

        else:
            return {'display': 'none'}
    
    return no_update

###   NEXT STEPS ###
'''
- Get the values from each input box 
- Store them as variables
- Cross reference the teams table to make sure the entered teams are valid
- Get each teams id
- Write the game to the "Games" table
'''