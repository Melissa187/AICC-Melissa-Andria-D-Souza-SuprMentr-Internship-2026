#Task 1: Movie Review Classifier

 #Build a model:

#Dataset: 20+ sentences

#Classes: Positive / Negative / Neutral

 #Bonus:

#Use TF-IDF instead of CountVectorizer keep simple and good sentences ok

# Movie Review Classifier using TF-IDF + Naive Bayes

# Step 1: Imports
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Dataset (Balanced & Clean)
sentences = [
    # Positive (15)
    "The movie was amazing and very enjoyable",
    "I loved every moment of the film",
    "Fantastic story and brilliant acting",
    "Absolutely wonderful movie experience",
    "One of the best films I have seen",
    "Great performances and excellent direction",
    "The film was inspiring and beautiful",
    "Highly entertaining and well made",
    "A masterpiece with strong emotions",
    "Superb movie with a great plot",
    "Outstanding film with excellent visuals",
    "Brilliant and emotionally engaging",
    "Loved the acting and direction",
    "An impressive and enjoyable movie",
    "A truly fantastic cinematic experience",

    # Negative (15)
    "The movie was terrible and boring",
    "I hated the film completely",
    "Worst movie I have ever seen",
    "Very disappointing and poorly made",
    "The acting was awful and fake",
    "Completely dull and uninteresting",
    "The story made no sense at all",
    "Waste of time and money",
    "Bad movie with weak performances",
    "Extremely boring and slow",
    "Horrible film with terrible acting",
    "Painful to watch and very bad",
    "The movie was annoying and frustrating",
    "Very weak plot and poor direction",
    "I regret watching this movie",

    # Neutral (15)
    "The movie was average",
    "It was an okay film",
    "Nothing special about the movie",
    "It was a typical movie",
    "The film was neither good nor bad",
    "An ordinary movie experience",
    "The story was simple and basic",
    "Just a normal film",
    "It was fine overall",
    "A standard movie with no surprises",
    "The movie was predictable",
    "It had a simple storyline",
    "Nothing new or exciting",
    "The film was straightforward",
    "An average cinematic experience"
]

labels = ["Positive"]*15 + ["Negative"]*15 + ["Neutral"]*15

# Step 3: TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words='english',
    ngram_range=(1,2),
    max_features=1000
)

X = vectorizer.fit_transform(sentences)

# Step 4: Train-Test Split (Stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, labels,
    test_size=0.3,
    random_state=42,
    stratify=labels
)

# Step 5: Model Training
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 6: Evaluation
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Step 7: Cross-validation (more reliable)
scores = cross_val_score(model, X, labels, cv=5)
print("\nCross-validation Accuracy:", scores.mean())

# Step 8: Test Predictions
test_sentences = [
    "This movie was absolutely wonderful",
    "I regret watching this movie",
    "It was just okay",
    "Amazing acting and great story",
    "Very boring and disappointing"
]

test_vectors = vectorizer.transform(test_sentences)
predictions = model.predict(test_vectors)

print("\nPredictions:\n")
for s, p in zip(test_sentences, predictions):
    print(f"{s} --> {p}")