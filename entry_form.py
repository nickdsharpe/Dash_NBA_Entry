from dash import dcc, html,Input, Output, State
import dash_daq as daq
import pandas as pd
from dash_bootstrap_components import Modal, ModalHeader, ModalBody, ModalFooter, Button

empty = pd.read_csv('empty.csv')

players = ['Jokic', 'Murray', 'Gordon', 'MPJ', 'KCP', 'Braun']
play_types = ['PNR Ball Handler', 'PNR Screener', 'DHO Ball Handler', 'DHO Screener', 'Isolation', 'Transition', 'Attacking Closeouts',
             'Catch & Shoot', 'Off-Ball Screens', 'Cutting', 'Offensive Rebounds']
shot_types = ['2pt FG', '3pt FG', '2pt Free Throws', '3pt Free Throws', '2pt And-1', '3pt And-1']

def ShooterHeader():
    return html.Div("Shooter", style={'marginLeft': 185,'fontSize': 25, 'paddingBottom': 8})

def ShotChecklist():
     return html.Div([
        dcc.Checklist(
            ['Make', 'Miss', 'Free Throws', 'Turnover'],
            inline=True,
            id='shot-checklist',
            style={'marginBottom': 15, 'marginLeft': 25, 'fontSize': 18},
            inputStyle={"marginRight": 5, 'marginLeft': 20}
        )
    ])

def FreeThrowInput():
    return html.Div([
        dcc.Input(
        id='free-throw-input',
        placeholder='Free Throws Made',
        type='number'
        )
    ])


def PlayerDropdown():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Player:", style={'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 18, 'paddingBottom': 13}),
                    dcc.Dropdown(
                        players,
                        placeholder='Select a player',
                        id='player-dropdown',
                        clearable=True,
                        style={'alignItems': 'center', 'maxWidth': 320, 'marginBottom': 5, 'flexGrow': 1}
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id='player-dropdown-output-container')
        ],
        className='player-dropdown-container'
    )

def PlayTypeDropdown():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        "Play Type:",
                        style={
                            'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 'display': 'inline-block', 
                            'fontSize': 18, 'paddingBottom': 13
                        }
                    ),
                    dcc.Dropdown(
                        play_types,
                        placeholder='Select a play type',
                        id='play-type-dropdown',
                        clearable=True,
                        style={'alignItems': 'center', 'maxWidth': 295, 'marginBottom': 5, 'flexGrow': 1}
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id='play-type-dropdown-output-container')
        ],
        className='play-type-dropdown-container'
    )
    
def ShotTypeDropdown():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        "Shot Type:",
                        style={
                            'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 'display': 'inline-block', 
                            'fontSize': 18, 'paddingBottom': 13
                        }
                    ),
                    dcc.Dropdown(
                        shot_types,
                        placeholder='Select a shot type',
                        id='shot-type-dropdown',
                        clearable=True,
                        style={'alignItems': 'center', 'maxWidth': 291, 'marginBottom': 5, 'flexGrow': 1}
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id='shot-type-dropdown-output-container')
        ],
        className='shot-type-dropdown-container'
    )

def MakePlayerDictionaries():
    player_dfs = {player: empty for player in players}
    return player_dfs

def RecordShotButton():
    return html.Div(
                children=[
                    html.Button("Record Shot", id="record-shot-button",
                                style={'borderRadius': '5px', 'marginLeft': 180, 'marginTop': 10, 'padding': '0px 7px'}),
                    html.Div(id="record-shot-output")
                ]
            )