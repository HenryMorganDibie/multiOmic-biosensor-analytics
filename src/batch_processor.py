import os
import pandas as pd
from src.preprocessing import load_and_clean
from src.metrics import calculate_advanced_metrics

def run_batch_analysis(base_path):
    all_results = []
    # Identify any folder that looks like a subject (001, CGMacros-001, etc)
    items = os.listdir(base_path)
    subject_folders = [f for f in items if os.path.isdir(os.path.join(base_path, f))]
    
    print(f"Detected {len(subject_folders)} potential subject folders.")

    for subject in sorted(subject_folders):
        try:
            folder_path = os.path.join(base_path, subject)
            # Find the first CSV in that folder
            csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
            if not csv_files: continue
            
            file_path = os.path.join(folder_path, csv_files[0])
            df, dex_name, lib_name = load_and_clean(file_path)
            
            metrics = calculate_advanced_metrics(df, dex_name)
            metrics['Subject_ID'] = subject
            all_results.append(metrics)
            print(f"Processed: {subject}")
            
        except Exception as e:
            print(f"Skipping {subject}: {e}")
            
    summary_df = pd.DataFrame(all_results)
    summary_df.to_csv("results/batch_summary_report.csv", index=False)
    return summary_df