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
            team_one['shooter'] = 1
            return updated_data
        
        elif inside_short_mid_range_shot_zone_1(team_one_click_data):
            team_one['shooter'] = 2
            return updated_data
        
        elif inside_short_mid_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = 3
            return updated_data
        
        elif inside_short_mid_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = 4
            return updated_data
        
        elif inside_long_mid_range_shot_zone_1(team_one_click_data):
            team_one['shooter'] = 5
            return updated_data
        
        elif inside_long_mid_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = 6
            return updated_data
        
        elif inside_long_mid_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = 7
            return updated_data
        
        elif inside_long_mid_range_shot_zone_4(team_one_click_data):
            team_one['shooter'] = 8
            return updated_data
        
        elif inside_long_mid_range_shot_zone_5(team_one_click_data):
            team_one['shooter'] = 9
            return updated_data
        
        elif inside_3pt_range_shot_zone_1(team_one_click_data):
            team_one['shooter'] = 10
            return updated_data
        
        elif inside_3pt_range_shot_zone_2(team_one_click_data):
            team_one['shooter'] = 11
            return updated_data
        
        elif inside_3pt_range_shot_zone_3(team_one_click_data):
            team_one['shooter'] = 12
            return updated_data
        
        elif inside_3pt_range_shot_zone_4(team_one_click_data):
            team_one['shooter'] = 13
            return updated_data
        
        elif inside_3pt_range_shot_zone_5(team_one_click_data):
            team_one['shooter'] = 14
            return updated_data
        
        
        
    if triggered_input_id == "team-two-court-graph":
    
        if inside_rim_shot_zone(team_two_click_data):
            team_two['shooter'] = 1
            return updated_data
        
        elif inside_short_mid_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = 2
            return updated_data
        
        elif inside_short_mid_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = 3
            return updated_data
        
        elif inside_short_mid_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = 4
            return updated_data
        
        elif inside_long_mid_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = 5
            return updated_data
        
        elif inside_long_mid_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = 6
            return updated_data
        
        elif inside_long_mid_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = 7
            return updated_data
        
        elif inside_long_mid_range_shot_zone_4(team_two_click_data):
            team_two['shooter'] = 8
            return updated_data
        
        elif inside_long_mid_range_shot_zone_5(team_two_click_data):
            team_two['shooter'] = 9
            return updated_data
        
        elif inside_3pt_range_shot_zone_1(team_two_click_data):
            team_two['shooter'] = 10
            return updated_data
        
        elif inside_3pt_range_shot_zone_2(team_two_click_data):
            team_two['shooter'] = 11
            return updated_data
        
        elif inside_3pt_range_shot_zone_3(team_two_click_data):
            team_two['shooter'] = 12

            return updated_data
        
        elif inside_3pt_range_shot_zone_4(team_two_click_data):
            team_two['shooter'] = 13
            return updated_data
        
        elif inside_3pt_range_shot_zone_5(team_two_click_data):
            team_two['shooter'] = 14
            return updated_data
        
    return updated_data