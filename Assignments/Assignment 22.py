from textblob import TextBlob

# 1. Your 5 Test Reviews
reviews = [
    "The cinematography was breathtaking and the acting was top-notch!",
    "I've never been so bored in my life. A total waste of money.",
    "The plot was okay, but the ending felt a bit rushed and confusing.",
    "An absolute masterpiece! Every scene was perfection.",
    "It was an average movie. Not great, but not terrible either."
]

print("--- Movie Review Sentiment Analysis ---")

# 2. Analyze each review
for i, review in enumerate(reviews, 1):
    analysis = TextBlob(review)
    score = analysis.sentiment.polarity
    
    # 3. Categorize based on score
    if score > 0.1:
        sentiment = "POSITIVE ✅"
    elif score < -0.1:
        sentiment = "NEGATIVE ❌"
    else:
        sentiment = "NEUTRAL 😐"
    
    print(f"Review {i}: {sentiment} (Score: {score:.2f})")
    print(f"Text: {review}\n")