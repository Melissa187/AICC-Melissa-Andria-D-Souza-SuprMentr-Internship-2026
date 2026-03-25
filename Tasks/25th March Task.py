#Task 1: Build Smarter Text Generator

 #Improve mini LLM:

#Add:
#Sentence input from user
#Better prediction logic
#Generate 10-word sentence

import random
import re

class SenseMakerLLM:
    def __init__(self):
        self.chain = {}
        self.words = []

    def train(self, text):
        self.words = re.findall(r'\w+', text.lower())
        # Look at sequences of 3 words (Trigrams)
        for i in range(len(self.words) - 2):
            key = (self.words[i], self.words[i+1])
            next_word = self.words[i+2]
            if key not in self.chain:
                self.chain[key] = []
            self.chain[key].append(next_word)

    def generate(self, prompt, length=10):
        input_w = re.findall(r'\w+', prompt.lower())
        if len(input_w) < 1: return "Enter a word!"
        
        # Start with your words
        res = input_w
        
        while len(res) < length:
            # Look at the LAST TWO words to predict the next one
            state = tuple(res[-2:]) if len(res) >= 2 else (res[-1], random.choice(self.words))
            
            if state in self.chain:
                res.append(random.choice(self.chain[state]))
            else:
                # If it gets lost, it grabs a random word it knows
                res.append(random.choice(self.words))
                
        return " ".join(res[:length]).capitalize() + "."

bot = SenseMakerLLM()
# Give it a bit more "sensible" data
bot.train("""
    Melissa is a brilliant student who loves coding. 
    Python is a great language for building cool things.
    The quick brown fox jumps over the lazy dog.
    A pretty girl is someone who is smart and kind.
""")

user_input = input("Enter a phrase: ")
print(f"Result: {bot.generate(user_input)}")