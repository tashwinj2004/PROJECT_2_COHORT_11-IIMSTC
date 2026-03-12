import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

"""
PROJECT: Disaster Relief Allocation ML
MODULE: Data Cleaning & Preprocessing
AUTHOR: [Your Name]
COLLABORATOR: Gemini (AI Assistant)
DATE: March 12, 2026
"""

def clean_disaster_data(input_path, output_path):
    print(f"--- Starting Data Cleaning Pipeline (Assisted by Gemini) ---")
    
    # 1. Load Dataset
    df = pd.read_csv(input_path)
    
    # 2. Handling Missing Values (Critical for Disaster Relief)
    # We use median for numericals to avoid outlier bias
    numerical_cols = ['population_density', 'infrastructure_damage', 'urgency_score']
    for col in numerical_cols:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
    
    # 3. Categorical Encoding
    # Converting 'Urban' vs 'Rural' to a binary format the ML model can read
    if 'location_type' in df.columns:
        df['is_urban'] = df['location_type'].map({'Urban': 1, 'Rural': 0})
        df.drop(columns=['location_type'], inplace=True)

    # 4. Feature Scaling (Normalization)
    # Scales values to a [0, 1] range to ensure no feature dominates the model
    scaler = MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # 5. Logic Validation
    # Removing any entries where coordinates might be missing or corrupted
    df = df.dropna(subset=['latitude', 'longitude'])
    
    # 6. Export Cleaned Data
    df.to_csv(output_path, index=False)
    print(f"--- Success: Cleaned data saved to {output_path} ---")

if __name__ == "__main__":
    # Example execution
    # clean_disaster_data('raw_disaster_reports.csv', 'cleaned_relief_allocation.csv')
    pass