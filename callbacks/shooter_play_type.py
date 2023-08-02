from maindash import app
import dash
from dash.dependencies import Input, Output

# Team One Play Type Dropdown callback
@app.callback(
    Output('team-one-play-type-dropdown-output-container', 'children'),
    Output('team-one', 'data', allow_duplicate=True,),
    
    Input('team-one-play-type-dropdown', 'value'),
    Input('team-one', 'data'),
    prevent_initial_call=True
)
def UpdateShooterPlayType(value, data):
    updated_data = data.copy()
    
    shooter = updated_data['shooter']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-play-type-dropdown":
        
        print('Play Type Selected')
        shooter['play_type'] = value
        return '', updated_data

    
    return '', updated_data



# Team Two Play Type Dropdown callback
@app.callback(
    Output('team-two-play-type-dropdown-output-container', 'children'),
    Output('team-two', 'data', allow_duplicate=True,),
    
    Input('team-two-play-type-dropdown', 'value'),
    Input('team-two', 'data'),
    prevent_initial_call=True
)
def UpdateShooterPlayType(value, data):
    updated_data = data.copy()
    
    shooter = updated_data['shooter']
    
    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-two-play-type-dropdown":
        
        print('Play Type Selected')
        shooter['play_type'] = value
        return '', updated_data

    
    return '', updated_data