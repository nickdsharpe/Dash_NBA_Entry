from maindash import app
import dash
from dash.dependencies import Input, Output

# Handle Shot Quality
@app.callback(
    Output('shot-quality', 'data'),
    
    Input('team-one-shot-quality-slider', 'value'),
    Input('team-two-shot-quality-slider', 'value'),
    Input('shot-quality', 'data')
)
def UpdateShotQuality(team_one_shot_quality, team_two_shot_quality, data):
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-shot-quality-slider":
        
        team_one['shooter'] = team_one_shot_quality
        team_one['creator'] = team_one_shot_quality
        
        return updated_data
        
    if triggered_input_id == "team-two-shot-quality-slider":
        
        team_two['shooter'] = team_two_shot_quality
        team_two['creator'] = team_two_shot_quality
        
        return updated_data
    
    return updated_data