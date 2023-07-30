from maindash import app
from dash.dependencies import Input, Output

# Team One Play Type Dropdown callback
@app.callback(
    Output('team-one-play-type-dropdown-output-container', 'children'),
    Output('store-data', 'data', allow_duplicate=True,),
    Input('team-one-play-type-dropdown', 'value'),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamOne_UpdateShooterPlayType(value, data):
    updated_data = data.copy()
    shooter = updated_data['team-one-shooter']
    shooter['play_type'] = value
    return '', updated_data

# Team Tne Play Type Dropdown callback
@app.callback(
    Output('team-two-play-type-dropdown-output-container', 'children'),
    Output('store-data', 'data', allow_duplicate=True,),
    Input('team-two-play-type-dropdown', 'value'),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamTwo_UpdateShooterPlayType(value, data):
    updated_data = data.copy()
    shooter = updated_data['team-two-shooter']
    shooter['play_type'] = value
    return '', updated_data