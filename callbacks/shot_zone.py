from maindash import app
import dash
from dash import no_update
from dash.dependencies import Input, Output
from assets.court import is_inside_three_point_line
from assets.shot_zone_math import inside_rim_shot_zone, inside_short_mid_range_shot_zone_1, inside_short_mid_range_shot_zone_2, inside_short_mid_range_shot_zone_3, inside_long_mid_range_shot_zone_1, inside_long_mid_range_shot_zone_5, inside_long_mid_range_shot_zone_2, inside_long_mid_range_shot_zone_4, inside_long_mid_range_shot_zone_3, inside_3pt_range_shot_zone_1, inside_3pt_range_shot_zone_5, inside_3pt_range_shot_zone_2, inside_3pt_range_shot_zone_4, inside_3pt_range_shot_zone_3

@app.callback(
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
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Team One
    if triggered_input_id == "team-one-court-graph":
    
        if inside_rim_shot_zone(team_one_click_data):
            team_one['shooter'] = 'Rim'
            team_one['creator'] = 'Rim'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_1(team_one_click_data):
            team_one['shooter'] = 'SMRZ 1'
            team_one['creator'] = 'SMRZ 1'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = 'SMRZ 2'
            team_one['creator'] = 'SMRZ 2'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = 'SMRZ 3'
            team_one['creator'] = 'SMRZ 3'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_1(team_one_click_data):
            team_one['shooter'] = 'LMRZ 1'
            team_one['creator'] = 'LMRZ 1'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = 'LMRZ 2'
            team_one['creator'] = 'LMRZ 2'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = 'LMRZ 3'
            team_one['creator'] = 'LMRZ 3'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_4(team_one_click_data):
            team_one['shooter'] = 'LMRZ 4'
            team_one['creator'] = 'LMRZ 4'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_5(team_one_click_data):
            team_one['shooter'] = 'LMRZ 5'
            team_one['creator'] = 'LMRZ 5'
            return updated_data
        
        elif inside_3pt_range_shot_zone_1(team_one_click_data):
            team_one['shooter'] = '3ptRZ 1'
            team_one['creator'] = '3ptRZ 1'
            return updated_data
        
        elif inside_3pt_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = '3ptRZ 2'
            team_one['creator'] = '3ptRZ 2'
            return updated_data
        
        elif inside_3pt_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = '3ptRZ 3'
            team_one['creator'] = '3ptRZ 3'
            return updated_data
        
        elif inside_3pt_range_shot_zone_4(team_one_click_data):
            team_one['shooter'] = '3ptRZ 4'
            team_one['creator'] = '3ptRZ 4'
            return updated_data
        
        elif inside_3pt_range_shot_zone_5(team_one_click_data):
            team_one['shooter'] = '3ptRZ 5'
            team_one['creator'] = '3ptRZ 5'
            return updated_data
        
        
        
    if triggered_input_id == "team-two-court-graph":
    
        if inside_rim_shot_zone(team_two_click_data):
            team_two['shooter'] = 'Rim'
            team_two['creator'] = 'Rim'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = 'SMRZ 1'
            team_two['creator'] = 'SMRZ 1'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = 'SMRZ 2'
            team_two['creator'] = 'SMRZ 2'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = 'SMRZ 3'
            team_two['creator'] = 'SMRZ 3'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = 'LMRZ 1'
            team_two['creator'] = 'LMRZ 1'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = 'LMRZ 2'
            team_two['creator'] = 'LMRZ 2'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = 'LMRZ 3'
            team_two['creator'] = 'LMRZ 3'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_4(team_two_click_data):
            team_two['shooter'] = 'LMRZ 4'
            team_two['creator'] = 'LMRZ 4'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_5(team_two_click_data):
            team_two['shooter'] = 'LMRZ 5'
            team_two['creator'] = 'LMRZ 5'
            return updated_data
        
        elif inside_3pt_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = '3ptRZ 1'
            team_two['creator'] = '3ptRZ 1'
            return updated_data
        
        elif inside_3pt_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = '3ptRZ 2'
            team_two['creator'] = '3ptRZ 2'
            return updated_data
        
        elif inside_3pt_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = '3ptRZ 3'
            team_two['creator'] = '3ptRZ 3'
            return updated_data
        
        elif inside_3pt_range_shot_zone_4(team_two_click_data):
            team_two['shooter'] = '3ptRZ 4'
            team_two['creator'] = '3ptRZ 4'
            return updated_data
        
        elif inside_3pt_range_shot_zone_5(team_two_click_data):
            team_two['shooter'] = '3ptRZ 5'
            team_two['creator'] = '3ptRZ 5'
            return updated_data
        
    return updated_data