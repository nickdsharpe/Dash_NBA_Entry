import dash
from dash import html
from dash.dependencies import Input, Output
import dash_daq as daq
from entry_from import ToggleSwitch, PlayerDropdown
from court import draw_plotly_court
import plotly.express as px
import plotly.graph_objects as go

fig = go.Figure()

# Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    children=[
        html.H2("PPP Entry Form"),
        html.Div(draw_plotly_court(fig), id='court-container'),
        html.Div(id='click-coordinates'),
        ToggleSwitch(),
        PlayerDropdown(),
        html.Div(id='shot-switch-result')
    ]
)

# Make or Miss Toggle callback


@app.callback(
    Output("shot-switch-result", "children"),
    [Input("shot-switch", "value")]
)
# Make or Miss Toggle switch logic
def update_shot_result(value):
    if value:
        return "Miss"
    else:
        return "Make"

# Player Dropdown callback


@app.callback(
    Output('player-dropdown-output-container', 'children'),
    Input('player-dropdown', 'value')
)
# Player Dropdown logic
def update_output(value):
    return f'You have selected {value}'

# Callback to draw the court plot


@app.callback(
    Output('court-graph', 'children'),
    Input('shot-switch', 'value')
)
def draw_court(value):
    fig = go.Figure()
    court_plot = draw_plotly_court(fig)
    return court_plot

# Callback to track click events and record coordinates


@app.callback(
    Output('click-coordinates', 'children'),
    Input('court-graph', 'clickData')
)
def record_coordinates(clickData):
    if clickData is not None:
        x = clickData['points'][0]['x']
        y = clickData['points'][0]['y']
        return f'Shot coordinates: ({x}, {y})'
    else:
        return ''


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
