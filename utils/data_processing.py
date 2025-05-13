import pandas as pd

# Function to load and process patient data
def load_and_process_data(file_path):
    # Load data
    df = pd.read_csv(file_path)
    print(df.head())  # Add this line to print the first few rows of the DataFrame
    
    # Process data (placeholder for actual processing logic)
    df['LengthOfStay'] = (pd.to_datetime(df['DischargeDate']) - pd.to_datetime(df['AdmissionDate'])).dt.days
    
    return df 