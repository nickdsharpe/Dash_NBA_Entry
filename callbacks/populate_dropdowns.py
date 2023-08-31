from maindash import app
import dash
from dash.dependencies import Input, Output
import json
from dash import no_update

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
    
    Input(component_id='team-one-team-dropdown', component_property='value'),
    Input(component_id='team-two-team-dropdown', component_property='value'),
)
def PopulateDropdowns(team_one, team_two):
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if (triggered_input_id == "team-one-team-dropdown") and (team_one is not None):
        
        selected_team = list(nba_teams.keys())[list(nba_teams.values()).index(team_one)]
        
        return rosters[selected_team], rosters[selected_team], no_update, no_update, no_update, rosters[selected_team]
    
    if (triggered_input_id == "team-two-team-dropdown") and (team_two is not None):
        
        selected_team = list(nba_teams.keys())[list(nba_teams.values()).index(team_two)]
        
        return no_update, no_update, rosters[selected_team], rosters[selected_team], rosters[selected_team], no_update
    
    return no_update, no_update, no_update, no_update, no_update, no_update