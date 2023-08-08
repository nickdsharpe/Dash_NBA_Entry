from maindash import app
import dash
from dash.dependencies import Input, Output

# Handle Defender Dropdown
@app.callback(
    Output('defender', 'data'),
    
    Input('team-one-defender-dropdown', 'value'),
    Input('team-two-defender-dropdown', 'value'),
    Input('defender', 'data'),
)
def UpdateDefender(team_one_defender, team_two_defender, data):
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-defender-dropdown":
        
        team_one['shooter'] = team_one_defender
        
        return updated_data
    
    if triggered_input_id == "team-two-defender-dropdown":
        
        team_two['shooter'] = team_two_defender
        
        return updated_data
    
    return updated_data