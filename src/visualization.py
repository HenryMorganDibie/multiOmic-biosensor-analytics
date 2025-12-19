import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def plot_performance(df, subject_id):
    plt.figure(figsize=(15, 7))
    
    # Use the columns we created in preprocessing
    plt.plot(df['Time_Clean'], df['Libre_Raw'], alpha=0.25, label='Raw Prototype Data (Noisy)', color='gray')
    plt.plot(df['Time_Clean'], df['Libre_Smooth'], label='Processed Signal (Filtered)', color='#1f77b4', linewidth=2)
    plt.plot(df['Time_Clean'], df['Dexcom_Clean'], label='Reference (Dexcom)', color='#d62728', linestyle='--')
    
    plt.title(f"Multi-Day Biosensor Performance Analysis: {subject_id}", fontsize=14)
    plt.xlabel("Timeline", fontsize=12)
    plt.ylabel("Analyte Concentration (mg/dL)", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.2)
    
    output_path = f"results/performance_{subject_id}.png"
    plt.savefig(output_path, dpi=300) # High resolution for the client
    plt.close()
    print(f"Chart saved to: {output_path}")