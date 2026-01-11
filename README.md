# Hackathon
### Hackathon Project - Silent Disease Detector

Repository for gkv-p - Vibe Coding Hackathon

<h3><b>STEP 1:</b> Data Acquisition → Cleaning → EDA (COMPLETE)</h3>
<b>Problem:  <q>Silent Disease Early Detection Engine</q> </b>
<b>Dataset: </b> PIMA Indians Diabetes (Kaggle)
<b>Goal: </b> Build ML model with 77% + accuracy
<b>Demo: </b> Streamlit web app with live predictions

<h4>Step 1.1: Dataset Discovery & Download (Kaggle)</h4>
<b>Action: </b> Found "PIMA Indians Diabetes Database" on Kaggle
<b>Source: </b> https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
<b>Method: </b> Direct CSV download (diabetes.csv - 9KB)
<b>Dataset: </b> 768 patients × 9 columns

<h4>Step 1.2: Initial Data Inspection</h4>
1. Loaded raw CSV into pandas
2. Shape confirmed: (768 rows × 9 columns)
3. Challenge: No column headers in raw file
4. Solution: Added medical-standard column names

<h4>Step 1.3: Data Quality Assessment & Cleaning</h4>
Issues Found & Fixed:

1. Zero Values (Medical Impossibilities):
   | Feature | Zero Count | Fixed To |
   |---------|------------|----------|
   | Glucose | 5 zeros    | Mean (122) |
   | BloodPressure | 35 zeros | Mean (72) |
   | BMI | 11 zeros    | Mean (32) |
   | Insulin | 374 zeros  | Median (30) |
   | SkinThickness | 227 zeros | Median (29) |

2. Outliers: Capped at 99th percentile
3. Missing Indicators: Zero → NaN → Imputed


<h4>Step 1.4: Exploratory Data Analysis (EDA)</h4>

📊 Key Statistics Generated:

Diabetes Prevalence: 34.90% (268 positive cases)
Feature Correlations with Outcome:
┌────────────────────┬──────────┐
│ Glucose            │ 0.466    │
│ BMI                │ 0.301    │
│ Age                │ 0.238    │
│ Pregnancies        │ 0.221    │
└────────────────────┴──────────┘

Distribution Analysis:
- Age: 21-81 years (mean: 33.2)
- BMI: 18.5-42.7 (mean: 32.0) 
- Glucose: 70-190 mg/dL (mean: 121)


<h4>Step 1.5: Data Export & Validation</h4>
<b>Final Dataset:</b> diabetes_clean.csv (9.2KB)
✅ 768 rows × 9 columns
✅ 0% missing values
✅ Medical outliers handled
✅ Ready for Step 2 ML Training
s_clean.csv (9.2KB) ✅ 768 rows × 9 columns ✅ 0% missing values ✅ Medical outliers handled ✅ Ready for Step 2 ML Training
