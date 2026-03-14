#Assignment (24/02/2026)

#Assignment Name : Dataset Detective
#Description : Load a dataset, display top rows, find highest value column, count missing values, share 5 insights.

import pandas as pd

# Create dataset directly
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [20000, 25000, 22000, 27000, 30000],
    "Marketing_Spend": [5000, 7000, 6000, 8000, 9000],
    "Profit": [15000, 18000, 16000, 19000, 21000]
}

df = pd.DataFrame(data)

# Save as CSV (you don’t need to type it manually)
df.to_csv("dataset_ass_7.csv", index=False)

# Optional: check the top rows
print(df.head())
