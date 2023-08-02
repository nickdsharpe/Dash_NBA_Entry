from maindash import app
import dash
from dash.dependencies import Input, Output

# Team One Player Dropdown callback
@app.callback(
    Output('team-one-player-dropdown-output-container', 'children'),
    Output('team-two-player-dropdown-output-container', 'children'),
    Output('store-data', 'data', allow_duplicate=True,),
    
    Input('team-one-player-dropdown', 'value'),
    Input('team-two-player-dropdown', 'value'),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamOne_UpdateShooterPlayer(team_one_value, team_two_value, data):
    updated_data = data.copy()
    
    team_one_shooter = updated_data['team-one-shooter']
    team_two_shooter = updated_data['team-two-shooter']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-player-dropdown":
        
        print('Player Selected')
        team_one_shooter['player'] = team_one_value
        
        return '', '',  updated_data
    
    elif triggered_input_id == "team-two-player-dropdown":
        
        print('Player Selected')
        team_two_shooter['player'] = team_two_value
        
        return '', '',  updated_data
    
    return '', '',  updated_data