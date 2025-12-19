import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

def merge_and_analyze_clinical():
    # 1. Load Sensor Data
    sensor_df = pd.read_csv("results/batch_summary_report.csv")
    sensor_df['subject'] = sensor_df['Subject_ID'].str.extract(r'(\d+)').astype(int)
    
    # 2. Load Clinical & Microbe Data
    base_path = "data/raw/CGMacros"
    bio_df = pd.read_csv(os.path.join(base_path, "bio.csv"))
    gut_df = pd.read_csv(os.path.join(base_path, "gut_health_test.csv"))
    micro_df = pd.read_csv(os.path.join(base_path, "microbes.csv"))
    
    # 3. Use 'left' merges to keep all 49 subjects from the sensor data
    merged = sensor_df.merge(bio_df, on='subject', how='left')
    merged = merged.merge(gut_df, on='subject', how='left')
    merged = merged.merge(micro_df, on='subject', how='left')
    
    # Insight 1: BMI Correlation
    plt.figure(figsize=(10, 6))
    sns.regplot(data=merged, x='BMI', y='MARD', color='teal')
    plt.title("Impact of BMI on Biosensor Accuracy (MARD)")
    plt.savefig("results/clinical_bmi_correlation.png")
    
    # Insight 2: Inflammation Impact (Fixed the palette warning)
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=merged, x='Inflammatory Activity', y='MARD', 
                hue='Inflammatory Activity', palette='coolwarm', legend=False)
    plt.title("Sensor Accuracy vs. Host Inflammatory Activity")
    plt.savefig("results/clinical_inflammation_mard.png")
    
    # Save the huge integrated dataset (Sensor + Bio + Gut + Microbes)
    merged.to_csv("results/final_integrated_clinical_report.csv", index=False)
    print(f"Full clinical integration complete. Dataset now contains {len(merged)} subjects.")
    return merged