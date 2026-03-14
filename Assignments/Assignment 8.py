#Assignment (26/02/2026)

#Assignment Name : Data Doctor
#Description : Clean a dataset by handling missing values, removing duplicates, standardizing text, and explain why cleaning matters.

# Import required libraries
import pandas as pd
import numpy as np

# -------------------------------
# STEP 1: Create a Messy Dataset
# -------------------------------

data = {
    "Name": ["Alice", "Bob", "alice ", "Charlie", None, "Bob"],
    "Age": [25, 30, 250, None, 22, 30],  # 250 is unrealistic (outlier)
    "City": ["New York", "Los Angeles", "new york", "Chicago", "Chicago", "Los Angeles"],
    "Marks": [85, 90, None, 78, 88, 90]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# -------------------------------
# STEP 2: Handle Missing Values
# -------------------------------

# Fill missing Age with median (better than mean when outliers exist)
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Drop rows where Name is missing (important column)
df = df.dropna(subset=["Name"])

# -------------------------------
# STEP 3: Remove Duplicates
# -------------------------------

df = df.drop_duplicates()

# -------------------------------
# STEP 4: Standardize Text
# -------------------------------

df["Name"] = df["Name"].str.strip().str.lower()
df["City"] = df["City"].str.strip().str.lower()

# -------------------------------
# STEP 5: Handle Outliers
# -------------------------------

# Remove unrealistic ages (example: age > 100)
df = df[df["Age"] <= 100]

# -------------------------------
# STEP 6: Fix Data Types
# -------------------------------

df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(float)

print("\nCleaned Dataset:\n")
print(df)

# -------------------------------
# STEP 7: Final Check
# -------------------------------

print("\nDataset Info:\n")
print(df.info())

print("\nSummary Statistics:\n")
print(df.describe())


