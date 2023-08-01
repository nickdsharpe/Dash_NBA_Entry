from maindash import app
import dash
from dash.dependencies import Input, Output

## TEAM ONE ###
# Make | Miss | Free Throws | And-1 | Turnover checklist callback
@app.callback(
    Output('team-one-free-throw-input-container', 'style'),
    Output('team-two-free-throw-input-container', 'style'),
    Output('store-data', 'data', allow_duplicate=True),
    Input("team-one-shot-checklist", "value"),
    Input("team-two-shot-checklist", "value"),
    Input('store-data', 'data'),
    prevent_initial_call=True
)
def team_one_update_shot_result(team_one_value, team_two_value, data):
    updated_data = data.copy()
    
    team_one_shooter = updated_data['team-one-shooter']
    team_one_creator = updated_data['team-one-creator']
    
    team_two_shooter = updated_data['team-two-shooter']
    team_two_creator = updated_data['team-two-creator']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-shot-checklist":
        if team_one_value == ['Miss']:
            team_one_shooter['result'] = 0
            team_one_creator['result'] = 0
            return {'display': 'none'}, {'display': 'none'}, updated_data
        elif team_one_value == ['Make']:
            team_one_shooter['result'] = 1
            team_one_creator['result'] = 1
            return {'display': 'none'}, {'display': 'none'}, updated_data
        elif team_one_value == ['Free Throws']:
            team_one_shooter['result'] = 11
            team_one_creator['result'] = 11
            return {'display': 'block'}, {'display': 'none'}, updated_data
        elif team_one_value == ['And-1']:
            team_one_shooter['result'] = 30
            team_one_creator['result'] = 30
            return {'display': 'block'}, {'display': 'none'}, updated_data
        elif team_one_value == ['Turnover']:
            team_one_shooter['result'] = 20
            team_one_creator['result'] = 20
            return {'display': 'none'}, {'display': 'none'}, updated_data
    if triggered_input_id == "team-two-shot-checklist":
        if team_two_value == ['Miss']:
            team_two_shooter['result'] = 0
            team_two_creator['result'] = 0
            return {'display': 'none'}, {'display': 'none'}, updated_data
        elif team_two_value == ['Make']:
            team_two_shooter['result'] = 1
            team_two_creator['result'] = 1
            return {'display': 'none'}, {'display': 'none'}, updated_data
        elif team_two_value == ['Free Throws']:
            team_two_shooter['result'] = 11
            team_two_creator['result'] = 11
            return {'display': 'none'}, {'display': 'block'}, updated_data
        elif team_two_value == ['And-1']:
            team_two_shooter['result'] = 30
            team_two_creator['result'] = 30
            return {'display': 'none'}, {'display': 'block'},  updated_data
        elif team_two_value == ['Turnover']:
            team_two_shooter['result'] = 20
            team_two_creator['result'] = 20
            return {'display': 'none'}, {'display': 'none'}, updated_data
    
    return {'display': 'none'}, {'display': 'none'}, updated_data