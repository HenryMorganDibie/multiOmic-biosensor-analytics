import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_microbe_drivers():
    # Load the integrated report we just created
    df = pd.read_csv("results/final_integrated_clinical_report.csv")
    
    # Identify microbe columns (they are the ones from microbes.csv)
    # Usually, these start after the 'Microbiome-Induced Stress' column or similar
    # For this script, we'll take all columns that were in microbes.csv
    microbe_data = pd.read_csv("data/raw/CGMacros/microbes.csv")
    microbe_cols = [col for col in microbe_data.columns if col != 'subject']
    
    # Prepare X (Microbes) and y (Sensor Accuracy - MARD)
    # Drop rows where MARD or microbes are NaN
    temp_df = df.dropna(subset=['MARD'] + microbe_cols)
    X = temp_df[microbe_cols]
    y = temp_df['MARD']
    
    # Train a quick model to find "Importance"
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Get Top 10 Microbes that predict Sensor Accuracy
    importances = pd.DataFrame({
        'Microbe': microbe_cols,
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False).head(10)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    sns.barplot(data=importances, x='Importance', y='Microbe', palette='viridis')
    plt.title("Top 10 Microbial Predictors of Sensor Accuracy (MARD)")
    plt.xlabel("Predictive Power (Feature Importance)")
    plt.tight_layout()
    plt.savefig("results/microbe_importance.png")
    
    print("Microbe driver analysis complete. Results saved to results/microbe_importance.png")
    return importances