from dash import dcc, html
import dash_bootstrap_components as dbc

# Add a Navbar for better navigation
navbar = dbc.NavbarSimple(
    brand='Healthcare Analytics Platform',
    brand_href='#',
    color='primary',
    dark=True,
    className='mb-4'
)

# Function to create the layout of the dashboard
def create_layout(app):
    return dbc.Container([
        navbar,  # Include the Navbar at the top
        dbc.Row([
            dbc.Col([
                html.H4('Filters', className='mt-4'),
                html.P('Use the filters below to refine the data displayed in the graphs.', className='text-muted'),
                dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date_placeholder_text='Start Period',
                    end_date_placeholder_text='End Period'
                ),
                html.H5('Department'),
                dcc.Dropdown(
                    id='department-dropdown',
                    options=[
                        {'label': 'Cardiology', 'value': 'cardiology'},
                        {'label': 'Neurology', 'value': 'neurology'},
                        {'label': 'Oncology', 'value': 'oncology'}
                    ],
                    placeholder='Select a department'
                ),
                html.H5('Age Group'),
                dcc.Dropdown(
                    id='age-group-dropdown',
                    options=[
                        {'label': '0-18', 'value': '0-18'},
                        {'label': '19-35', 'value': '19-35'},
                        {'label': '36-50', 'value': '36-50'},
                        {'label': '51+', 'value': '51+'}
                    ],
                    placeholder='Select age group'
                ),
            ], width=3, className='sidebar'),
            dbc.Col([
                html.Div(id='graphs-container', className='content')
            ], width=9)
        ])
    ], fluid=True) 