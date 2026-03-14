#Assignment (09/03/2026)

#Assignment Name : House Price Predictor
#Description : Train a Linear Regression model, predict prices, and test with new input.

# Import required libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ----------------------------------
# STEP 1: Create Sample Housing Data
# ----------------------------------

data = {
    "Size_sqft": [1000, 1500, 1800, 2400, 3000, 3500],
    "Bedrooms": [2, 3, 3, 4, 4, 5],
    "Age": [10, 5, 8, 2, 1, 3],
    "Price": [200000, 300000, 350000, 450000, 500000, 600000]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# ----------------------------------
# STEP 2: Define Features and Target
# ----------------------------------

X = df[["Size_sqft", "Bedrooms", "Age"]]   # Features
y = df["Price"]                            # Target variable

# ----------------------------------
# STEP 3: Split Data into Train/Test
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------
# STEP 4: Train Linear Regression Model
# ----------------------------------

model = LinearRegression()
model.fit(X_train, y_train)

# ----------------------------------
# STEP 5: Make Predictions
# ----------------------------------

predictions = model.predict(X_test)

print("\nPredicted Prices:", predictions)
print("Actual Prices:", y_test.values)

# ----------------------------------
# STEP 6: Evaluate Model
# ----------------------------------

mse = mean_squared_error(y_test, predictions)
print("\nMean Squared Error:", mse)

# ----------------------------------
# STEP 7: Predict Price for New House
# ----------------------------------

new_house = np.array([[2000, 3, 5]])  # size, bedrooms, age
predicted_price = model.predict(new_house)

print("\nPredicted Price for New House:", predicted_price[0])

