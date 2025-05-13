import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.layout import create_layout
from components.callbacks import register_callbacks

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Set the layout of the app
app.layout = create_layout(app)

# Register callbacks
register_callbacks(app)

# Run the server
if __name__ == '__main__':
    app.run(debug=True) 