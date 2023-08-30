from dash import dcc, html,Input, Output, State
import dash_daq as daq
import pandas as pd
from dash_bootstrap_components import Modal, ModalHeader, ModalBody, ModalFooter, Button

empty = pd.read_csv('assets/empty.csv')

team_two_players = ['Butler', 'Adebayo', 'Herro', 'Lowry', 'Martin', 'D. Robinson', 'Love', 'Highsmith', 'Richardson', 'Jovic', 'Bryant', 'O. Robinson', 'Jaquez Jr.']
team_one_players = ['Jokic', 'Murray', 'Porter Jr.', 'Caldwell-Pope', 'Gordon', 'Braun', 'Watson', 'Jackson', 'Jordan', 'Cancar', 'Nnaji']

play_types = ['PNR Ball Handler', 'PNR Screener', 'DHO Ball Handler', 'DHO Screener', 'Isolation', 'Transition', 'Attacking Closeouts',
             'Catch & Shoot', 'Off-Ball Screens', 'Cutting', 'Offensive Rebounds']
shot_types = ['2pt FG', '3pt FG', '2pt Free Throws', '3pt Free Throws', '2pt And-1', '3pt And-1']

def ShooterHeader(creation_checklist_id):
    return html.Div(children=[
        html.Div("Shooter", id=f'{creation_checklist_id}-shooter-header', className='shooter-header'),
        dcc.Checklist(
            ['Add Creator'],
            inline=True,
            id=f'{creation_checklist_id}-creation-checklist',
            className='creation-checklist',
            inputStyle={"marginRight": 7},
        )],
        style={'display': 'flex', 'alignItems': 'center'})

def ShotChecklist(checklist_id):
     return html.Div([
        dcc.Checklist(
            ['Make', 'Miss', 'Free Throws', 'And-1', 'Turnover'],
            inline=True,
            id=f'{checklist_id}-shot-checklist',
            inputStyle={"marginRight": 5, 'marginLeft': 20},
            className='shot-checklist'
        )
    ])

def FreeThrowInput(FT_input_id):
    return html.Div(
        children=[
            html.Div("Free Throws:", id=f'{FT_input_id}-free-throw-label', className='free-throw-label'),
            dcc.Input(
            id=f'{FT_input_id}-free-throw-input',
            className='free-throw-input',
            placeholder='Free throws made',
            type='number',
            min=0,
            max=3
            )
        ],
        style={'display': 'flex', 'alignItems': 'center'})


def PlayerDropdown(player_dropdown_id):
    
    if player_dropdown_id == 'team-one':
        players=team_one_players
    elif player_dropdown_id == 'team-two':
        players=team_two_players
        
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Player:", style={'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 18, 'paddingBottom': 13}),
                    dcc.Dropdown(
                        players,
                        placeholder='Select a player',
                        id=f'{player_dropdown_id}-player-dropdown',
                        maxHeight=200,
                        clearable=True,
                        className='player-dropdown'
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id=f'{player_dropdown_id}-player-dropdown-output-container')
        ]
    )

def PlayTypeDropdown(play_type_dropdown_id):
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        "Play Type:",
                        id=f'{play_type_dropdown_id}-play-type-label',
                        style={
                            'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 'display': 'inline-block', 
                            'fontSize': 18, 'paddingBottom': 10
                        }
                    ),
                    dcc.Dropdown(
                        play_types,
                        className='play-type-dropdown',
                        placeholder='Select a play type',
                        id=f'{play_type_dropdown_id}-play-type-dropdown',
                        maxHeight=200,
                        clearable=True,
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id=f'{play_type_dropdown_id}-play-type-dropdown-output-container')
        ],
        className='play-type-dropdown-container'
    )

def PasserHeader(passer_header_id):
    return html.Div(children=[
        html.Hr(id=f'{passer_header_id}-creator-header-break', className='creator-header-break'),
        html.Div("Creator", id=f'{passer_header_id}-creator-header', className='creator-header')])

