from maindash import app
import dash
from dash.dependencies import Input, Output

# Free Throws made callback
@app.callback(
    Output('store-data', 'data', allow_duplicate=True),
    Input("team-one-free-throw-input", "value"),
    Input("team-two-free-throw-input", "value"),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamOne_UpdateFreeThrows(team_one_value, team_two_value,  data):
    updated_data = data.copy()
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-free-throw-input":
        team_one_shooter = updated_data['team-one-shooter']
        team_one_creator = updated_data['team-one-creator']
        team_one_shooter['ftm'] = team_one_value
        team_one_creator['ftm'] = team_one_value
        return updated_data
    
    if triggered_input_id == "team-two-free-throw-input":
        team_two_shooter = updated_data['team-two-shooter']
        team_two_creator = updated_data['team-two-creator']
        team_two_shooter['ftm'] = team_two_value
        team_two_creator['ftm'] = team_two_value
        return updated_data
    
    return updated_data