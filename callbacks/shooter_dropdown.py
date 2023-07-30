from maindash import app
from dash.dependencies import Input, Output

# Team One Player Dropdown callback
@app.callback(
    Output('team-one-player-dropdown-output-container', 'children'),
    Output('store-data', 'data', allow_duplicate=True,),
    Input('team-one-player-dropdown', 'value'),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamOne_UpdateShooterPlayer(value, data):
    updated_data = data.copy()
    shooter = updated_data['team-one-shooter']
    shooter['player'] = value
    return '', updated_data

# Team Two Player Dropdown
@app.callback(
    Output('team-two-player-dropdown-output-container', 'children'),
    Output('store-data', 'data', allow_duplicate=True,),
    Input('team-two-player-dropdown', 'value'),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamTwo_UpdateShooterPlayer(value, data):
    updated_data = data.copy()
    shooter = updated_data['team-two-shooter']
    shooter['player'] = value
    return '', updated_data