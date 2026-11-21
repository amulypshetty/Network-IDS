
import pandas as pd
import joblib
import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("========== RANDOM FOREST MODEL TRAINING ==========")

# Load training and testing data
X_train = pd.read_csv("data/processed/X_train.csv")
X_test = pd.read_csv("data/processed/X_test.csv")

y_train = pd.read_csv("data/processed/y_train.csv").squeeze()
y_test = pd.read_csv("data/processed/y_test.csv").squeeze()

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

# Train model
print("\nTraining started...")

start_time = time.time()

model.fit(X_train, y_train)

end_time = time.time()

print("\nTraining completed!")

print("Training Time:", round(end_time - start_time, 2), "seconds")

# Predict test data
print("\nTesting model...")

y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n========== MODEL RESULTS ==========")
print("Accuracy:", round(accuracy * 100, 2), "%")

# Save trained model
joblib.dump(model, "data/processed/random_forest_model.pkl")

print("\nModel saved successfully!")
print("Location: data/processed/random_forest_model.pkl")
