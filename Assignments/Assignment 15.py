#Assignment (11/03/2026)

#Assignment Name : Customer Segmentation
#Description : Perform K-Means clustering on a mall dataset and describe customer groups.

#Dataset: https://www.kaggle.com/code/tochelle1/mail-customer-segmentation/input

# Customer Segmentation using K-Means

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 2: Load Dataset
data = pd.read_csv("Mall_Customers.csv")

# Step 3: Display First 5 Rows
print("Dataset Preview:")
print(data.head())

# Step 4: Check Dataset Info
print("\nDataset Info:")
print(data.info())

# Step 5: Select Features for Clustering
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Step 6: Use Elbow Method to Find Optimal Number of Clusters
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure()
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Step 7: Apply K-Means (K = 5)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Step 8: Visualize Clusters
plt.figure()

plt.scatter(X.iloc[y_kmeans == 0, 0], X.iloc[y_kmeans == 0, 1], label='Cluster 1')
plt.scatter(X.iloc[y_kmeans == 1, 0], X.iloc[y_kmeans == 1, 1], label='Cluster 2')
plt.scatter(X.iloc[y_kmeans == 2, 0], X.iloc[y_kmeans == 2, 1], label='Cluster 3')
plt.scatter(X.iloc[y_kmeans == 3, 0], X.iloc[y_kmeans == 3, 1], label='Cluster 4')
plt.scatter(X.iloc[y_kmeans == 4, 0], X.iloc[y_kmeans == 4, 1], label='Cluster 5')

# Plot Centroids
plt.scatter(kmeans.cluster_centers_[:,0],
            kmeans.cluster_centers_[:,1],
            s=200,
            marker='X',
            label='Centroids')

plt.title('Customer Segments')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()

plt.show()

