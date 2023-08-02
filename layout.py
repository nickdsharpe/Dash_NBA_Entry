from maindash import app
from dash import html, dcc
import plotly.graph_objects as go
from assets.court import draw_plotly_court
from components import PlayerDropdown, PlayTypeDropdown, ShooterHeader, RecordShotButton, ShotChecklist, ClearLocationDataButton, FreeThrowInput, PasserHeader, PassingPlayerDropdown, PassingPlayTypeDropdown

fig = go.Figure()

team_one = {'shooter' : {}, 'creator': {}}
team_two = {'shooter' : {}, 'creator': {}}
ovr_game_data = {'team-one-shooter' : {}, 'team-one-creator': {}, 'team-two-shooter' : {}, 'team-two-creator': {}}

# Create a store to save the dictionaries
app.config.suppress_callback_exceptions = True

def make_layout():
    return html.Div(id='main-container',
            children=[
                html.Div(id='team-one-container',
                    children=[
                        html.Div(draw_plotly_court(fig, 'team-one'), id='team-one-court-plot'),
                        ClearLocationDataButton('team-one'),
                        ShotChecklist('team-one'),
                        ShooterHeader('team-one'),
                        html.Div(id='team-one-free-throw-input-container', style={'display': 'none'}, children=[
                            FreeThrowInput('team-one')
                        ] ),
                        html.Div(id='team-one-free-throw-result'),
                        PlayerDropdown('team-one'),
                        PlayTypeDropdown('team-one'),
                        html.Div(id='team-one-creation-inputs-container', style={'display': 'none'}, children=[
                            PasserHeader('team-one'),
                            PassingPlayerDropdown('team-one'), 
                            PassingPlayTypeDropdown('team-one')
                        ] ),
                        RecordShotButton('team-one'),
                        html.Div(id='team-one-shot-type')
                    ]
                ),
                html.Div(id='team-two-container',
                    children=[
                        html.Div(draw_plotly_court(fig, 'team-two'), id='team-two-court-plot'),
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
                        html.Div(id='team-two-creation-inputs-container', style={'display': 'none'}, children=[
                            PasserHeader('team-two'),
                            PassingPlayerDropdown('team-two'), 
                            PassingPlayTypeDropdown('team-two')
                        ] ),
                        RecordShotButton('team-two'),
                        html.Div(id='team-two-shot-type')
                    ]
                ),
                dcc.Store(id='team-one', data=ovr_game_data, storage_type='session'),
                dcc.Store(id='team-two', data=ovr_game_data, storage_type='session')
            ], style={'display': 'flex'}
        )

