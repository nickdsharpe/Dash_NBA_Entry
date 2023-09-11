from maindash import app
import os
from dash import DiskcacheManager, Input, Output
import diskcache
import time
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup, Comment
import pandas as pd
import os
import time
import requests
import json

cache = diskcache.Cache("./cache")
background_callback_manager = DiskcacheManager(cache)

team_tickers = ['MIA', 'WAS', 'TOR', 'PHI', 'ORL', 'NYK', 'MIL', 'ATL', 'IND', 'CLE', 'BOS', 'BRK', 'CHI', 'CHO', 'DET', 'MEM', 'DEN', 'DAL', 
                'MIN', 'NOP', 'GSW', 'OKC', 'LAL', 'LAC', 'PHO', 'POR', 'SAC', 'SAS', 'UTA', 'HOU']

nba_rosters = {team: [] for team in team_tickers}

def get_html(url, sleep=5, retries=3):
    
    for i in range(1, retries+1):
        time.sleep(sleep * i)
        
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            print(soup.title.string)
            return str(soup)
        except requests.exceptions.Timeout:
            print(f'Timeout error on {url}')
            
    return None

def update_roster(ticker):
    
    html = get_html(f'https://www.basketball-reference.com/contracts/{ticker}.html')
    soup = BeautifulSoup(html, 'html.parser')
    
    rows = soup.find_all('tr')
    
    for row in rows:
        try:
            player = row.find("a").get_text()

            contract = row.find('td', {'data-stat': 'y1'})
            on_payroll = contract.get_text()
            if on_payroll:
                nba_rosters[ticker].append(player)
        except:
            continue

@app.callback(
        Output('update-roster-output', 'children'),
        Input('update-roster-button', 'n_clicks'),
        background=True,
        manager=background_callback_manager,
        prevent_initial_call=True,
        running=[
        (Output("update-roster-button", "disabled"), True, False),
        (Output("cancel-update-roster-button", "disabled"), False, True),
        (
            Output("update-roster-output", "style"),
            {"visibility": "hidden"},
            {"visibility": "visible"},
        ),
        (
            Output("update-roster-progress", "style"),
            {"visibility": "visible"},
            {"visibility": "hidden"},
        ),
        ],
        cancel=[Input("cancel-update-roster-button", "n_clicks")],
        progress=[Output("update-roster-progress", "value"), Output("update-roster-progress", "max")],
)
def UpdateRosters(set_progress, n_clicks):
    
    total = 30
    count = 0
    for ticker in nba_rosters.keys():
        update_roster(ticker)
        count +=1
        set_progress((str(count), str(total)))
        
    path = './assets/rosters.json'
    
    with open(path, 'w') as f:
        json.dump(nba_rosters, f)
        
    return ['Rosters Updated.']