from maindash import app
import dash
from dash import no_update
from dash.dependencies import Input, Output
from assets.court import is_inside_three_point_line
from assets.shot_zone_math import inside_rim_shot_zone, inside_short_mid_range_shot_zone_1, inside_short_mid_range_shot_zone_2, inside_short_mid_range_shot_zone_3, inside_long_mid_range_shot_zone_1, inside_long_mid_range_shot_zone_5, inside_long_mid_range_shot_zone_2, inside_long_mid_range_shot_zone_4, inside_long_mid_range_shot_zone_3

@app.callback(
    Output('team-one-shot-zone-output', 'children'),
    Output('team-two-shot-zone-output', 'children'),
    Output('shot-zone', 'data'),
    
    Input('team-one-court-graph', 'clickData'),
    Input('team-two-court-graph', 'clickData'),
    Input('shot-zone', 'data'),
    prevent_initial_call=True
)
def HandleShotZone(team_one_click_data, team_two_click_data, data):
    
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]
    
    if inside_rim_shot_zone(team_one_click_data):
        team_one['shooter'] = 'Rim'
        team_one['creator'] = 'Rim'
        return 'Rim', None, updated_data
    
    elif inside_short_mid_range_shot_zone_1(team_one_click_data):
        team_one['shooter'] = 'SMRZ 1'
        team_one['creator'] = 'SMRZ 1'
        return 'Short Mid-range Zone 1', None, updated_data
    
    elif inside_short_mid_range_shot_zone_2(team_one_click_data):
        team_one['shooter'] = 'SMRZ 2'
        team_one['creator'] = 'SMRZ 2'
        return 'Short Mid-range Zone 2', None, updated_data
    
    elif inside_short_mid_range_shot_zone_3(team_one_click_data):
        team_one['shooter'] = 'SMRZ 3'
        team_one['creator'] = 'SMRZ 3'
        return 'Short Mid-range Zone 3', None, updated_data
    
    elif inside_long_mid_range_shot_zone_1(team_one_click_data):
        team_one['shooter'] = 'LMRZ 1'
        team_one['creator'] = 'LMRZ 1'
        return 'Long Mid-range Zone 1', None, updated_data
    
    elif inside_long_mid_range_shot_zone_2(team_one_click_data):
        team_one['shooter'] = 'LMRZ 2'
        team_one['creator'] = 'LMRZ 2'
        return 'Long Mid-range Zone 2', None, updated_data
    
    elif inside_long_mid_range_shot_zone_3(team_one_click_data):
        team_one['shooter'] = 'LMRZ 3'
        team_one['creator'] = 'LMRZ 3'
        return 'Long Mid-range Zone 3', None, updated_data
    
    elif inside_long_mid_range_shot_zone_4(team_one_click_data):
        team_one['shooter'] = 'LMRZ 4'
        team_one['creator'] = 'LMRZ 4'
        return 'Long Mid-range Zone 4', None, updated_data
    
    elif inside_long_mid_range_shot_zone_5(team_one_click_data):
        team_one['shooter'] = 'LMRZ 5'
        team_one['creator'] = 'LMRZ 5'
        return 'Long Mid-range Zone 5', None, updated_data
    
    return '', '', updated_data