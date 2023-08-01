from maindash import app
import dash
from dash.dependencies import Input, Output
from assets.court import is_inside_three_point_line

@app.callback(
        Output('team-one-shot-type', 'children'),
        Output('team-two-shot-type', 'children'),
        Output('store-data', 'data', allow_duplicate=True),
        Input('team-one-court-graph', 'clickData'),
        Input('team-two-court-graph', 'clickData'),
        Input('store-data', 'data'),
    prevent_initial_call=True
)
def handle_shot_type(click_data_team_one, click_data_team_two, data):
    updated_data = data.copy()

    # Team One
    if dash.callback_context.triggered[0]['prop_id'] == 'team-one-court-graph.clickData':
        shooter = updated_data['team-one-shooter']
        creator = updated_data['team-one-creator']
        if is_inside_three_point_line(click_data_team_one):
            shooter['shot_type'] = '2pt FG'
            creator['shot_type'] = '2pt FG'
            team_one_shot_type = '2pt FG'
        else:
            shooter['shot_type'] = '3pt FG'
            creator['shot_type'] = '3pt FG'
            team_one_shot_type = '3pt FG'
        
        return team_one_shot_type, None, updated_data

    # Team Two
    elif dash.callback_context.triggered[0]['prop_id'] == 'team-two-court-graph.clickData':
        shooter = updated_data['team-two-shooter']
        creator = updated_data['team-two-creator']
        if is_inside_three_point_line(click_data_team_two):
            shooter['shot_type'] = '2pt FG'
            creator['shot_type'] = '2pt FG'
            team_two_shot_type = '2pt FG'
        else:
            shooter['shot_type'] = '3pt FG'
            creator['shot_type'] = '3pt FG'
            team_two_shot_type = '3pt FG'
        
        return None, team_two_shot_type, updated_data

    # No callback triggered, return default values
    return None, None, updated_data
