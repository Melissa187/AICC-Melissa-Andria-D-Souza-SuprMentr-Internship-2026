#Assignment (07/03/2026)

#Assignment Name : KNN in Real Life
#Description : Explain Netflix-like recommendations using KNN and create a small similarity example.

# Import libraries
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# ---------------------------------
# Step 1: Create a small movie dataset
# ---------------------------------

data = {
    "Movie": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"],
    "Action": [1, 1, 0, 0, 1],
    "Romance": [0, 0, 1, 1, 0],
    "Comedy": [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

print("Movie Dataset:\n")
print(df)

# ---------------------------------
# Step 2: Use features for similarity
# ---------------------------------

features = df[["Action", "Romance", "Comedy"]]

# ---------------------------------
# Step 3: Train KNN Model
# ---------------------------------

knn = NearestNeighbors(n_neighbors=2)
knn.fit(features)

# ---------------------------------
# Step 4: Find similar movies
# ---------------------------------

movie_index = 0  # Movie A
distances, indices = knn.kneighbors([features.iloc[movie_index]])

print("\nMovies similar to", df.iloc[movie_index]["Movie"], ":")

for i in indices[0][1:]:
    print(df.iloc[i]["Movie"])

