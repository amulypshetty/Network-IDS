
import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("data/processed/prepared_dataset.csv")

print("========== FEATURE ANALYSIS ==========")

# Separate input features and target
X = data.drop("Label", axis=1)

# 1. Check constant features
constant_features = [
    col for col in X.columns
    if X[col].nunique() <= 1
]

print("\nConstant Features:")
print(constant_features)
print("Total:", len(constant_features))

# 2. Check highly correlated features
correlation = X.corr().abs()

upper = correlation.where(
    np.triu(np.ones(correlation.shape), k=1).astype(bool)
)

high_corr_features = [
    col for col in upper.columns
    if any(upper[col] > 0.95)
]

print("\nHighly Correlated Features (> 0.95):")
print(high_corr_features)
print("Total:", len(high_corr_features))

# 3. Display feature count
print("\nOriginal Feature Count:", X.shape[1])

print("\nFeature analysis completed!")
