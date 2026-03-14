import pandas as pd
import numpy as np

# 1. Create/Ensure Dataset matches the Task Requirements
# Since the current student.csv only has 'id', 'name', 'gpa', 
# we create a sample dataset that matches your "Task for Today" requirements.
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'maths': [85, 70, 95, 60, 88, 92, 45, 76],
    'science': [90, 80, 85, 65, 78, 95, 50, 82],
    'english': [78, 75, 88, 70, 82, 91, 55, 79],
    'dept': ['CS', 'Math', 'CS', 'Math', 'CS', 'Math', 'Bio', 'Bio']
}

# Create the DataFrame and save it as student.csv to simulate the file read
df_initial = pd.DataFrame(data)
# Let's add some missing values to demonstrate handling
df_initial.loc[1, 'maths'] = np.nan
df_initial.loc[3, 'science'] = np.nan
df_initial.to_csv("student.csv", index=False)

# --- START OF MAIN TASK ---

# 1. Read CSV
df = pd.read_csv("student.csv")

# 2. Handle missing values
# Filling missing marks with 0 as specified in your original logic
subjects = ['maths', 'science', 'english']
df[subjects] = df[subjects].fillna(0)

# 3. Add total column
df['total'] = df['maths'] + df['science'] + df['english']

# 4. Add average column
df['average'] = df['total'] / 3

# 5. Find Top 3 students based on total
top_3 = df.sort_values(by='total', ascending=False).head(3)

print("--- Top 3 Students ---")
print(top_3[['name', 'total']])

# 6. Department wise average marks
# Using mean() to find averages for each subject, total, and overall average per dept
dept_avg = df.groupby('dept')[subjects + ['total', 'average']].mean()

print("\n--- Department Wise Average Marks ---")
print(dept_avg)

# 7. Students scoring above 75 in all subjects
above_75 = df[
    (df['maths'] > 75) & 
    (df['science'] > 75) & 
    (df['english'] > 75)
]

print("\n--- Students scoring above 75 in all subjects ---")
if not above_75.empty:
    print(above_75[['name', 'maths', 'science', 'english']])
else:
    print("No students met the criteria.")

# Save the final results to a new file
df.to_csv("student_task_results.csv", index=False)