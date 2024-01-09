from maindash import app
import dash
from dash.dependencies import Input, Output
import json
from dash import no_update
from sqlalchemy import create_engine
import pandas as pd
import configparser

nba_teams = {'ATL': 'Atlanta Hawks', 'BOS': 'Boston Celtics', 'BRK': 'Brooklyn Nets', 'CHO': 'Charlotte Hornets', 'CHI': 'Chicago Bulls', 'CLE': 'Cleveland Cavaliers', 'DAL': 'Dallas Mavericks', 'DEN': 'Denver Nuggets', 'DET': 'Detroit Pistons', 'GSW': 'Golden State Warriors',
             'HOU': 'Houston Rockets', 'IND': 'Indiana Pacers', 'LAC': 'Los Angeles Clippers', 'LAL': 'Los Angeles Lakers', 'MEM': 'Memphis Grizlies', 'MIA': 'Miami Heat', 'MIL': 'Milwaukee Bucks', 'MIN': 'Minnesota Timberwolves', 'NOP': 'New Orleans Pelicans', 
             'NYK': 'New York Knicks', 'OKC': 'Oklahoma City Thunder', 'ORL': 'Orlando Magic', 'PHI': 'Philadelphia 76ers', 'PHO': 'Phoenix Suns', 'POR': 'Portland Trailblazers', 'SAC': 'Sacramento Kings', 'SAS': 'San Antonio Spurs', 'TOR': 'Toronto Raptors',
             'UTA': 'Utah Jazz', 'WAS': 'Washington Wizards'}

with open('assets/rosters.json', 'r') as f:
    rosters = json.load(f)

@app.callback(
    Output(component_id='team-one-player-dropdown', component_property='options'),
    Output(component_id='team-one-passing-player-dropdown', component_property='options'),
    Output(component_id='team-one-defender-dropdown', component_property='options'),
    
    Output(component_id='team-two-player-dropdown', component_property='options'),
    Output(component_id='team-two-passing-player-dropdown', component_property='options'),
    Output(component_id='team-two-defender-dropdown', component_property='options'),
    
    Output('player-ids', 'data', allow_duplicate=True),
    
    Input(component_id='team-one-team-dropdown', component_property='value'),
    Input(component_id='team-two-team-dropdown', component_property='value'),
    
    Input('team-ids', 'data'),
    Input('player-ids', 'data')
)
def PopulateDropdowns(team_one, team_two, team_ids, player_ids):
 
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if (triggered_input_id == "team-one-team-dropdown") and (team_one is not None):
        
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
        query = f"select * from \"Players\" where \"team_id\" = {team_ids[0]['home']}"
        result = engine.execute(query)
        rows = result.fetchall()
        columns = result.keys()
        team = pd.DataFrame(rows, columns=columns)
      
        home_player_ids = {
                        f"{row['first_name']} {row['last_name']}": row['id']
                        for index, row in team.iterrows()
                    }
        player_ids[0]['home'] = home_player_ids

        selected_team = list(nba_teams.keys())[list(nba_teams.values()).index(team_one)]
        
        return rosters[selected_team], rosters[selected_team], no_update, no_update, no_update, rosters[selected_team], player_ids
    
    if (triggered_input_id == "team-two-team-dropdown") and (team_two is not None):
        
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
        query = f"select * from \"Players\" where \"team_id\" = {team_ids[0]['away']}"
        result = engine.execute(query)
        rows = result.fetchall()
        columns = result.keys()
        team = pd.DataFrame(rows, columns=columns)
        
        away_player_ids = {
                        f"{row['first_name']} {row['last_name']}": row['id']
                        for index, row in team.iterrows()
                    }
        player_ids[1]['away'] = away_player_ids
        
        selected_team = list(nba_teams.keys())[list(nba_teams.values()).index(team_two)]
        
        return no_update, no_update, rosters[selected_team], rosters[selected_team], rosters[selected_team], no_update, player_ids
    
    return no_update, no_update, no_update, no_update, no_update, no_update, no_update