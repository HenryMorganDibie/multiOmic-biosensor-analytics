import numpy as np

def calculate_advanced_metrics(df, dex_name):
    # Ensure we only compare valid, non-zero data points
    valid_mask = (df[dex_name] > 0) & (df['Libre_Smooth'] > 0)
    ref = df.loc[valid_mask, dex_name]
    sen = df.loc[valid_mask, 'Libre_Smooth']
    
    # 1. MARD (Standard Accuracy)
    mard = np.abs(sen - ref).mean() / ref.mean() * 100
    
    # 2. SNR (Signal to Noise Ratio)
    noise = df['Libre_Raw'] - df['Libre_Smooth']
    snr = 10 * np.log10(np.var(sen) / np.var(noise)) if np.var(noise) > 0 else 0
    
    # 3. Time Lag (Response Time)
    # Finds the shift (in 5-min increments) where the signals align best
    correlation = np.correlate(sen - sen.mean(), ref - ref.mean(), mode='full')
    lag_idx = np.argmax(correlation) - (len(sen) - 1)
    lag_mins = lag_idx * 5  
    
    # 4. Hysteresis (Directional Bias)
    # Measures if the error is different during 'Glucose Rising' vs 'Glucose Falling'
    df_diff = df[dex_name].diff()
    rising = df_diff > 0
    falling = df_diff < 0
    
    error_rising = (sen[rising] - ref[rising]).mean()
    error_falling = (sen[falling] - ref[falling]).mean()
    hysteresis = np.abs(error_rising - error_falling)
    
    # 5. Baseline Drift (Stability over time)
    split = int(len(ref) * 0.1)
    drift = (sen.iloc[-split:] - ref.iloc[-split:]).mean() - (sen.iloc[:split] - ref.iloc[:split:]).mean()

    return {
        "MARD": mard, 
        "SNR": snr, 
        "Lag_Mins": lag_mins, 
        "Hysteresis": hysteresis,
        "Drift": drift
    }