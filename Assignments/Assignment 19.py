#Assignment (20/03/2026)

#Assignment Name : Text Challenges
#Description :Collect 20 messy sentences and identify slang, emojis, typos; explain preprocessing needed.

import re

# 1. The Slang Dictionary (The "Translator")
slang_dict = {
    "omg": "oh my god",
    "rn": "right now",
    "cant": "cannot",
    "c u": "see you",
    "l8er": "later",
    "hbd": "happy birthday",
    "u": "you",
    "gr8": "great",
    "idk": "i do not know",
    "pls": "please",
    "asap": "as soon as possible",
    "ngl": "not gonna lie",
    "sus": "suspicious",
    "smh": "shaking my head"
}

# 2. 20 Messy Sentences
messy_sentences = [
    "OMG i cant even rn!! 💀🔥",
    "The movie wasss sooo goooddd.",
    "c u l8er at the library!!",
    "This laptop is 🔥 but the battery is 🗑️.",
    "I am goign to the markit now.",
    "hbd!! hope u have a gr8 day!!",
    "WHYYYY IS THIS HAPPENINGGG???",
    "The food was expensive ($$$) but worth it.",
    "Check out https://mall-data.com/deals/123",
    "idk, maybe i'll go... or maybe not...",
    "smh at this service 😒",
    "Pls send the file asap!!!!!",
    "I  love  coding.",
    "Its 2 cold outside today.",
    "ngl that was kinda sus.",
    "Running, ran, runs... all the same.",
    "The @user123 was very helpful.",
    "I'm soooooo tired 😴",
    "Is it 10pm or 10:00 PM?",
    "Worst. Day. Ever. Period."
]

def advanced_clean(text):
    # A. Lowercase
    text = text.lower()
    
    # B. Remove URLs and Mentions
    text = re.sub(r'http\S+|www\S+|\@\w+', '', text)
    
    # C. Remove Emojis and Punctuation (Keep only letters and spaces)
    text = re.sub(r'[^\w\s]', '', text)
    
    # D. Slang Translation (Loop through the dictionary)
    words = text.split()
    translated_words = [slang_dict.get(w, w) for w in words]
    text = " ".join(translated_words)
    
    # E. Remove extra whitespace
    text = " ".join(text.split())
    
    return text

# 3. Execution and Display
print(f"{'BEFORE (Messy)':<45} | {'AFTER (Cleaned & Translated)'}")
print("-" * 100)

for original in messy_sentences:
    cleaned = advanced_clean(original)
    print(f"{original:<45} | {cleaned}")