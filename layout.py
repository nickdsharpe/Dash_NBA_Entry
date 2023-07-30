from maindash import app
from dash import html, dcc
import plotly.graph_objects as go
from assets.court import draw_plotly_court
from components import PlayerDropdown, PlayTypeDropdown, ShooterHeader, RecordShotButton, ShotChecklist, ClearLocationDataButton, FreeThrowInput

fig = go.Figure()

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
                        html.Div(id='team-one-creation-inputs-container'),
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
                        html.Div(id='team-two-creation-inputs-container'),
                        RecordShotButton('team-two'),
                        html.Div(id='team-two-shot-type')
                    ]
                ),
                dcc.Store(id='store-data', data=ovr_game_data, storage_type='session')
            ], style={'display': 'flex'}
        )

