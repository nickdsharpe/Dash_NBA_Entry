from dash import dcc, html
from dash.dependencies import Input, Output
from dash.development.base_component import Component
import dash_daq as daq

players = ['Jokic', 'Murray', 'Gordon', 'MPJ', 'KCP', 'Braun']
play_types = ['PNR Ball Handler', 'PNR Screener', 'DHO Ball Handler', 'DHO Screener', 'Isolation', 'Transition', 'Attacking Closeouts',
             'Catch & Shoot', 'Off-Ball Screens', 'Cutting', 'Offensive Rebounds']

def ShooterHeader():
    return html.Div([
        html.H2('Shooter', style={'display': 'flex', 'align-items': 'center', 'margin-left': '80px', 'margin-bottom': '10px',
                                  'margin-top': '5px'})
    ])

def ToggleSwitch():
    return html.Div([
                    daq.ToggleSwitch(
                        id="shot-switch", 
                        value=False, size=50,
                        label='Make | Miss',
                        labelPosition='bottom',
                        style= {'display': 'flex', 'align-items': 'center', 'margin-left': '40px', 'margin-bottom': '10px'}
                        ),
                    ], className='shot-switch-container')

def PlayerDropdown():
    return html.Div([
                    dcc.Dropdown(players,
                        placeholder='Select a player',
                        id='player-dropdown',
                        clearable=True,
                        style= {'min-width': '300px', 'display': 'flex', 'align-items': 'center', 'margin-left': '20px'}),
                    html.Div(id='player-dropdown-output-container')
                    ])

def PlayTypeDropdown():
    return html.Div([
                    dcc.Dropdown(play_types,
                        placeholder='Select a play type',
                        id='play-type-dropdown',
                        clearable=True,
                        style= {'min-width': '300px', 'display': 'flex', 'align-items': 'center', 'margin-left': '20px'}),
                    html.Div(id='play-type-dropdown-output-container')
                    ])
    