
import pandas as pd

# Load prepared dataset
data = pd.read_csv("data/processed/prepared_dataset.csv")

print("========== FEATURE SELECTION ==========")

# Identify constant features automatically
constant_features = [
    col for col in data.columns
    if col != "Label" and data[col].nunique() <= 1
]

print("\nFeatures to Remove:")
print(constant_features)

# Remove constant features
selected_data = data.drop(columns=constant_features)

# Display results
print("\nOriginal Dataset Shape:", data.shape)
print("Selected Dataset Shape:", selected_data.shape)

print("\nRemaining Features:", selected_data.shape[1] - 1)

# Save selected dataset
selected_data.to_csv(
    "data/processed/selected_dataset.csv",
    index=False
)

print("\nSelected dataset saved successfully!")
print("Location: data/processed/selected_dataset.csv")
