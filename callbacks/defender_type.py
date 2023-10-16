from maindash import app
import dash
from dash.dependencies import Input, Output

# Handle Defender Type Toggle
@app.callback(
    Output('defender-type', 'data'),
    
    Input('team-one-defense-toggle', 'value'),
    Input('team-two-defense-toggle', 'value'),
    Input('defender-type', 'data'),
)
def UpdateDefender(team_one_defender, team_two_defender, data):
    
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-defense-toggle":
        
        if team_one_defender:
        
            team_one['shooter'] = 'HELP'
            
        else:
            team_one['shooter'] = 'POA'
            
        return updated_data
            
    if triggered_input_id == "team-two-defense-toggle":
        
        if team_two_defender:
        
            team_two['shooter'] = 'HELP'
            
        else:
            team_two['shooter'] = 'POA'
            
        return updated_data
    
    return updated_data
            
    