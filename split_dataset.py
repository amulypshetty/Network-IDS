
import pandas as pd
from sklearn.model_selection import train_test_split

print("========== TRAIN TEST SPLITTING ==========")

# Load selected dataset
data = pd.read_csv("data/processed/selected_dataset.csv")

# Separate features and target
X = data.drop("Label", axis=1)
y = data["Label"]

print("\nOriginal Dataset Shape:", data.shape)

# Split dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Display shapes
print("\nTraining Features:", X_train.shape)
print("Testing Features:", X_test.shape)

print("\nTraining Labels:", y_train.shape)
print("Testing Labels:", y_test.shape)

# Display class distribution
print("\nTraining Label Distribution:")
print(y_train.value_counts())

print("\nTesting Label Distribution:")
print(y_test.value_counts())

# Save split datasets
X_train.to_csv("data/processed/X_train.csv", index=False)
X_test.to_csv("data/processed/X_test.csv", index=False)
y_train.to_csv("data/processed/y_train.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

print("\nTrain-test splitting completed!")
print("All split datasets saved successfully!")
