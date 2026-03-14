#Assignment (03/03/2026)

#Assignment Name : Build Your First Dataset
#Description : Create a dataset (e.g., study hours vs marks), identify features & labels, predict relationship.


# Step 1: Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 2: Create the dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 50, 55, 65, 70, 75, 85, 90, 95]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Step 3: Identify Features (X) and Label (y)
X = df[["Study_Hours"]]   # Feature
y = df["Marks"]           # Label

# Step 4: Build the model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict marks for a new study hour value
predicted_marks = model.predict([[7.5]])

print("\nPredicted marks for 7.5 study hours:", predicted_marks[0])

# Step 6: Visualize the relationship
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
