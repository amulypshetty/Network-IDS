
import pandas as pd
from pathlib import Path

# Folder containing all 8 CSV files
data_folder = Path("data/MachineLearningCVE")

print("\n========== ATTACK LABEL ANALYSIS ==========")

# Find all CSV files
csv_files = sorted(data_folder.glob("*.csv"))

for file in csv_files:
    print(f"\nFile: {file.name}")

    # Read the header to identify the Label column
    header = pd.read_csv(file, nrows=0)
    label_column = next(
        col for col in header.columns if col.strip() == "Label"
    )

    # Read only the Label column in smaller chunks
    label_counts = {}

    for chunk in pd.read_csv(
        file,
        usecols=[label_column],
        chunksize=100000
    ):
        counts = chunk[label_column].value_counts()

        for label, count in counts.items():
            label = str(label).strip()
            label_counts[label] = label_counts.get(label, 0) + count

    # Display attack types and counts
    for label, count in sorted(label_counts.items()):
        print(f"{label}: {count:,}")
