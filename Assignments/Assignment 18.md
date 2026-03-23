#Assignment (19/03/2026)

#Assignment Name : Mini Project Proposal
#Description : Submit a 1-page proposal with problem, dataset, algorithm, expected output.

Mini Project Proposal - Enhanced Predictive Lead Scoring
1. Problem Definition:The challenge most businesses face is to determine which potential customers are actually likely to make a purchase. While K-Means Clustering (from our last assignment) helps us understand who our customers are, it does not provide any information on whether a new lead is likely to convert or not. This project seeks to bridge this gap by utilizing historical data to forecast "High Value" conversion probabilities.
2. Data Description:The data to be used for this project would be an extension of the Mall Customer Data Set or Online Retail II Data Set (from UCI Machine Learning Repository).Key Features:Annual Income, Spending Score, Age ,Frequency of Visits, Converted (Yes/No),Size:500 - 1,000 records.
3. Proposed Algorithm:The algorithm to be used for this project is a Hybrid Model: 
K-Means Clustering: To cluster our existing customers based on their behavior (Sensible, Careless, Target, etc.).
Random Forest Classifier:To then forecast the possibility of a new customer falling into the "Target/Elite" group based on initial data provided.
4. Expected Output:Segment Visualization: 3D Scatter Plot showing customer segments.Accuracy Metrics:Confusion Matrix,Accuracy Score (> 85%), Business Insight: Lead Score Visualization