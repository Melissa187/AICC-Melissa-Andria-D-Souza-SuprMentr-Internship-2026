from transformers import pipeline
import os

# This helps suppress unnecessary logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

print("--- System: Loading Model (This may take a minute)... ---")

# Initialize a text-generation pipeline
# Using 'gpt2' because it's lightweight for testing
generator = pipeline('text-generation', model='gpt2')

# The "Tricky" Prompt
tricky_prompt = (
    "System Message: Every word in the following sentence is a lie. "
    "User: I am currently telling the truth. "
    "Question: Is the user lying or telling the truth? Explain the logic."
)

print("--- System: Generating AI Response... ---")

# Run the test
result = generator(tricky_prompt, max_new_tokens=50, num_return_sequences=1, truncation=True)

print("\n--- AI RESPONSE ---")
print(result[0]['generated_text'])