
import pandas as pd
import joblib

from sklearn.metrics import accuracy_score, classification_report

print("========== NETWORK IDS BATCH PREDICTION ==========")

# Load trained model
model = joblib.load("data/processed/random_forest_model.pkl")

# Load test data
X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv").squeeze()

# Select first 100 records
X_sample = X_test.iloc[:100]
y_actual = y_test.iloc[:100]

# Predict traffic
y_pred = model.predict(X_sample)

# Display results
print("\nTotal Records Tested:", len(X_sample))

print("\nActual Labels:")
print(y_actual.value_counts().rename(index={0: "BENIGN", 1: "ATTACK"}))

print("\nPredicted Labels:")
print(pd.Series(y_pred).value_counts().rename(index={0: "BENIGN", 1: "ATTACK"}))

# Calculate accuracy
accuracy = accuracy_score(y_actual, y_pred)

print("\nPrediction Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(
    y_actual,
    y_pred,
    target_names=["BENIGN", "ATTACK"],
    zero_division=0
))

print("\nBatch prediction completed!")
