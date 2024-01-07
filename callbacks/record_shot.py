from maindash import app
import dash
from dash import no_update
from dash.dependencies import Input, Output
from assets.update_defender_data import UpdateDefenderDF
from assets.update_shooter_data import UpdateShooterDF
from assets.update_creator_data import UpdateCreatorDF

# Record shot callback
@app.callback(
    Output("team-one-record-shot-output", "children"),
    Output("team-two-record-shot-output", "children"),
    Output('shot-type', 'data', allow_duplicate=True),
    Output('shot-result', 'data', allow_duplicate=True),
    Output('play-type', 'data', allow_duplicate=True),
    Output('player', 'data', allow_duplicate=True),
    Output('defender', 'data', allow_duplicate=True),
    Output('shot-coordinates', 'data', allow_duplicate=True),
    Output('shot-quality', 'data', allow_duplicate=True),
    Output('free-throws', 'data', allow_duplicate=True),
    Output('shot-zone', 'data', allow_duplicate=True),
    Output('defender-type', 'data', allow_duplicate=True),
    Output('steals-blocks', 'data', allow_duplicate=True),
    Output('clear-components-flag', 'data', allow_duplicate=True),
    
    Input("team-one-record-shot-button", "n_clicks"),
    Input("team-two-record-shot-button", "n_clicks"),
    Input('game-id', 'data'),
    Input('team-ids', 'data'),
    Input('shot-type', 'data'),
    Input('shot-result', 'data'),
    Input('play-type', 'data'),
    Input('player', 'data'),
    Input('defender', 'data'),
    Input('shot-coordinates', 'data'),
    Input('shot-quality', 'data'),
    Input('free-throws', 'data'),
    Input('shot-zone', 'data'),
    Input('defender-type', 'data'),
    Input('steals-blocks', 'data'),
    
    prevent_initial_call=True,
)
def teamOne_RecordShot(team_one_n_clicks, team_two_n_clicks, game_id, team_ids, shot_type, shot_result, play_type, player, defender, shot_coordinates, shot_quality, free_throws, shot_zone, defender_type, steals_blocks):

    cleared = [{}, {}]
    none_cleared = [{'shooter': None}, {'shooter': None}]
    poa_reset = [{'shooter': 'POA'}, {'shooter': 'POA'}]
    
    game_id = game_id.copy()
    shot_type = shot_type.copy()
    shot_result = shot_result.copy()
    play_type = play_type.copy()
    player = player.copy()
    defender = defender.copy()
    shot_coordinates = shot_coordinates.copy()
    shot_quality = shot_quality.copy()
    free_throws = free_throws.copy()
    shot_zone = shot_zone.copy()
    defender_type = defender_type.copy()
    steals_blocks = steals_blocks.copy()

    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Team One
    if triggered_input_id == "team-one-record-shot-button" and team_one_n_clicks is not None:
        print(len(player[0].keys()))
        event_list = [game_id[0]['id'], player[0]['shooter']]
        print(event_list)

        return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, poa_reset, none_cleared, False
    
    # Team Two
    if triggered_input_id == "team-two-record-shot-button" and team_two_n_clicks is not None:

        return None, 'Shot Recorded', cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, cleared, poa_reset, none_cleared, True
    
    
    return None, '', no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, no_update, False