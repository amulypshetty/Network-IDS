
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load prepared dataset
data = pd.read_csv("data/processed/prepared_dataset.csv")

print("========== EXPLORATORY DATA ANALYSIS ==========")

# 1. Dataset information
print("\nDataset Shape:")
print(data.shape)

# 2. Label distribution
print("\nLabel Distribution:")
print(data["Label"].value_counts())

# 3. Missing values
print("\nMissing Values:")
print(data.isnull().sum().sum())

# 4. Duplicate records
print("\nDuplicate Records:")
print(data.duplicated().sum())

# 5. Statistical information
print("\nStatistical Summary:")
print(data.describe())

# 6. Traffic distribution graph
sns.countplot(x="Label", data=data)

plt.title("Normal vs Attack Traffic")
plt.xlabel("Traffic (0 = Normal, 1 = Attack)")
plt.ylabel("Number of Records")

plt.savefig("data/processed/traffic_distribution.png")
plt.close()

print("\nEDA completed successfully!")

