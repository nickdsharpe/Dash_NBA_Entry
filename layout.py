from maindash import app
from dash import html, dcc
import plotly.graph_objects as go
from assets.court import draw_plotly_court
from components import PlayerDropdown, PlayTypeDropdown, ShooterHeader, RecordShotButton, ShotChecklist, ClearLocationDataButton, FreeThrowInput, PasserHeader, PassingPlayerDropdown, PassingPlayTypeDropdown, TeamSelector, DefenderDropdown, ShotQualitySlider, UpdateRosterButton, DefenderTypeToggle, DefenderChecklist, AddPlayerInput

fig = go.Figure()

shot_type = [{}, {}]
shot_result = [{}, {}]
play_type = [{}, {}]
player = [{}, {}]
shot_coordinates = [{}, {}]
free_throws = [{}, {}]
shot_quality = [{}, {}]
defender = [{'shooter': None}, {'shooter': None}]
defender_type = [{'shooter': 'POA'}, {'shooter': 'POA'}]
shot_zone = [{}, {}]
steals_blocks = [{'shooter': None}, {'shooter': None}]

app.config.suppress_callback_exceptions = True

def make_layout():
    return html.Div(id='main-container',   
                children=[
                    html.Div(id='team-one-container',
                        children=[
                            TeamSelector('team-one'),
                            html.Div(id='team-one-add-player-input-container', style={'display': 'none'}, children=[
                                AddPlayerInput('team-one')]
                            ),
                            html.Div(id='team-one-court-slider-container',
                                children=[ 
                                    html.Div(draw_plotly_court(fig, 'team-one'), id='team-one-court-plot'),
                                    ShotQualitySlider('team-one'),
                                ]
                            ),
                            ClearLocationDataButton('team-one'),
                            ShotChecklist('team-one'),
                            ShooterHeader('team-one'),
                            html.Div(id='team-one-free-throw-input-container', style={'display': 'none'}, children=[
                                FreeThrowInput('team-one')
                            ] ),
                            html.Div(id='team-one-free-throw-result'),
                            PlayerDropdown('team-one'),
                            PlayTypeDropdown('team-one'),
                            DefenderDropdown('team-one'),
                            html.Div(id='team-one-defender-container', children=[
                                DefenderChecklist('team-one'),
                                DefenderTypeToggle('team-one'),
                            ], style={'display': 'flex', 'alignItems': 'center'}),
                            html.Div(id='team-one-creation-inputs-container', style={'display': 'none'}, children=[
                                PasserHeader('team-one'),
                                PassingPlayerDropdown('team-one'), 
                                PassingPlayTypeDropdown('team-one')
                            ]),
                            RecordShotButton('team-one'),
                            html.Div(id='team-one-shot-type')
                        ], style={'width': '33.33%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
                    ),
                    html.Div(children=[UpdateRosterButton()], style={'width': '33.33%', 'align-items': 'center'}),
                    html.Div(id='team-two-container',
                        children=[
                            TeamSelector('team-two'),
                            html.Div(id='team-two-add-player-input-container', style={'display': 'none'}, children=[
                                AddPlayerInput('team-two')]
                            ),
                            html.Div(id='team-two-court-slider-container',
                                children=[
                                    html.Div(draw_plotly_court(fig, 'team-two'), id='team-two-court-plot'),
                                    ShotQualitySlider('team-two'),
                                ]
                            ),
                            ClearLocationDataButton('team-two'),
                            ShotChecklist('team-two'),
                            ShooterHeader('team-two'),
                            html.Div(id='team-two-free-throw-input-container', style={'display': 'none'}, children=[
                                FreeThrowInput('team-two')
                            ] ),
                            html.Div(id='team-two-shot-checklist-result'),
                            html.Div(id='team-two-free-throw-result'),
                            PlayerDropdown('team-two'),
                            PlayTypeDropdown('team-two'),
                            DefenderDropdown('team-two'),
                            html.Div(id='team-two-defender-container', children=[
                                DefenderChecklist('team-two'),
                                DefenderTypeToggle('team-two'),
                            ], style={'display': 'flex', 'alignItems': 'center'}),
                            html.Div(id='team-two-creation-inputs-container', style={'display': 'none'}, children=[
                                PasserHeader('team-two'),
                                PassingPlayerDropdown('team-two'), 
                                PassingPlayTypeDropdown('team-two')
                            ] ),
                            RecordShotButton('team-two'),
                            html.Div(id='team-two-shot-type')
                        ], style={'width': '33.33%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
                    ),
                    dcc.Store(id='shot-type', data=shot_type, storage_type='session'),
                    dcc.Store(id='shot-result', data=shot_result, storage_type='session'),
                    dcc.Store(id='play-type', data=play_type, storage_type='session'),
                    dcc.Store(id='player', data=player, storage_type='session'),
                    dcc.Store(id='shot-coordinates', data=shot_coordinates, storage_type='session'),
                    dcc.Store(id='free-throws', data=free_throws, storage_type='session'),
                    dcc.Store(id='shot-quality', data=shot_quality, storage_type='session'),
                    dcc.Store(id='defender', data=defender, storage_type='session'),
                    dcc.Store(id='defender-type', data=defender_type, storage_type='session'),
                    dcc.Store(id='steals-blocks', data=steals_blocks, storage_type='session'),
                    dcc.Store(id='shot-zone', data=shot_zone, storage_type='session'),
                    
                    dcc.Store(id='players', data=[], storage_type='session'),
                    dcc.Store(id='clear-components-flag', data=False, storage_type='session')
                ], style={'display': 'flex'}
            )