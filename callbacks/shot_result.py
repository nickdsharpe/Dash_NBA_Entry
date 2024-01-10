from maindash import app
import dash
from dash.dependencies import Input, Output

## TEAM ONE ###
# Make | Miss | Free Throws | And-1 | Turnover checklist callback
@app.callback(
    Output('team-one-free-throw-input-container', 'style'),
    Output('team-two-free-throw-input-container', 'style'),
    Output('shot-result', 'data'),
    
    Input("team-one-shot-checklist", "value"),
    Input("team-two-shot-checklist", "value"),
    Input('shot-result', 'data'),
    prevent_initial_call=True
)
def team_one_update_shot_result(team_one_value, team_two_value, data):
    updated_data = data.copy()
    
    team_one = updated_data[0]
    team_two = updated_data[1]
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-shot-checklist":

        if team_one_value == ['Miss']:
            team_one['shooter'] = 2
            return {'display': 'none'}, {'display': 'none'},  updated_data
        
        elif team_one_value == ['Make']:
            team_one['shooter'] = 1
            return {'display': 'none'}, {'display': 'none'}, updated_data
        
        elif team_one_value == ['Free Throws']:
            team_one['shooter'] = 3
            return {'display': 'block'}, {'display': 'none'}, updated_data
        
        elif team_one_value == ['And-1']:
            team_one['shooter'] = 4
            return {'display': 'block'}, {'display': 'none'}, updated_data
        
        elif team_one_value == ['Turnover']:
            team_one['shooter'] = 5
            return {'display': 'none'}, {'display': 'none'}, updated_data
        
        elif team_one_value == ['Passing Turnover']:
            team_one['shooter'] = 6
            return {'display': 'none'}, {'display': 'none'}, updated_data
        
    if triggered_input_id == "team-two-shot-checklist":
        
        if team_two_value == ['Miss']:
            team_two['shooter'] = 2
          
            return {'display': 'none'}, {'display': 'none'},  updated_data
        
        elif team_two_value == ['Make']:
            
            team_two['shooter'] = 1
            
            return {'display': 'none'}, {'display': 'none'}, updated_data
        
        elif team_two_value == ['Free Throws']:
            team_two['shooter'] = 3
            return {'display': 'none'}, {'display': 'block'}, updated_data
        
        elif team_two_value == ['And-1']:
            team_two['shooter'] = 4

            return {'display': 'none'}, {'display': 'block'}, updated_data
        
        elif team_two_value == ['Turnover']:
            team_two['shooter'] = 5
            return {'display': 'none'}, {'display': 'none'}, updated_data
        
        elif team_two_value == ['Passing Turnover']:
            team_two['shooter'] = 6
            return {'display': 'none'}, {'display': 'none'}, updated_data
        
        
    return {'display': 'none'}, {'display': 'none'}, updated_data