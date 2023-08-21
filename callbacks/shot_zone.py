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
            team_one['shooter'] = 'SMZ1'
            team_one['creator'] = 'SMZ1'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = 'SMZ2'
            team_one['creator'] = 'SMZ2'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = 'SMZ3'
            team_one['creator'] = 'SMZ3'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_1(team_one_click_data):
            team_one['shooter'] = 'LMZ1'
            team_one['creator'] = 'LMZ1'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = 'LMZ2'
            team_one['creator'] = 'LMZ2'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = 'LMZ3'
            team_one['creator'] = 'LMZ3'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_4(team_one_click_data):
            team_one['shooter'] = 'LMZ4'
            team_one['creator'] = 'LMZ4'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_5(team_one_click_data):
            team_one['shooter'] = 'LMZ5'
            team_one['creator'] = 'LMZ5'
            return updated_data
        
        elif inside_3pt_range_shot_zone_1(team_one_click_data):
            team_one['shooter'] = '3ptZ1'
            team_one['creator'] = '3ptZ1'
            return updated_data
        
        elif inside_3pt_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = '3ptZ2'
            team_one['creator'] = '3ptZ2'
            return updated_data
        
        elif inside_3pt_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = '3ptZ3'
            team_one['creator'] = '3ptZ3'
            return updated_data
        
        elif inside_3pt_range_shot_zone_4(team_one_click_data):
            team_one['shooter'] = '3ptZ4'
            team_one['creator'] = '3ptZ4'
            return updated_data
        
        elif inside_3pt_range_shot_zone_5(team_one_click_data):
            team_one['shooter'] = '3ptZ5'
            team_one['creator'] = '3ptZ5'
            return updated_data
        
        
        
    if triggered_input_id == "team-two-court-graph":
    
        if inside_rim_shot_zone(team_two_click_data):
            team_two['shooter'] = 'Rim'
            team_two['creator'] = 'Rim'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = 'SMZ1 '
            team_two['creator'] = 'SMZ1'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = 'SMZ2'
            team_two['creator'] = 'SMZ2'
            return updated_data
        
        elif inside_short_mid_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = 'SMZ3'
            team_two['creator'] = 'SMZ3'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = 'LMZ1'
            team_two['creator'] = 'LMZ1'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = 'LMZ2'
            team_two['creator'] = 'LMZ2'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = 'LMZ3'
            team_two['creator'] = 'LMZ3'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_4(team_two_click_data):
            team_two['shooter'] = 'LMZ4'
            team_two['creator'] = 'LMZ4'
            return updated_data
        
        elif inside_long_mid_range_shot_zone_5(team_two_click_data):
            team_two['shooter'] = 'LMZ5'
            team_two['creator'] = 'LMZ5'
            return updated_data
        
        elif inside_3pt_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = '3ptZ1'
            team_two['creator'] = '3ptZ1'
            return updated_data
        
        elif inside_3pt_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = '3ptZ2'
            team_two['creator'] = '3ptZ2'
            return updated_data
        
        elif inside_3pt_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = '3ptZ3'
            team_two['creator'] = '3ptZ3'
            return updated_data
        
        elif inside_3pt_range_shot_zone_4(team_two_click_data):
            team_two['shooter'] = '3ptZ4'
            team_two['creator'] = '3ptZ4'
            return updated_data
        
        elif inside_3pt_range_shot_zone_5(team_two_click_data):
            team_two['shooter'] = '3ptZ5'
            team_two['creator'] = '3ptZ5'
            return updated_data
        
    return updated_data