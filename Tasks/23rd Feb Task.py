import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Create DataFrame with sample data
# (Assuming Mileage is in km/liter or MPG, and Price is in USD)
data = {
    'Engine Size': [1000, 1200, 1400, 1500, 1600, 1800, 2000],
    'Mileage': [25, 22, 20, 18, 16, 15, 12], 
    'Age': [5, 4, 4, 3, 5, 6, 2],
    'Price': [5000, 6500, 7500, 9000, 8000, 8500, 12000] 
}
df = pd.DataFrame(data)

print("--- Dataset ---")
print(df.to_string(), "\n")

# 2. Train the Multiple Linear Regression model
# Separate features (X) and target variable (y)
X = df[['Engine Size', 'Mileage', 'Age']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

# 3. Predict price for: Engine = 1500, Mileage = 20, Age = 3
# We pass the new data as a DataFrame with the same column names to avoid warnings
new_car = pd.DataFrame({
    'Engine Size': [1500], 
    'Mileage': [20], 
    'Age': [3]
})

predicted_price = model.predict(new_car)[0]
print(f"--- Prediction ---")
print(f"Predicted Price for Engine=1500, Mileage=20, Age=3: ${predicted_price:.2f}\n")

# 4. Print coefficients
print("--- Model Coefficients ---")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")
print(f"Intercept: {model.intercept_:.2f}\n")