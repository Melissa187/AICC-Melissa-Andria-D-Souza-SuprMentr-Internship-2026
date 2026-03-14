#Create a dataset with columns: age(some missing) salary(some missing) city (mixed case: hyderabad, HYDERABAD, Hyderabad) experience(some duplicates) perform: remove duplicates handle missing values standardize city names apply minMax scaling on age and salary show final cleaned data.
# Step 1: Create dataset
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = {
    "age": [25, 30, np.nan, 28, 25, 35, np.nan, 30],
    "salary": [50000, 60000, 55000, np.nan, 50000, 70000, 65000, np.nan],
    "city": ["hyderabad", "HYDERABAD", "Hyderabad", "mumbai", "MUMBAI", "Mumbai", "hyderabad", "HYDERABAD"],
    "experience": [2, 5, 3, 4, 2, 7, 3, 5]  # duplicates exist
}

df = pd.DataFrame(data)

# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Handle missing values
df["age"].fillna(df["age"].mean(), inplace=True)
df["salary"].fillna(df["salary"].mean(), inplace=True)

# Step 4: Standardize city names
df["city"] = df["city"].str.lower().str.strip().str.capitalize()

# Step 5: Apply MinMax Scaling on age and salary
scaler = MinMaxScaler()
df[["age", "salary"]] = scaler.fit_transform(df[["age", "salary"]])

df
