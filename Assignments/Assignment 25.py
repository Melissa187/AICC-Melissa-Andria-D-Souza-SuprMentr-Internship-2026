#Assignment (30/03/2026)

#Assignment Name : Prompt Engineer
#Description : Write prompts for resume, business idea, study plan and compare weak vs strong prompts.

import sys

print("1. Script started...")

try:
    from transformers import pipeline
    print("2. Libraries imported successfully.")
except ImportError:
    print("ERROR: transformers not found. Run: pip install transformers torch")
    sys.exit()

print("3. Initializing model (this is usually where it hangs)...")
# We use 'cpu' explicitly to avoid GPU errors
generator = pipeline('text-generation', model='gpt2', device=-1) 

# Your Assignment Prompts
prompts = [
    ("Weak", "Write a resume."),
    ("Strong", "Professional Resume for a Junior Web Developer. Focus on: HTML, CSS, JavaScript. Format: Summary and Skills list.")
]

for label, p_text in prompts:
    print(f"\n--- Testing {label} Prompt ---")
    result = generator(p_text, max_new_tokens=40, num_return_sequences=1, truncation=True)
    print(result[0]['generated_text'])

print("\n4. Script finished successfully!")