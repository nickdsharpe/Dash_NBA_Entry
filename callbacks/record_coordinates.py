from maindash import app
from dash.dependencies import Input, Output

# Team One Track click events
@app.callback(
    Output('store-data', 'data', allow_duplicate=True),
    Input('team-one-court-graph', 'clickData'),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamOne_RecordCoordinates(clickData, data):
    updated_data = data.copy()
    shooter = updated_data['team-one-shooter']
    creator = updated_data['team-one-creator']
    
    if clickData is not None:
        x = clickData['points'][0]['x']
        y = clickData['points'][0]['y']
        shooter['x'] = x
        creator['x'] = x
        shooter['y'] = y
        creator['y'] = y
        return updated_data
    else:
        return updated_data
    
# Team Two Track click events
@app.callback(
    Output('store-data', 'data', allow_duplicate=True),
    Input('team-two-court-graph', 'clickData'),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamTwo_RecordCoordinates(clickData, data):
    updated_data = data.copy()
    shooter = updated_data['team-two-shooter']
    creator = updated_data['team-two-creator']
    
    if clickData is not None:
        x = clickData['points'][0]['x']
        y = clickData['points'][0]['y']
        shooter['x'] = x
        creator['x'] = x
        shooter['y'] = y
        creator['y'] = y
        return updated_data
    else:
        return updated_data