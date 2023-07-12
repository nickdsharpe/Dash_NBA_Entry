from dash import dcc, html
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import dash_daq as daq
import pandas as pd
import json

empty = pd.read_csv('empty.csv')

players = ['Jokic', 'Murray', 'Gordon', 'MPJ', 'KCP', 'Braun']
play_types = ['PNR Ball Handler', 'PNR Screener', 'DHO Ball Handler', 'DHO Screener', 'Isolation', 'Transition', 'Attacking Closeouts',
             'Catch & Shoot', 'Off-Ball Screens', 'Cutting', 'Offensive Rebounds']
shot_types = ['2pt FG', '3pt FG', '2pt Free Throws', '3pt Free Throws', '2pt And-1', '3pt And-1']

def ShooterHeader():
    return html.Div([
        html.H2('Shooter', style={'display': 'flex', 'alignItems': 'center', 'marginLeft': '80px', 'marginBottom': '10px',
                                  'marginTop': '5px'})
    ])

def ShotChecklist():
    return html.Div([
        dcc.Checklist(
            ['Make', 'Miss', 'Free Throws', 'Turnover'],
            inline=True,
            id='shot-checklist',
            style={'padding': 5},
            inputStyle={"marginRight": 5, 'marginLeft': 20}
        ), 
    ])

def FreeThrows():
    return html.Div([
        dcc.Input(
            id='free-throw-input',
            placeholder='Free Throws Made'
        )
    ])

def PlayerDropdown():
    return html.Div([
                    dcc.Dropdown(players,
                        placeholder='Select a player',
                        id='player-dropdown',
                        clearable=True,
                        style= {'minWidth': '300px', 'display': 'flex', 'alignItems': 'center', 'marginLeft': '20px'}),
                    html.Div(id='player-dropdown-output-container')
                    ])

def PlayTypeDropdown():
    return html.Div([
                    dcc.Dropdown(play_types,
                        placeholder='Select a play type',
                        id='play-type-dropdown',
                        clearable=True,
                        style= {'minWidth': '300px', 'display': 'flex', 'alignItems': 'center', 'marginLeft': '20px'}),
                    html.Div(id='play-type-dropdown-output-container')
                    ])
    
def ShotTypeDropdown():
    return html.Div([
                    dcc.Dropdown(shot_types,
                        placeholder='Select a shot type',
                        id='shot-type-dropdown',
                        clearable=True,
                        style= {'minWidth': '300px', 'display': 'flex', 'alignItems': 'center', 'marginLeft': '20px'}),
                    html.Div(id='shot-type-dropdown-output-container')
                    ])

def MakePlayerDictionaries():
    player_dfs = {player: empty for player in players}
    return player_dfs

def RecordShotButton():
    return html.Div(
                children=[
                    html.Button("Record Shot", id="record-shot-button"),
                    html.Div(id="record-shot-output")
                ]
            )