def PassingPlayerDropdown(passing_player_dropdown_id):
    
    if passing_player_dropdown_id == 'team-one':
        players=team_one_players
    elif passing_player_dropdown_id == 'team-two':
        players=team_two_players
        
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Player:", style={'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 18, 'paddingBottom': 13}),
                    dcc.Dropdown(
                        players,
                        placeholder='Select a player',
                        id=f'{passing_player_dropdown_id}-passing-player-dropdown',
                        maxHeight=200,
                        clearable=True,
                        className='passing-player-dropdown'
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id=f'{passing_player_dropdown_id}-passing-player-dropdown-output-container')
        ])

def PassingPlayTypeDropdown(passing_play_type_dropdown_id):
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        "Play Type:",
                        style={
                            'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 'display': 'inline-block', 
                            'fontSize': 18, 'paddingBottom': 10,
                        }
                    ),
                    dcc.Dropdown(
                        play_types,
                        placeholder='Select a play type',
                        id=f'{passing_play_type_dropdown_id}-passing-play-type-dropdown',
                        maxHeight=200,
                        clearable=True,
                        className='passing-play-type-dropdown'
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id=f'{passing_play_type_dropdown_id}-passing-play-type-dropdown-output-container')])

def RecordShotButton(record_shot_id):
    return html.Div(
                children=[
                    html.Button("Record Shot", id=f"{record_shot_id}-record-shot-button", className='record-shot-button',
                                style={'borderRadius': '5px', 'marginLeft': 45, 'marginTop': 20, 'padding': '0px 7px'}),
                    html.Div(id=f"{record_shot_id}-record-shot-output", className='record-shot-output')
                ]
            )

def ClearLocationDataButton(clear_location_id):
    return html.Div(
                children=[
                    html.Button("Clear Shot", id=f"{clear_location_id}-clear-shot-button", className='clear-shot-button'),
                    html.Div(id=f"{clear_location_id}-clear-shot-output")
                ]
            )

def TeamSelector(team_id):
    
    if team_id == 'team-one':
        players=team_one_players
    elif team_id == 'team-two':
        players=team_two_players
        
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Team:", style={'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 18, 'paddingBottom': 0}),
                    dcc.Dropdown(
                        players,
                        placeholder='Select a team',
                        id=f'{team_id}-team-dropdown',
                        maxHeight=200,
                        clearable=True,
                        className='team-dropdown'
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id=f'{team_id}-team-dropdown-output-container')
        ]
    )   

def DefenderDropdown(defender_id):
    
    if defender_id == 'team-one':
        players=team_two_players
    elif defender_id == 'team-two':
        players=team_one_players
        
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Defender:", style={'marginLeft': 45, 'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 18, 'paddingBottom': 15}),
                    dcc.Dropdown(
                        players,
                        placeholder='Select a defender',
                        id=f'{defender_id}-defender-dropdown',
                        maxHeight=200,
                        clearable=True,
                        className='defender-dropdown'
                    ),
                ],
                style={'display': 'flex', 'alignItems': 'center'}
            ),
            html.Div(id=f'{defender_id}-defender-dropdown-output-container')
        ]
    )   

def ShotQualitySlider(slider_id):
    return html.Div(
                    dcc.Slider(1, 5,
                        step=None,
                        marks={
                            1: {'label': 'Heavily Contested', 'style': {'color': '#f56c62', 'font-size': '16px'}}, 
                            2: {'label': 'Well Contested', 'style': {'color': '#f7aa57', 'font-size': '16px'}},
                            3: {'label': 'Lightly Contested', 'style': {'color': '#e6e673', 'font-size': '16px'}},
                            4: {'label': 'Late Contest', 'style': {'color': '#b3ff6b', 'font-size': '16px'}}, 
                            5: {'label': 'Open', 'style': {'color': '#81ff78', 'font-size': '16px'}}, 
                        },
                        vertical=True,
                        value=None,
                        id=f'{slider_id}-shot-quality-slider',
                    ),className='shot-quality-slider'
                    )