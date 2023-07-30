from maindash import app
from dash.dependencies import Input, Output

# Free Throws made callback
@app.callback(
    Output('store-data', 'data', allow_duplicate=True),
    Input("team-one-free-throw-input", "value"),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamOne_UpdateFreeThrows(value, data):
    updated_data = data.copy()
    shooter = updated_data['team-one-shooter']
    creator = updated_data['team-one-creator']
    shooter['ftm'] = value
    creator['ftm'] = value
    return updated_data

# Free Throws made callback
@app.callback(
    Output('store-data', 'data', allow_duplicate=True),
    Input("team-two-free-throw-input", "value"),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def teamTwo_UpdateFreeThrows(value, data):
    updated_data = data.copy()
    shooter = updated_data['team-two-shooter']
    creator = updated_data['team-two-creator']
    shooter['ftm'] = value
    creator['ftm'] = value
    return updated_data
