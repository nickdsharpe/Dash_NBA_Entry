from maindash import app
import dash
from dash.dependencies import Input, Output

## TEAM ONE ###
# Make | Miss | Free Throws | And-1 | Turnover checklist callback
@app.callback(
    Output('team-one-free-throw-input-container', 'style'),
    Output('team-one', 'data'),
    
    Input("team-one-shot-checklist", "value"),
    Input('team-one', 'data'),
    prevent_initial_call=True
)
def team_one_update_shot_result(value, data):
    updated_data = data.copy()
    
    shooter = updated_data['shooter']
    creator = updated_data['creator']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-shot-checklist":
        print('Shot result recorded')
        if value == ['Miss']:
            shooter['result'] = 0
            creator['result'] = 0
            return {'display': 'none'},  updated_data
        
        elif value == ['Make']:
            print('Shot Result Receorded')
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



## TEAM Two ###
# Make | Miss | Free Throws | And-1 | Turnover checklist callback
@app.callback(
    Output('team-two-free-throw-input-container', 'style'),
    Output('team-two', 'data'),
    
    Input("team-two-shot-checklist", "value"),
    Input('team-two', 'data'),
    prevent_initial_call=True
)
def team_two_update_shot_result(value, data):
    updated_data = data.copy()
    
    shooter = updated_data['shooter']
    creator = updated_data['creator']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-two-shot-checklist":
        print('Shot result recorded')
        if value == ['Miss']:
            shooter['result'] = 0
            creator['result'] = 0
            return {'display': 'none'},  updated_data
        
        elif value == ['Make']:
            print('Shot Result Receorded')
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