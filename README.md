# Healthcare Analytics Platform

This project is designed to help healthcare providers track patient outcomes and optimize resource allocation through interactive data visualizations and dashboards.

## Features
- Visualizations of patient outcomes (e.g., recovery rate, mortality rate, readmission rate, average length of stay)
- Resource utilization charts (e.g., bed occupancy rate, available vs. occupied ICU beds, staff allocation)
- Filters for date ranges, departments, and patient demographics (e.g., age group, gender, diagnosis)
- Responsive layout with sidebar navigation and clear, user-friendly UI components

## Tech Stack
- **Python** for backend and data processing
- **Dash** for interactive web application interface
- **Pandas** for data analysis and transformation

## Setup Instructions
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the app using `python app.py`.

## Project Structure
```
healthcare_analytics_platform/
├── app.py
├── assets/
│   └── styles.css
├── components/
│   ├── layout.py
│   └── callbacks.py
├── data/
│   ├── sample_patients.csv
│   └── processed_data.pkl
├── utils/
│   └── data_processing.py
├── config/
│   └── settings.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Generating a Large Dataset
To generate a large synthetic dataset for testing purposes, you can use the `generate_large_dataset.py` script located in the `utils` directory. This script creates a CSV file with 10,000 synthetic patient records.

### Steps to Generate the Dataset
1. Navigate to the `healthcare_analytics_platform` directory in your terminal.
2. Run the following command to execute the script:
   ```
   python utils/generate_large_dataset.py
   ```
3. The generated dataset will be saved as `large_sample_patients.csv` in the `data` directory.

This dataset can be used to test the performance and scalability of the Healthcare Analytics Platform. 