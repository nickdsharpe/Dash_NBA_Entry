from maindash import app
import dash
from dash import no_update
from dash.dependencies import Input, Output
from assets.court import is_inside_three_point_line
from callbacks.shot_zone import is_inside_rim_shot_zone, is_inside_short_mid_range_shot_zone_3, is_inside_short_mid_range_shot_zone_1, is_inside_short_mid_range_shot_zone_2

@app.callback(
        Output('team-one-shot-type', 'children'),
        Output('team-two-shot-type', 'children'),
        Output('shot-type', 'data'),
        
        Input('team-one-court-graph', 'clickData'),
        Input('team-two-court-graph', 'clickData'),
        Input('shot-type', 'data'),
    prevent_initial_call=True
)
def handle_shot_type(team_one_clickData, team_two_clickData, data):
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]

    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Team One
    if triggered_input_id == "team-one-court-graph":
        
        print(is_inside_short_mid_range_shot_zone_2(team_one_clickData))
        
        if is_inside_three_point_line(team_one_clickData):
            
            team_one['shooter'] = '2pt FG'
            team_one['creator'] = '2pt FG'
            
            shot_type = '2pt FG'
            
        else:
    
            team_one['shooter'] = '3pt FG'
            team_one['creator'] = '3pt FG'
            
            shot_type = '3pt FG'
        
        return shot_type, no_update, updated_data
    
    # Team One
    if triggered_input_id == "team-two-court-graph":
        
        if is_inside_three_point_line(team_two_clickData):
            
            team_two['shooter'] = '2pt FG'
            team_two['creator'] = '2pt FG'
            
            shot_type = '2pt FG'
            
        else:
    
            team_two['shooter'] = '3pt FG'
            team_two['creator'] = '3pt FG'
            
            shot_type = '3pt FG'
        
        return no_update, shot_type, updated_data
    
    return no_update, no_update, no_update