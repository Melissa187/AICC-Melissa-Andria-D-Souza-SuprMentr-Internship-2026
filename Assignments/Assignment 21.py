#Assignment (24/03/2026)

#Assignment Name :Word Importance Explorer
#Description : Use TF-IDF on 5 documents and identify top keywords with explanation.

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 1. Define your 5 documents
documents = [
    "AI is transforming the future of healthcare and medicine.",
    "Space exploration is reaching new heights with Mars missions.",
    "Healthcare systems are adopting new digital tools for patients.",
    "The future of AI depends on ethical data collection.",
    "Mars is a primary target for future space exploration."
]

# 2. Initialize the Vectorizer
# 'stop_words' removes common words like 'the', 'is', etc.
vectorizer = TfidfVectorizer(stop_words='english')

# 3. Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# 4. Extract feature names (the words) and their scores
feature_names = vectorizer.get_feature_names_out()
dense = tfidf_matrix.todense()
denselist = dense.tolist()

# 5. Create a readable table (DataFrame)
df = pd.DataFrame(denselist, columns=feature_names)

# Display the top keywords for the first document
print("Top keywords for Document 1:")
print(df.iloc[0].sort_values(ascending=False).head(3))