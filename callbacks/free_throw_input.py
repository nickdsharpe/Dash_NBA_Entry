from maindash import app
import dash
from dash.dependencies import Input, Output

# Free Throws made callback
@app.callback(
    Output('free-throws', 'data', allow_duplicate=True),
    
    Input("team-one-free-throw-input", "value"),
    Input("team-two-free-throw-input", "value"),
    Input('free-throws', 'data'),
    prevent_initial_call=True
)
def teamOne_UpdateFreeThrows(team_one_value, team_two_value,  data):
    updated_data = data.copy()
    
    team_one = updated_data['team-one']
    team_two = updated_data['team-two']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-free-throw-input":
        
        print('Free Throws Recorded')
        team_one['shooter'] = team_one_value
        team_one['creator'] = team_one_value
        print(updated_data)
        return updated_data
    
    if triggered_input_id == "team-two-free-throw-input":
        
        print('Free Throws Recorded')
        team_two['shooter'] = team_two_value
        team_two['creator'] = team_two_value
        print(updated_data)
        return updated_data
    
    return updated_data