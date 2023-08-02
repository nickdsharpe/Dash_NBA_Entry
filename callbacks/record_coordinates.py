from maindash import app
import dash
from dash.dependencies import Input, Output

# Team One Track click events
@app.callback(
    Output('shot-coordinates', 'data'),
    
    Input('team-one-court-graph', 'clickData'),
    Input('team-two-court-graph', 'clickData'),
    Input('shot-coordinates', 'data'),
    prevent_initial_call=True
)
def teamOne_RecordCoordinates(team_one_value, team_two_value, data):
    updated_data = data.copy()
    
    team_one = updated_data['team-one']
    team_two = updated_data['team-two']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-court-graph":
        
        x = team_one_value['points'][0]['x']
        y = team_one_value['points'][0]['y']
        
        print('Shot Coordinates Recorded')
        
        team_one['x'] = x
        team_one['y'] = y
        
        print(updated_data)
        
        return updated_data
    
    if triggered_input_id == "team-two-court-graph":
        
        x = team_two_value['points'][0]['x']
        y = team_two_value['points'][0]['y']
        
        team_two['x'] = x
        team_two['y'] = y
        
        return updated_data
    
    return updated_data