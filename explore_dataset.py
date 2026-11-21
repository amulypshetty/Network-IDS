
import pandas as pd

# Path of the first dataset file
file_path = "data/MachineLearningCVE/Monday-WorkingHours.pcap_ISCX.csv"

# Read only 10,000 rows initially to avoid using too much memory
df = pd.read_csv(file_path, nrows=10000)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\n========== DATASET INFORMATION ==========")

# Number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display first 5 records
print("\nFirst 5 records:")
print(df.head())

# Display data types
print("\nData types:")
print(df.dtypes)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Check attack labels
print("\nTraffic label distribution:")
print(df["Label"].value_counts())