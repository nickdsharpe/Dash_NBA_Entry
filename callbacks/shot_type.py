from maindash import app
from dash.dependencies import Input, Output
from assets.court import is_inside_three_point_line

# Team One Callback to handle shot type
@app.callback(
        Output('team-one-shot-type', 'children'),
        Output('store-data', 'data', allow_duplicate=True),
        Input('team-one-court-graph', 'clickData'),
        Input('store-data', 'data'),
        prevent_initial_call=True
    )
def teamOne_HandleShotType(click_data, data):
    updated_data = data.copy()
    shooter = updated_data['team-one-shooter']
    creator = updated_data['team-one-creator']
    
    if is_inside_three_point_line(click_data):
        shooter['shot_type'] = '2pt FG'
        creator['shot_type'] = '2pt FG'
        return '2pt FG', updated_data
    else:
        shooter['shot_type'] = '3pt FG'
        creator['shot_type'] = '3pt FG'
        return '3pt FG', updated_data
    
# Team Two Callback to handle shot type
@app.callback(
        Output('team-two-shot-type', 'children'),
        Output('store-data', 'data', allow_duplicate=True),
        Input('team-two-court-graph', 'clickData'),
        Input('store-data', 'data'),
        prevent_initial_call=True
    )
def teamTwo_HandleShotType(click_data, data):
    updated_data = data.copy()
    shooter = updated_data['team-two-shooter']
    creator = updated_data['team-two-creator']
    
    if is_inside_three_point_line(click_data):
        shooter['shot_type'] = '2pt FG'
        creator['shot_type'] = '2pt FG'
        return '2pt FG', updated_data
    else:
        shooter['shot_type'] = '3pt FG'
        creator['shot_type'] = '3pt FG'
        return '3pt FG', updated_data
