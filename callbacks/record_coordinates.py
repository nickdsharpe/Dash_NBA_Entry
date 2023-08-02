from maindash import app
import dash
from dash.dependencies import Input, Output

# Team One Track click events
@app.callback(
    Output('team-one', 'data'),
    
    Input('team-one-court-graph', 'clickData'),
    Input('team-one', 'data'),
    prevent_initial_call=True
)
def teamOne_RecordCoordinates(value, data):
    updated_data = data.copy()
    
    shooter = updated_data['shooter']
    creator = updated_data['creator']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-court-graph":
        
        x = data['points'][0]['x']
        y = data['points'][0]['y']
        
        shooter['x'] = x
        creator['x'] = x
        shooter['y'] = y
        creator['y'] = y
        
        return updated_data
    
    return updated_data



# Team Two Track click events
@app.callback(
    Output('team-two', 'data'),
    
    Input('team-two-court-graph', 'clickData'),
    Input('team-two', 'data'),
    prevent_initial_call=True
)
def teamtwo_RecordCoordinates(value, data):
    updated_data = data.copy()
    
    shooter = updated_data['shooter']
    creator = updated_data['creator']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-two-court-graph":
        
        x = data['points'][0]['x']
        y = data['points'][0]['y']
        
        shooter['x'] = x
        creator['x'] = x
        shooter['y'] = y
        creator['y'] = y
        
        return updated_data
    
    return updated_data