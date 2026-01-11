# Hackathon
### Hackathon Project - Silent Disease Detector

STEP 1: Data Acquisition → Cleaning → EDA (COMPLETE)
Problem: Silent Disease Early Detection Engine Dataset: PIMA Indians Diabetes (Kaggle) Goal: Build ML model with 77% + accuracy Demo: Streamlit web app with live predictions
Step 1.1: Dataset Discovery & Download (Kaggle)
Action: Found "PIMA Indians Diabetes Database" on Kaggle Source: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database Method: Direct CSV download (diabetes.csv - 9KB) Dataset: 768 patients × 9 columns
Step 1.2: Initial Data Inspection
1. Loaded raw CSV into pandas 2. Shape confirmed: (768 rows × 9 columns) 3. Challenge: No column headers in raw file 4. Solution: Added medical-standard column names
Step 1.3: Data Quality Assessment & Cleaning
Issues Found & Fixed:
Zero Values (Medical Impossibilities):

Feature	Zero Count	Fixed To
Glucose	5 zeros	Mean (122)
BloodPressure	35 zeros	Mean (72)
BMI	11 zeros	Mean (32)
Insulin	374 zeros	Median (30)
SkinThickness	227 zeros	Median (29)
Outliers: Capped at 99th percentile

Missing Indicators: Zero → NaN → Imputed

Step 1.4: Exploratory Data Analysis (EDA)
📊 Key Statistics Generated:

Diabetes Prevalence: 34.90% (268 positive cases) Feature Correlations with Outcome:
┌────────────────────┬──────────┐ 
│ Glucose │ 0.466 │ 
│ BMI │ 0.301 │ 
│ Age │ 0.238 │
│ Pregnancies │ 0.221 │
└────────────────────┴──────────┘

Distribution Analysis:

Age: 21-81 years (mean: 33.2)
BMI: 18.5-42.7 (mean: 32.0)
Glucose: 70-190 mg/dL (mean: 121)
Step 1.5: Data Export & Validation
Final Dataset: diabetes_clean.csv (9.2KB) ✅ 768 rows × 9 columns ✅ 0% missing values ✅ Medical outliers handled ✅ Ready for Step 2 ML Training
