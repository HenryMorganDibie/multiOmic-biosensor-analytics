<<<<<<< HEAD
from src.batch_processor import run_batch_analysis
from src.clinical_analysis import merge_and_analyze_clinical
from src.microbe_analysis import analyze_microbe_drivers

if __name__ == "__main__":
    # 1. Sensor Processing
    run_batch_analysis("data/raw/CGMacros")
    
    # 2. Clinical Integration
    merge_and_analyze_clinical()
    
    # 3. Microbe Discovery
    print("Step 3: Finding microbial signatures of sensor performance...")
    top_microbes = analyze_microbe_drivers()
    
    print("\n" + "="*40)
    print("ANALYSIS COMPLETE")
    print("Key Discovery: The following microbes correlate most with sensor drift/error:")
    print(top_microbes['Microbe'].to_list())
=======
from src.batch_processor import run_batch_analysis
from src.clinical_analysis import merge_and_analyze_clinical
from src.microbe_analysis import analyze_microbe_drivers

if __name__ == "__main__":
    # 1. Sensor Processing
    run_batch_analysis("data/raw/CGMacros")
    
    # 2. Clinical Integration
    merge_and_analyze_clinical()
    
    # 3. Microbe Discovery
    print("Step 3: Finding microbial signatures of sensor performance...")
    top_microbes = analyze_microbe_drivers()
    
    print("\n" + "="*40)
    print("ANALYSIS COMPLETE")
    print("Key Discovery: The following microbes correlate most with sensor drift/error:")
    print(top_microbes['Microbe'].to_list())
>>>>>>> f0a56f77262ae95fad99cf0d3804f291bf045502
    print("="*40)