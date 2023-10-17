from dash import dcc, html
import dash_daq as daq
import pandas as pd
import json

empty = pd.read_csv('assets/empty.csv')

nba_teams = {'ATL': 'Atlanta Hawks', 'BOS': 'Boston Celtics', 'BRK': 'Brooklyn Nets', 'CHO': 'Charlotte Hornets', 'CHI': 'Chicago Bulls', 'CLE': 'Cleveland Cavaliers', 'DAL': 'Dallas Mavericks', 'DEN': 'Denver Nuggets', 'DET': 'Detroit Pistons', 'GSW': 'Golden State Warriors',
             'HOU': 'Houston Rockets', 'IND': 'Indiana Pacers', 'LAC': 'Los Angeles Clippers', 'LAL': 'Los Angeles Lakers', 'MEM': 'Memphis Grizlies', 'MIA': 'Miami Heat', 'MIL': 'Milwaukee Bucks', 'MIN': 'Minnesota Timberwolves', 'NOP': 'New Orleans Pelicans', 
             'NYK': 'New York Knicks', 'OKC': 'Oklahoma City Thunder', 'ORL': 'Orlando Magic', 'PHI': 'Philadelphia 76ers', 'PHO': 'Phoenix Suns', 'POR': 'Portland Trailblazers', 'SAC': 'Sacramento Kings', 'SAS': 'San Antonio Spurs', 'TOR': 'Toronto Raptors',
             'UTA': 'Utah Jazz', 'WAS': 'Washington Wizards'}

play_types = ['PNR Ball Handler', 'PNR Screener', 'DHO Ball Handler', 'DHO Screener', 'Isolation', 'Transition', 'Attacking Closeouts',
             'Catch & Shoot', 'Off-Ball Screens', 'Cutting', 'Offensive Rebounds']
shot_types = ['2pt FG', '3pt FG', '2pt Free Throws', '3pt Free Throws', '2pt And-1', '3pt And-1']

with open('assets/rosters.json', 'r') as f:
    rosters = json.load(f)

def ShooterHeader(creation_checklist_id):
    return html.Div(children=[
        html.Div("Shooter", id=f'{creation_checklist_id}-shooter-header', className='shooter-header'),
        dcc.Checklist(
            ['Add Creator'],
            inline=True,
            id=f'{creation_checklist_id}-creation-checklist',
            className='creation-checklist',
            inputStyle={"marginRight": 8, 'transform': 'scale(1.5)'},
        )],
        style={'display': 'flex', 'alignItems': 'center'})

def ShotChecklist(checklist_id):
     return html.Div([
        dcc.Checklist(
            ['Make', 'Miss', 'Free Throws', 'And-1', 'Turnover'],
            inline=True,
            id=f'{checklist_id}-shot-checklist',
            inputStyle={"marginRight": 8, 'marginLeft': 20, 'transform': 'scale(1.5)'},
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
        players=['']
    elif player_dropdown_id == 'team-two':
        players=['']
        
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Player:", style={'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 20, 'paddingBottom': 13}),
                    dcc.Dropdown(
                        options=players,
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
                            'marginRight': 10, 'verticalAlign': 'middle', 'display': 'inline-block', 
                            'fontSize': 20, 'paddingBottom': 15
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
        players=['']
    elif passing_player_dropdown_id == 'team-two':
        players=['']
        
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Player:", style={'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 20, 'paddingBottom': 15}),
                    dcc.Dropdown(
                        options=players,
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
                            'marginRight': 10, 'verticalAlign': 'middle', 'display': 'inline-block', 
                            'fontSize': 20, 'paddingBottom': 10,
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
                                style={'borderRadius': '5px', 'marginTop': 20, 'padding': '0px 7px'}),
                    html.Div(id=f"{record_shot_id}-record-shot-output", className='record-shot-output')
                ], style={'align-items': 'center'}
            )

def ClearLocationDataButton(clear_location_id):
    return html.Div(
                children=[
                    html.Button("Clear Shot", id=f"{clear_location_id}-clear-shot-button", className='clear-shot-button'),
                    html.Div(id=f"{clear_location_id}-clear-shot-output")
                ]
            )

def TeamSelector(team_id):
    
    teams=list(nba_teams.values())
        
    return html.Div(   
        children=[
            html.Div(
                children=[
                    html.Div("Team:", style={'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 20, 'paddingBottom': 0}),
                    dcc.Dropdown(
                        teams,    
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
        players=['']
    elif defender_id == 'team-two':
        players=['']
        
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div("Defender:", style={'marginRight': 10, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 20, 'paddingBottom': 7}),
                    dcc.Dropdown(
                        options=players,
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

def UpdateRosterButton():
    return html.Div(
        children=[
            html.Progress(id=f"update-roster-progress", className='update-roster-progress', style={'display': 'none'}),
            html.Div(
                children=[
                    html.Button("Update Rosters", id=f"update-roster-button", className='update-roster-button',
                                style={'borderRadius': '5px', 'margin': '10px', 'padding': '0px 7px'}),
                    html.Button("Cancel", id=f"cancel-update-roster-button", className='cancel-update-roster-button',
                                style={'borderRadius': '5px', 'margin': '10px', 'padding': '0px 7px'}),
                ],
                style={'alignItems': 'center'}
            ),
            html.P(children=[''], id='update-roster-output', className='update-roster-output')
        ],
        id='update-roster-container',
        style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
    )

def DefenderTypeToggle(defense_id):
    return html.Div(
        children=[
            html.Div("POA", style={'marginRight': 9, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 20, 'paddingBottom': 2}),
            daq.ToggleSwitch(
                id=f'{defense_id}-defense-toggle',
                value=False,
                size=40,
                color={'on': '#03fc17', 'off': 'red'}
            ),
            html.Div("HELP", style={'marginLeft': 9, 'verticalAlign': 'middle', 
                                               'display': 'inline-block', 'fontSize': 20, 'paddingBottom': 2}),
        ],
        style={'display': 'flex', 'alignItems': 'center', 'marginTop': 10}
    )

def DefenderChecklist(defense_id):
    return html.Div(
        children=[
            dcc.Checklist(
            ['Steal', 'Block'],
            inline=True,
            id=f'{defense_id}-shot-checklist',
            inputStyle={"marginRight": 8, 'marginLeft': 20, 'transform': 'scale(1.5)'},
            className='defense-checklist'
        )
        ]
    )