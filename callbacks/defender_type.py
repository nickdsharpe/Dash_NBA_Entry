from maindash import app
import dash
from dash.dependencies import Input, Output

# Handle Defender Type Toggle
@app.callback(
    Output('defender-type', 'data'),
    
    Input('team-one-defense-toggle', 'value'),
    Input('team-two-defense-toggle', 'value'),
    Input('defender-type', 'data'),
    Input("team-one-record-shot-button", "n_clicks"),
    Input("team-two-record-shot-button", "n_clicks"),
)
def UpdateDefender(team_one_defender, team_two_defender, data, team_one_flag, team_two_flag):
    
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    #if triggered_input_id == "team-one-defense-toggle":
        
    if team_one_defender:
    
        team_one['shooter'] = 2
        
    else:
        team_one['shooter'] = 1
            
    #if triggered_input_id == "team-two-defense-toggle":
        
    if team_two_defender:
    
        team_two['shooter'] = 2
        
    else:
        team_two['shooter'] = 1
        
    return updated_data

            
    