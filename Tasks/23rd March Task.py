#Train a Mini Word2Vec Model
#Task:

#Create your own small dataset of at least 15 sentences on any topic like:

#sports
#food
#movies
#college life

#Train a Word2Vec model and print:

#vector of one word
#5 most similar words for any chosen word
#Expected outcome: understand how embeddings are learned from context.

from gensim.models import Word2Vec

# 1. Create the dataset (15 sentences about College Life)
# Each sentence is a list of lowercase words (tokens)
data = [
    ["college", "students", "study", "hard", "for", "exams"],
    ["the", "professor", "gives", "a", "lecture", "in", "the", "classroom"],
    ["i", "go", "to", "the", "library", "to", "study"],
    ["students", "write", "notes", "during", "the", "lecture"],
    ["the", "campus", "library", "is", "very", "quiet"],
    ["exams", "are", "difficult", "for", "many", "students"],
    ["the", "professor", "explains", "the", "lesson", "clearly"],
    ["we", "have", "a", "group", "study", "session", "at", "the", "cafe"],
    ["the", "university", "campus", "is", "large", "and", "beautiful"],
    ["i", "need", "to", "pass", "my", "final", "exams"],
    ["the", "lecture", "hall", "was", "full", "of", "students"],
    ["books", "are", "available", "at", "the", "library"],
    ["the", "professor", "is", "helpful", "during", "office", "hours"],
    ["living", "on", "campus", "is", "convenient", "for", "students"],
    ["every", "student", "must", "attend", "the", "morning", "lecture"]
]

# 2. Train the Word2Vec Model
# vector_size=10: keeps the math simple for a small task
# min_count=1: ensures no words are ignored
model = Word2Vec(sentences=data, vector_size=10, window=5, min_count=1, workers=4)

# 3. Print the Vector of one word ('exams')
print("--- Vector for the word 'exams' ---")
word_vector = model.wv['exams']
print(word_vector)
print("\n" + "-"*30 + "\n")

# 4. Print 5 most similar words for 'professor'
print("--- 5 most similar words to 'professor' ---")
similar_to_professor = model.wv.most_similar('professor', topn=5)
for word, score in similar_to_professor:
    print(f"{word}: {score:.4f}")