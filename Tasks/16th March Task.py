import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# 1. Dataset
corpus = [
    'I love this movie',
    'This movie is terrible',
    'Amazing acting',
    'Worst film ever'
]

# --- 1. Apply Bag of Words (BoW) ---
# We use CountVectorizer to convert text to a matrix of token counts
cv = CountVectorizer()
bow_data = cv.fit_transform(corpus)
feature_names = cv.get_feature_names_out()

# Visualize BoW using Pandas
df_bow = pd.DataFrame(bow_data.toarray(), columns=feature_names)

# --- 2. Apply TF-IDF ---
# We use TfidfVectorizer to reflect word importance
tfidf = TfidfVectorizer()
tfidf_data = tfidf.fit_transform(corpus)

# Visualize TF-IDF using Pandas
df_tfidf = pd.DataFrame(tfidf_data.toarray(), columns=feature_names)

# --- 3. Print Matrices ---
print("-" * 30)
print("BAG OF WORDS MATRIX")
print("-" * 30)
print(df_bow)

print("\n" + "-" * 30)
print("TF-IDF MATRIX (Normalized)")
print("-" * 30)
print(df_tfidf.round(3)) # Rounded for readability

# --- 4. Comparison Summary ---
print("\n" + "-" * 30)
print("COMPARISON RESULTS")
print("-" * 30)
print("1. BoW shows raw frequency (integers). Note how 'this' and 'movie' appear in multiple rows.")
print("2. TF-IDF shows weighted importance (decimals).")
print("3. In TF-IDF, 'movie' has a lower score than 'amazing' because 'movie' appears in 50% of the docs,")
print("   making it less unique for sentiment than 'amazing' which only appears once.")