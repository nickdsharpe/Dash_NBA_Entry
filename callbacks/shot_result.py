from maindash import app
from dash.dependencies import Input, Output

## TEAM ONE ###
# Make | Miss | Free Throws | And-1 | Turnover checklist callback
@app.callback(
    Output('team-one-free-throw-input-container', 'style'),
    Output('store-data', 'data', allow_duplicate=True),
    Input("team-one-shot-checklist", "value"),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def team_one_update_shot_result(value, data):
    
    updated_data = data.copy()
    print(updated_data)
    shooter = updated_data['team-one-shooter']
    creator = updated_data['team-one-creator']
    if value == ['Miss']:
        shooter['result'] = 0
        creator['result'] = 0
        return {'display': 'none'}, updated_data
    elif value == ['Make']:
        shooter['result'] = 1
        creator['result'] = 1
        return {'display': 'none'}, updated_data
    elif value == ['Free Throws']:
        shooter['result'] = 11
        creator['result'] = 11
        return {'display': 'block'}, updated_data
    elif value == ['And-1']:
        shooter['result'] = 30
        creator['result'] = 30
        return {'display': 'block'}, updated_data
    elif value == ['Turnover']:
        shooter['result'] = 20
        creator['result'] = 20
        return {'display': 'none'}, updated_data
    
    return {'display': 'none'}, updated_data
    
 ### TEAM TWO ###
@app.callback(
    Output('team-two-free-throw-input-container', 'style'),
    Output('store-data', 'data', allow_duplicate=True),
    Input("team-two-shot-checklist", "value"),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def team_two_update_shot_result(value, data):
    
    updated_data = data.copy()
    shooter = updated_data['team-two-shooter']
    creator = updated_data['team-two-creator']
    if value == ['Miss']:
        shooter['result'] = 0
        creator['result'] = 0
        return {'display': 'none'}, updated_data
    elif value == ['Make']:
        shooter['result'] = 1
        creator['result'] = 1
        return {'display': 'none'}, updated_data
    elif value == ['Free Throws']:
        shooter['result'] = 11
        creator['result'] = 11
        return {'display': 'block'}, updated_data
    elif value == ['And-1']:
        shooter['result'] = 30
        creator['result'] = 30
        return {'display': 'block'}, updated_data
    elif value == ['Turnover']:
        shooter['result'] = 20
        creator['result'] = 20
        return {'display': 'none'}, updated_data
    
    return {'display': 'none'}, updated_data
   
    