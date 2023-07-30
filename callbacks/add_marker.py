from maindash import app
import dash
from layout import make_layout
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import json

with open('assets/initial_state.json', "r") as file:
    initial_state = json.load(file)

# Callback to handle click events and update the scatter trace with markers
@app.callback(
    Output('team-one-court-graph', 'figure'),
    Input('team-one-court-graph', 'clickData'),
    Input("team-one-clear-shot-button", "n_clicks"),
    [Input("team-one-record-shot-button", "n_clicks")],
    State('team-one-court-graph', 'figure'),
    prevent_initial_call=True,
    allow_duplicate=True
)
def team_one_add_marker(clickData, n_clicks, rec_n_clicks, figure):
    ctx = dash.callback_context
    # If the clear button is clicked, remove the marker trace
    if (ctx.triggered[0]['prop_id'] == "team-one-clear-shot-button.n_clicks") or (ctx.triggered[0]['prop_id'] == "team-one-record-shot-button.n_clicks"):
        figure['data'] = initial_state
    else:
        if clickData:
            x = clickData['points'][0]['x']
            y = clickData['points'][0]['y']
            # Remove all marker traces from the figure
            figure['data'] = [trace for trace in figure['data'] if trace['mode'] != 'markers']

            # Create a new marker trace
            new_marker_trace = go.Scatter(
                x=[x],
                y=[y],
                mode="markers",
                marker=dict(
                    color='#4fafa9',
                    size=18,
                    opacity=0.9,
                    symbol='x',
                ),
                hoverinfo='none'
            )

            # Add the new marker trace to the figure
            figure['data'].append(new_marker_trace)

            # Update the layout to enable click events again
            figure['layout']['clickmode'] = 'event+select'

    return figure

# Callback to handle click events and update the scatter trace with markers
@app.callback(
    Output('team-two-court-graph', 'figure'),
    Input('team-two-court-graph', 'clickData'),
    Input("team-two-clear-shot-button", "n_clicks"),
    [Input("team-two-record-shot-button", "n_clicks")],
    State('team-two-court-graph', 'figure'),
    prevent_initial_call=True,
    allow_duplicate=True
)
def team_two_add_marker(clickData, n_clicks, rec_n_clicks, figure):
    ctx = dash.callback_context
    
    # If the clear button is clicked, remove the marker trace
    if (ctx.triggered[0]['prop_id'] == "team-two-clear-shot-button.n_clicks") or (ctx.triggered[0]['prop_id'] == "team-two-record-shot-button.n_clicks"):
        figure['data'] = initial_state
    else:
        if clickData:
            x = clickData['points'][0]['x']
            y = clickData['points'][0]['y']

            # Remove all marker traces from the figure
            figure['data'] = [trace for trace in figure['data'] if trace['mode'] != 'markers']

            # Create a new marker trace
            new_marker_trace = go.Scatter(
                x=[x],
                y=[y],
                mode="markers",
                marker=dict(
                    color='#b465f7',
                    size=18,
                    opacity=0.9,
                    symbol='x',
                ),
                hoverinfo='none'
            )

            # Add the new marker trace to the figure
            figure['data'].append(new_marker_trace)

            # Update the layout to enable click events again
            figure['layout']['clickmode'] = 'event+select'

    return figure