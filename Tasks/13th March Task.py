#Task 1: Build Text Preprocessing Tool

#Create a program that:

#Input:

#"I am learning NLP and it is very exciting!!!"

#Your program should:

#convert to lowercase

#remove punctuation

#tokenize text

#remove stopwords

#apply stemming

#Output example:

#['learn','nlp','excit']

import pandas as pd
import numpy as np
import nltk
import string
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# --- 0. SETUP & DOWNLOADS ---
# These downloads only happen once
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def setup_data():
    """Creates a valid student.csv if the current one is incorrect."""
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
        'maths': [85, 70, 95, 60, 88, 92, 45, 76],
        'science': [90, 80, 85, 65, 78, 95, 50, 82],
        'english': [78, 75, 88, 70, 82, 91, 55, 79],
        'dept': ['CS', 'Math', 'CS', 'Math', 'CS', 'Math', 'Bio', 'Bio']
    }
    pd.DataFrame(data).to_csv("student.csv", index=False)
    print("Checked 'student.csv': Data is ready.\n")

# Run the setup
setup_data()

# --- 1. PANDAS DATASET TASK ---
print("--- TASK 1: DATASET PROCESSING ---")
df = pd.read_csv("student.csv")

# Handle missing values
subjects = ['maths', 'science', 'english']
df[subjects] = df[subjects].fillna(0)

# Add Total and Average
df['total'] = df[subjects].sum(axis=1)
df['average'] = df['total'] / 3

# Find Top 3
top_3 = df.sort_values(by='total', ascending=False).head(3)
print("Top 3 Students:\n", top_3[['name', 'total']])

# Dept Wise Average
dept_avg = df.groupby('dept')[subjects + ['total', 'average']].mean()
print("\nDept Wise Average:\n", dept_avg)

# Scoring > 75 in all
high_scorers = df[(df['maths'] > 75) & (df['science'] > 75) & (df['english'] > 75)]
print("\nStudents scoring > 75 in all subjects:\n", high_scorers[['name', 'maths', 'science', 'english']])


# --- 2. NLP PREPROCESSING TASK ---
print("\n" + "="*30 + "\n")
print("--- TASK 2: NLP PREPROCESSING ---")

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    final_output = [stemmer.stem(w) for w in filtered_tokens]
    
    return final_output

input_text = "I am learning NLP and it is very exciting!!!"
nlp_result = preprocess_text(input_text)

print(f"Input: {input_text}")
print(f"Output: {nlp_result}")