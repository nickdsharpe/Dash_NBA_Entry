import dash
import dash_bootstrap_components as dbc

# Dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], 
                suppress_callback_exceptions=True,
                prevent_initial_callbacks="initial_duplicate")