import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

def load_and_clean(file_path):
    df = pd.read_csv(file_path)
    
    # 1. Identify Time
    possible_time_cols = ['Time', 'Date', 'DateTime', 'timestamp']
    time_col = next((col for col in df.columns if col in possible_time_cols), df.columns[0])
    df['Time_Clean'] = pd.to_datetime(df[time_col])
    
    # 2. Identify Glucose columns (Case-insensitive search)
    libre_col = [c for c in df.columns if 'Libre' in c][0]
    dexcom_col = [c for c in df.columns if 'Dexcom' in c][0]

    # 3. Cleaning
    df['Libre_Raw'] = df[libre_col] # Keep raw for the 'gray' line in plot
    df['Libre_Clean'] = df[libre_col].interpolate(method='linear')
    df['Dexcom_Clean'] = df[dexcom_col].interpolate(method='linear')
    
    # Apply filter
    df['Libre_Smooth'] = savgol_filter(df['Libre_Clean'], window_length=11, polyorder=2)
    
    return df, dexcom_col, libre_col