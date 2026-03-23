#Assignment (21/03/2026)

#Assignment Name : Build a Text Cleaner
#Description : Write code to remove punctuation, lowercase text, remove stopwords and test it.

import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the necessary data for NLTK
nltk.download('punkt')
nltk.download('stopwords')

def text_cleaner(text):
    # 1. Lowercase the text
    text = text.lower()
    
    # 2. Remove Punctuation
    # string.punctuation contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 3. Tokenize (Break into individual words)
    words = word_tokenize(text)
    
    # 4. Remove Stopwords
    # Stopwords are words like 'the', 'is', 'a', etc.
    stop_words = set(stopwords.words('english'))
    cleaned_words = [w for w in words if w not in stop_words]
    
    # Join them back into a clean string for display
    return " ".join(cleaned_words)

# --- TEST IT ---
test_sentences = [
    "The quick brown fox jumps over the lazy dog!",
    "Hello! This is a test sentence, showing how we remove the stop-words.",
    "Natural Language Processing is amazing, isn't it?",
    "I am going to the mall to buy some expensive clothes."
]

print(f"{'ORIGINAL TEXT':<65} | {'CLEANED TEXT'}")
print("-" * 110)

for s in test_sentences:
    cleaned = text_cleaner(s)
    print(f"{s:<65} | {cleaned}")
    