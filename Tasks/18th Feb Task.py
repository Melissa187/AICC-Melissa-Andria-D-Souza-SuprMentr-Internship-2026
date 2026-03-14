#Today's task: Sales analysis report create own dataset columns: month,revenue,marketing spend,profit task.Create line plot for revenue trend create scatter pot btn marketing, profit create correlation map write insights from your graph 

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Revenue": [50000, 52000, 58000, 60000, 65000, 70000, 
                72000, 75000, 78000, 82000, 85000, 90000],
    "Marketing_Spend": [8000, 8500, 9000, 9500, 10000, 11000, 
                        11500, 12000, 12500, 13000, 14000, 15000],
    "Profit": [12000, 13000, 15000, 16000, 18000, 20000, 
               21000, 23000, 25000, 27000, 29000, 32000]
}

df = pd.DataFrame(data)

# 1. Line plot for Revenue trend
plt.figure()
plt.plot(df["Month"], df["Revenue"])
plt.title("Revenue Trend Over Months")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# 2. Scatter plot between Marketing Spend and Profit
plt.figure()
plt.scatter(df["Marketing_Spend"], df["Profit"])
plt.title("Marketing Spend vs Profit")
plt.xlabel("Marketing Spend")
plt.ylabel("Profit")
plt.show()

# 3. Correlation Map
correlation = df[["Revenue", "Marketing_Spend", "Profit"]].corr()

plt.figure()
plt.imshow(correlation)
plt.title("Correlation Matrix")
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.colorbar()
plt.show()

df

