# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 2: Create dataset
data = {
    "Age": [19, 21, 20, 23, 31, 22, 35, 23, 64, 30],
    "Annual Income": [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "Spending Score": [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
}

# Step 3: Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Step 4: Select features for clustering
X = df[["Annual Income", "Spending Score"]]

# Step 5: Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

# Step 6: Plot clusters
plt.scatter(df["Annual Income"], df["Spending Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Mall Customer Segmentation")

# Step 7: Plot centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:,0], centroids[:,1], marker='X', s=200)

plt.show()

# Step 8: Display centroids
print("Centroids:")
print(centroids)
