import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_summary_stats():
    df = pd.read_csv("results/batch_summary_report.csv")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['MARD'], kde=True, color='skyblue')
    plt.axvline(df['MARD'].mean(), color='red', linestyle='--', label=f"Mean: {df['MARD'].mean():.2f}%")
    plt.title("Distribution of Sensor Accuracy (MARD) Across 45 Subjects")
    plt.xlabel("MARD (%)")
    plt.legend()
    plt.savefig("results/population_summary.png")
    print("Population summary plot saved to results/population_summary.png")