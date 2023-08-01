from maindash import app
import dash
from dash.dependencies import Input, Output

# Team One Track click events
@app.callback(
    Output('store-data', 'data', allow_duplicate=True),
    Input('team-one-court-graph', 'clickData'),
    Input('team-two-court-graph', 'clickData'),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamOne_RecordCoordinates(team_one_data, team_two_data, data):
    updated_data = data.copy()
    team_one_shooter = updated_data['team-one-shooter']
    team_one_creator = updated_data['team-one-creator']
    
    team_two_shooter = updated_data['team-two-shooter']
    team_two_creator = updated_data['team-two-creator']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-court-graph":
        x = team_one_data['points'][0]['x']
        y = team_one_data['points'][0]['y']
        team_one_shooter['x'] = x
        team_one_creator['x'] = x
        team_one_shooter['y'] = y
        team_one_creator['y'] = y
        return updated_data
    
    elif triggered_input_id == "team-two-court-graph":
        x = team_two_data['points'][0]['x']
        y = team_two_data['points'][0]['y']
        team_two_shooter['x'] = x
        team_two_creator['x'] = x
        team_two_shooter['y'] = y
        team_two_creator['y'] = y
        return updated_data
    else:
        return updated_data