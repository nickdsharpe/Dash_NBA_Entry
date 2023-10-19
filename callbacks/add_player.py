from maindash import app
import dash
from dash.dependencies import Input, Output, State
from dash import no_update

# Controls whether or not the add player input is displayed
@app.callback(
    Output('team-one-add-player-input-container', 'style'),
    Output('team-two-add-player-input-container', 'style'),
    Output('team-one-add-player-checklist', 'value'),
    Output('team-two-add-player-checklist', 'value'),
    
    Input('team-one-add-player-checklist', 'value'),
    Input('team-two-add-player-checklist', 'value'),
    
    Input('team-one-add-player-input-button', 'n_clicks'),
    Input('team-two-add-player-input-button', 'n_clicks'),
    
    prevent_initial_call=True
)
def HandleStyle(team_one_check, team_two_check, team_one_button, team_two_button):

    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Display Add PLayer Input if Checked
    if triggered_input_id == "team-one-add-player-checklist":
        
        if team_one_check:
            return {'display': 'block'}, {'display': 'none'}, no_update, no_update
        else:
            return {'display': 'none'}, {'display': 'none'}, no_update, no_update
    
    if triggered_input_id == "team-two-add-player-checklist":
        
        if team_two_check:
            return {'display': 'none'}, {'display': 'block'}, no_update, no_update
        else:
            return {'display': 'none'}, {'display': 'none'}, no_update, no_update
        
    # Remove Display if Add Player Button is Clicked    
    if triggered_input_id == "team-one-add-player-input-button":
        
        return {'display': 'none'}, no_update, [], no_update
    
    if triggered_input_id == "team-two-add-player-input-button":
        
        return no_update, {'display': 'none'}, no_update, []
    
    return no_update




@app.callback(
    Output('team-one-player-dropdown', 'options', allow_duplicate=True),
    Output('team-two-player-dropdown', 'options', allow_duplicate=True),
    
    State('team-one-add-player-input', 'value'),
    State('team-two-add-player-input', 'value'),
    
    State('team-one-player-dropdown', 'options'),
    State('team-two-player-dropdown', 'options'),
    
    Input('team-one-add-player-input-button', 'n_clicks'),
    Input('team-two-add-player-input-button', 'n_clicks'),
    
    prevent_initial_call=True
)
def AddPlayerToTeam(team_one_player, team_two_player, team_one_roster, team_two_roster, team_one_click, team_two_click):

    ctx = dash.callback_context
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_input_id == "team-one-add-player-input-button":
        
        if team_one_player not in team_one_roster:
            
            team_one_roster.append(team_one_player)
        
            return team_one_roster, team_two_roster
        
    if triggered_input_id == "team-two-add-player-input-button":
        
        if team_two_player not in team_two_roster:
            
            team_two_roster.append(team_two_player)
        
            return team_one_roster, team_two_roster
    
    return no_update