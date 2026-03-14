#Assignment (10/03/2026)

#Assignment Name : Spam Classifier Thinking
#Description : Design a spam detection system: features, data needed, possible mistakes.

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# ---------------------------------
# STEP 1: Create a Sample Dataset
# ---------------------------------

data = {
    "Message": [
        "Win a free iPhone now",
        "Congratulations you won a lottery",
        "Meeting at 10am tomorrow",
        "Project submission deadline today",
        "Claim your free reward now",
        "Let's have lunch today",
        "Limited time offer click now",
        "Can you send the report"
    ],
    
    "Label": [
        "spam",
        "spam",
        "ham",
        "ham",
        "spam",
        "ham",
        "spam",
        "ham"
    ]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# ---------------------------------
# STEP 2: Convert Labels to Numbers
# ---------------------------------

df["Label"] = df["Label"].map({"ham":0, "spam":1})

# ---------------------------------
# STEP 3: Split Data
# ---------------------------------

X = df["Message"]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------
# STEP 4: Convert Text to Numbers
# ---------------------------------

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ---------------------------------
# STEP 5: Train Model
# ---------------------------------

model = MultinomialNB()
model.fit(X_train_vec, y_train)

# ---------------------------------
# STEP 6: Test Model
# ---------------------------------

predictions = model.predict(X_test_vec)

print("\nAccuracy:", accuracy_score(y_test, predictions))

# ---------------------------------
# STEP 7: Test with New Message
# ---------------------------------

new_message = ["Congratulations! You won a free ticket"]
new_message_vec = vectorizer.transform(new_message)

prediction = model.predict(new_message_vec)

if prediction[0] == 1:
    print("Spam Message")
else:
    print("Not Spam")



