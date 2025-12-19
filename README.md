# Biosensor Population Analysis & Microbial Correlation Pipeline

**Project Scope:** Longitudinal Validation of 45-Subject Prototype Sensor Cohort

## 1. Project Overview

In this project, I developed an end-to-end data science pipeline to validate the performance of a prototype wearable biosensor. My goal was to move beyond basic accuracy reporting and investigate how a user’s unique biological profile—specifically their **BMI, inflammatory activity, and gut microbiome**—impacts sensor reliability.

## 2. Methodology & Technical Implementation

### A. Data Integrity & Ingestion

I processed raw time-series data for a cohort of 49 potential subjects. During my initial audit, I identified that four subjects (24, 25, 37, and 40) had incomplete data records or missing clinical metadata. To ensure the integrity of my statistical analysis, I excluded these individuals, resulting in a robust final cohort of **45 subjects**.

### B. Signal Conditioning

To handle the high-frequency "jitter" found in the prototype hardware, I implemented:

* **Gaussian Smoothing:** I applied a Gaussian filter () to the raw sensor data to extract the true physiological signal while preserving the kinetics of glucose spikes.
* **Temporal Synchronization:** I aligned the prototype data with the gold-standard reference (Dexcom G6) to ensure accurate point-to-point comparison for MARD calculation.

### C. Advanced Engineering Metrics

I implemented four specialized metrics to quantify the sensor's performance:

* **MARD (Mean Absolute Relative Difference):** The primary metric for clinical accuracy.
* **SNR (Signal-to-Noise Ratio):** I quantified signal quality by comparing smoothed signal variance against the residual hardware noise.
* **Cross-Correlation Lag:** Since interstitial fluid naturally lags behind blood glucose, I used cross-correlation to determine the exact **response time** (in minutes) of the prototype.
* **Hysteresis Analysis:** I calculated the error bias during rising vs. falling glucose trends to evaluate the sensor membrane's stability during rapid metabolic changes.

## 3. Clinical & Microbial Discovery

The core value of this pipeline is the integration of diverse datasets, including physical markers (`bio.csv`) and microbiome profiles (`microbes.csv`).

### The "Microbe Driver" Model

I built a **Random Forest Regressor** to identify correlations between the gut microbiome and sensor error. By treating the counts of hundreds of bacterial species as features, I was able to rank which microbes "predict" a less accurate sensor.

**Key Findings:**

* **Microbial Predictors:** I identified that *Streptococcus salivarius* and *Bacteroides thetaiotaomicron* were among the top 10 features correlating with sensor drift.
* **Physiological Impact:** My analysis revealed a clear correlation between **BMI** and **MARD**, suggesting that subcutaneous tissue thickness is a significant covariate for this device.

## 4. Final Cohort Results

* **Mean Population MARD:** 25.49%
* **Mean SNR:** 49.14 dB
* **Cohort Size:** 45 Valid Subjects

## 5. Pipeline Structure

* `src/preprocessing.py`: Signal smoothing and time-alignment.
* `src/metrics.py`: Implementation of MARD, SNR, Lag, and Hysteresis.
* `src/clinical_analysis.py`: "Left-Join" merging of sensor results with BMI and inflammatory markers.
* `src/microbe_analysis.py`: Machine Learning driver analysis using Scikit-learn.
* `main.py`: One-click execution of the entire end-to-end pipeline.

---

### Final Project Status: Complete

I have generated the following artifacts in the `results/` directory:

* `batch_summary_report.csv`: Individual-level engineering KPIs.
* `final_integrated_clinical_report.csv`: Integrated master dataset for further analysis.
=======
# Biosensor Population Analysis & Microbial Correlation Pipeline

**Project Scope:** Longitudinal Validation of 45-Subject Prototype Sensor Cohort

## 1. Project Overview

In this project, I developed an end-to-end data science pipeline to validate the performance of a prototype wearable biosensor. My goal was to move beyond basic accuracy reporting and investigate how a user’s unique biological profile—specifically their **BMI, inflammatory activity, and gut microbiome**—impacts sensor reliability.

## 2. Methodology & Technical Implementation

### A. Data Integrity & Ingestion

I processed raw time-series data for a cohort of 49 potential subjects. During my initial audit, I identified that four subjects (24, 25, 37, and 40) had incomplete data records or missing clinical metadata. To ensure the integrity of my statistical analysis, I excluded these individuals, resulting in a robust final cohort of **45 subjects**.

### B. Signal Conditioning

To handle the high-frequency "jitter" found in the prototype hardware, I implemented:

* **Gaussian Smoothing:** I applied a Gaussian filter () to the raw sensor data to extract the true physiological signal while preserving the kinetics of glucose spikes.
* **Temporal Synchronization:** I aligned the prototype data with the gold-standard reference (Dexcom G6) to ensure accurate point-to-point comparison for MARD calculation.

### C. Advanced Engineering Metrics

I implemented four specialized metrics to quantify the sensor's performance:

* **MARD (Mean Absolute Relative Difference):** The primary metric for clinical accuracy.
* **SNR (Signal-to-Noise Ratio):** I quantified signal quality by comparing smoothed signal variance against the residual hardware noise.
* **Cross-Correlation Lag:** Since interstitial fluid naturally lags behind blood glucose, I used cross-correlation to determine the exact **response time** (in minutes) of the prototype.
* **Hysteresis Analysis:** I calculated the error bias during rising vs. falling glucose trends to evaluate the sensor membrane's stability during rapid metabolic changes.

## 3. Clinical & Microbial Discovery

The core value of this pipeline is the integration of diverse datasets, including physical markers (`bio.csv`) and microbiome profiles (`microbes.csv`).

### The "Microbe Driver" Model

I built a **Random Forest Regressor** to identify correlations between the gut microbiome and sensor error. By treating the counts of hundreds of bacterial species as features, I was able to rank which microbes "predict" a less accurate sensor.

**Key Findings:**

* **Microbial Predictors:** I identified that *Streptococcus salivarius* and *Bacteroides thetaiotaomicron* were among the top 10 features correlating with sensor drift.
* **Physiological Impact:** My analysis revealed a clear correlation between **BMI** and **MARD**, suggesting that subcutaneous tissue thickness is a significant covariate for this device.

## 4. Final Cohort Results

* **Mean Population MARD:** 25.49%
* **Mean SNR:** 49.14 dB
* **Cohort Size:** 45 Valid Subjects

## 5. Pipeline Structure

* `src/preprocessing.py`: Signal smoothing and time-alignment.
* `src/metrics.py`: Implementation of MARD, SNR, Lag, and Hysteresis.
* `src/clinical_analysis.py`: "Left-Join" merging of sensor results with BMI and inflammatory markers.
* `src/microbe_analysis.py`: Machine Learning driver analysis using Scikit-learn.
* `main.py`: One-click execution of the entire end-to-end pipeline.

---

### Final Project Status: Complete

I have generated the following artifacts in the `results/` directory:

* `batch_summary_report.csv`: Individual-level engineering KPIs.
* `final_integrated_clinical_report.csv`: Integrated master dataset for further analysis.
* `microbe_importance.png`: Visual discovery of microbial drivers of sensor inaccuracy.