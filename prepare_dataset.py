
import pandas as pd
import numpy as np
from pathlib import Path

# Dataset folder
data_folder = Path("data/MachineLearningCVE")

# Find all CSV files
csv_files = sorted(data_folder.glob("*.csv"))

print("========== DATASET PREPARATION ==========")

dataframes = []

# Read and combine all files
for file in csv_files:
    print(f"\nReading: {file.name}")

    df = pd.read_csv(file, low_memory=False)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean labels
    df["Label"] = df["Label"].astype(str).str.strip()

    dataframes.append(df)

# Combine datasets
data = pd.concat(dataframes, ignore_index=True)

print("\nCombined dataset shape:", data.shape)

# Convert labels into binary classification
data["Label"] = data["Label"].apply(
    lambda x: 0 if x == "BENIGN" else 1
)

# Convert features to numeric values
for col in data.columns:
    if col != "Label":
        data[col] = pd.to_numeric(data[col], errors="coerce")

# Replace infinite values
data.replace([np.inf, -np.inf], np.nan, inplace=True)

# Handle missing values
data.dropna(inplace=True)

# Remove duplicate records
data.drop_duplicates(inplace=True)

# Display final information
print("\n========== FINAL DATASET ==========")

print("Dataset shape:", data.shape)

print("\nLabel distribution:")
print(data["Label"].value_counts())

print("\nNormal traffic (0):", (data["Label"] == 0).sum())
print("Attack traffic (1):", (data["Label"] == 1).sum())

# Save prepared dataset
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

data.to_csv(
    output_folder / "prepared_dataset.csv",
    index=False
)

print("\nDataset saved successfully!")
print("Location: data/processed/prepared_dataset.csv")
