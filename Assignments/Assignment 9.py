#Assignment (28/02/2026)

#Assignment Name : Storytelling with Graphs
#Description : Create bar chart, pie chart, histogram and write a short data story explaining trends.

# Storytelling with Graphs - Full Code
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ Sample Data
# -----------------------------
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": [120, 150, 90, 200, 130],
    "Region": ["North", "South", "East", "West", "North"]
}
df = pd.DataFrame(data)

# -----------------------------
# 2️⃣ Bar Chart
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Product"], df["Sales"], color='skyblue')
plt.title("Sales of Products")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.show()

# -----------------------------
# 3️⃣ Pie Chart
# -----------------------------
plt.figure(figsize=(6,6))
plt.pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%",
        colors=['gold', 'lightgreen', 'lightcoral', 'lightskyblue', 'pink'])
plt.title("Sales Distribution by Product")
plt.show()

# -----------------------------
# 4️⃣ Histogram
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=5, color='orange', edgecolor='black')
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 5️⃣ Data Story
# -----------------------------
story = """
Data Story:
- Product D is the top-selling item with 200 units, while Product C has the lowest sales at 90 units.
- The pie chart shows that Product D contributes the largest share (~29%) of total sales, 
  indicating it is crucial for revenue.
- Histogram shows most products sell between 100-150 units, highlighting moderate sales consistency 
  except for the high performer D and the low performer C.
- Actionable insight: Focus on boosting sales of lower-performing products while maintaining 
  Product D's success.
"""
print(story)


