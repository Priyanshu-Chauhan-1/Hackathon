import pandas as pd
import numpy as np

cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome']
df = pd.read_csv('diabetes.csv')

print("=== PIMA DIABETES DATASET ANALYSIS ===")
print(f"Total records: {len(df)}")
print(f"Diabetes cases: {df['Outcome'].sum()} ({df['Outcome'].mean()*100:.1f}% positive)")
print("\nFirst 3 rows:")
print(df.head(3))

print("\nKey stats (means):")
print(df[['Glucose', 'BMI', 'BloodPressure', 'Age']].mean())

print("\nZeros check (possible missing values):")
zeros = (df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] == 0).sum()
print(zeros)

print("\nCorrelation with Diabetes (Outcome):")
corr = df.corr()['Outcome'].sort_values(ascending=False)
print(corr)

df.to_csv('diabetes_clean.csv', index=False)
print("\n Data saved as 'diabetes_clean.csv'")