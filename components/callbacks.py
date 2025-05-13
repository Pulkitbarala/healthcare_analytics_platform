from dash import Input, Output, html, dcc
import plotly.express as px
from utils.data_processing import load_and_process_data
from config.settings import DATA_FILE_PATH
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Function to register callbacks
def register_callbacks(app):
    @app.callback(
        Output('graphs-container', 'children'),
        [
            Input('date-picker-range', 'start_date'),
            Input('date-picker-range', 'end_date'),
            Input('department-dropdown', 'value'),
            Input('age-group-dropdown', 'value')
        ]
    )
    def update_graphs(start_date, end_date, department, age_group):
        try:
            # Load and process data
            df = load_and_process_data(DATA_FILE_PATH)

            # Apply filters
            if start_date and end_date:
                df = df[(df['AdmissionDate'] >= start_date) & (df['DischargeDate'] <= end_date)]
            if department:
                df = df[df['Department'] == department]
            if age_group:
                age_min, age_max = map(int, age_group.split('-'))
                df = df[(df['Age'] >= age_min) & (df['Age'] <= age_max)]

            # Create a sample graph (e.g., recovery rate by department)
            fig = px.bar(df, x='Department', y='LengthOfStay', color='Outcome', barmode='group')

            return [dcc.Graph(figure=fig)]
        except Exception as e:
            logging.error(f"Error updating graphs: {e}")
            return [html.Div("An error occurred while updating the graphs.", className='text-danger')] 