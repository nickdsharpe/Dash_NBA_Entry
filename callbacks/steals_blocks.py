from maindash import app
import dash
from dash.dependencies import Input, Output

@app.callback(
    Output('steals-blocks', 'data'),
    
    Input('team-one-defense-checklist', 'value'),
    Input('team-two-defense-checklist', 'value'),
    Input('steals-blocks', 'data'),
    
    prevent_initial_call=True
)
def StealsBlocks(team_one_value, team_two_value, data):
    
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-defense-checklist":

        if team_one_value == ['Steal']:

            team_one['shooter'] = 'STL'
            return updated_data
            
        if team_one_value == ['Block']:
            
            team_one['shooter'] = 'BLK'
            return updated_data
        
    if triggered_input_id == "team-two-defense-checklist":
        
        if team_two_value == ['Steal']:
            
            team_two['shooter'] = 'STL'
            return updated_data
            
        if team_two_value == ['Block']:
            
            team_two['shooter'] = 'BLK'
            return updated_data
        
    return updated_data
        