import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# LOAD DATASET
df = pd.read_csv('diabetes_clean.csv')

# Target: Outcome (0=Healthy, 1=Diabetes)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# TRAIN-TEST SPLIT (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# RANDOM FOREST MODEL (Tuned for Hackathon)
model = RandomForestClassifier(
    n_estimators=100,      
    max_depth=6,           
    min_samples_split=5,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# MODEL EVALUATION
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("=== MODEL TRAINING COMPLETE ===")
print(f"Accuracy on test set: {accuracy:.3f} ({accuracy*100:.1f}%)")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# FEATURE IMPORTANCE (Medical Insights)
importances = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nTop 5 Important Features:")
print(importances.head())

# SAVE MODEL FOR PRODUCTION
joblib.dump(model, 'diabetes_model.pkl')
print("\n Model saved: 'diabetes_model.pkl'")
print("Next: step3_streamlit.py")
