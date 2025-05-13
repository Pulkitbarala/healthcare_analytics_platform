import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of records
num_records = 10000

# Generate synthetic data
data = {
    'PatientID': np.arange(1, num_records + 1),
    'Age': np.random.randint(0, 100, num_records),
    'Gender': np.random.choice(['M', 'F'], num_records),
    'Diagnosis': np.random.choice(['Flu', 'Diabetes', 'Cancer'], num_records),
    'AdmissionDate': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_records)],
    'DischargeDate': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_records)],
    'Outcome': np.random.choice(['Recovered', 'Deceased'], num_records),
    'Department': np.random.choice(['Cardiology', 'Neurology', 'Oncology'], num_records)
}

# Create a DataFrame
large_df = pd.DataFrame(data)

# Ensure DischargeDate is after AdmissionDate
large_df['DischargeDate'] = large_df.apply(
    lambda row: fake.date_between(start_date=row['AdmissionDate'], end_date='today'), axis=1
)

# Save to CSV
large_df.to_csv('data/large_sample_patients.csv', index=False)

print("Large dataset created and saved to 'data/large_sample_patients.csv'") 