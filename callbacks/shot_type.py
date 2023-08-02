from maindash import app
import dash
from dash import no_update
from dash_extensions.enrich import Dash, Input, State, Output, html, dcc
from dash.exceptions import PreventUpdate
from assets.court import is_inside_three_point_line

@app.callback(
        Output('team-one-shot-type', 'children'),
        Output('team-one', 'data'),
        
        Input('team-one-court-graph', 'clickData'),
        Input('team-one', 'data'),
    prevent_initial_call=True
)
def handle_shot_type(clickData, data):
    updated_data = data.copy()
    
    if clickData is None:
        return no_update, no_update

    # Team One
    if dash.callback_context.triggered_id == 'team-one-court-graph.clickData':
        shooter = updated_data['shooter']
        creator = updated_data['creator']
        if is_inside_three_point_line(clickData):
            print('Shot Type Recorded')
            shooter['shot_type'] = '2pt FG'
            creator['shot_type'] = '2pt FG'
            shot_type = '2pt FG'
        else:
            print('Shot Type Recorded')
            shooter['shot_type'] = '3pt FG'
            creator['shot_type'] = '3pt FG'
            shot_type = '3pt FG'
        
        return shot_type, updated_data
    
    return no_update, no_update




@app.callback(
        Output('team-two-shot-type', 'children'),
        Output('team-two', 'data'),
        
        Input('team-two-court-graph', 'clickData'),
        Input('team-two', 'data'),
    prevent_initial_call=True
)
def handle_shot_type(clickData, data):
    updated_data = data.copy()
    
    if clickData is None:
        return no_update, no_update

    # Team two
    if dash.callback_context.triggered[0]['prop_id'] == 'team-two-court-graph.clickData':
        shooter = updated_data['shooter']
        creator = updated_data['creator']
        if is_inside_three_point_line(clickData):
            print('Shot Type Recorded')
            shooter['shot_type'] = '2pt FG'
            creator['shot_type'] = '2pt FG'
            shot_type = '2pt FG'
        else:
            print('Shot Type Recorded')
            shooter['shot_type'] = '3pt FG'
            creator['shot_type'] = '3pt FG'
            shot_type = '3pt FG'
        
        return shot_type, updated_data
    
    return no_update, no_update

    
