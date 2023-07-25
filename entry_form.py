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
    return html.Div(children=[
        html.Div("Shooter", id='shooter-header'),
        dcc.Checklist(
            ['Shot Created?'],
            inline=True,
            id='creation-checklist',
            inputStyle={"marginRight": 5},
        )],
        style={'display': 'flex', 'alignItems': 'center'})

def ShotChecklist():
     return html.Div([
        dcc.Checklist(
            ['Make', 'Miss', 'Free Throws', 'Turnover'],
            inline=True,
            id='shot-checklist',
            inputStyle={"marginRight": 5, 'marginLeft': 20},
        )
    ])

def FreeThrowInput():
    return html.Div(
        children=[
            html.Div("Free Throws:", style={'verticalAlign': 'middle', 'display': 'inline-block', 'fontSize': 18, 'marginLeft': 45, 'paddingBottom': 13, 'backgroundColor': '#242424'}),
            dcc.Input(
            id='free-throw-input',
            placeholder='Free throws made',
            type='number',
            min=0,
            max=3
            )
        ],
        style={'display': 'flex', 'alignItems': 'center'})


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
                        style={'alignItems': 'center', 'maxWidth': 300, 'marginBottom': 5, 'flexGrow': 1, 'backgroundColor': '#242424'}
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
                        style={'alignItems': 'center', 'maxWidth': 272, 'marginBottom': 5, 'flexGrow': 1, 'backgroundColor': '#242424'}
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id='play-type-dropdown-output-container')
        ],
        className='play-type-dropdown-container'
    )

def PassingPlayerDropdown():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Player:", style={'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 18, 'paddingBottom': 13}),
                    dcc.Dropdown(
                        players,
                        placeholder='Select a player',
                        id='passing-player-dropdown',
                        clearable=True,
                        style={'alignItems': 'center', 'maxWidth': 300, 'marginBottom': 5, 'flexGrow': 1, 'backgroundColor': '#242424'}
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
        ])

def PassingPlayTypeDropdown():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        "Play Type:",
                        style={
                            'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 'display': 'inline-block', 
                            'fontSize': 18, 'paddingBottom': 13,
                        }
                    ),
                    dcc.Dropdown(
                        play_types,
                        placeholder='Select a play type',
                        id='passing-play-type-dropdown',
                        clearable=True,
                        style={'alignItems': 'center', 'maxWidth': 272, 'marginBottom': 5, 'flexGrow': 1, 'backgroundColor': '#242424'}
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            )])

def MakePlayerDictionaries():
    player_dfs = {player: empty for player in players}
    return player_dfs

def PasserHeader():
    return html.Div(children=[
        html.Hr(id='creator-header-break'),
        html.Div("Creator", id='creator-header')])
        

def RecordShotButton():
    return html.Div(
                children=[
                    html.Button("Record Shot", id="record-shot-button",
                                style={'borderRadius': '5px', 'marginLeft': 45, 'marginTop': 10, 'padding': '0px 7px'}),
                    html.Div(id="record-shot-output")
                ]
            )

def ClearLocationDataButton():
    return html.Div(
                children=[
                    html.Button("Clear Shot", id="clear-shot-button",),
                    html.Div(id="clear-shot-output")
                ]
            )