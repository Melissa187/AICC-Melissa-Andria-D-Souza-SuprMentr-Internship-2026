#Add PDF Upload Support

#Hint:

#pip install PyPDF2

#Extract text from PDF and analyze.import PyPDF2

import PyPDF2
import os
from collections import Counter
import re

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a given PDF file path."""
    text = ""
    try:
        if not os.path.exists(pdf_path):
            return f"Error: The file '{pdf_path}' was not found."

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Iterate through all pages
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        
        return text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_text(text):
    """Performs basic NLP analysis on the extracted text."""
    if not text or text.startswith("Error:"):
        print("No valid text to analyze.")
        return

    # 1. Basic Stats
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)
    char_count = len(text)
    
    # 2. Keyword Frequency (excluding short words like 'the', 'is', etc.)
    stopwords = {'the', 'and', 'is', 'in', 'it', 'of', 'to', 'for', 'with', 'on', 'a', 'an'}
    filtered_words = [w for w in words if w not in stopwords and len(w) > 2]
    common_keywords = Counter(filtered_words).most_common(5)

    # Output Results
    print("\n" + "="*40)
    print("       PDF ANALYSIS REPORT")
    print("="*40)
    print(f"Total Words:      {word_count}")
    print(f"Total Characters: {char_count}")
    print("-" * 40)
    print("Top Keywords:")
    for word, count in common_keywords:
        print(f" - {word}: {count} times")
    print("-" * 40)
    print("Text Preview (First 250 chars):")
    print(f"{text[:250]}...")
    print("="*40 + "\n")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Change 'sample.pdf' to the name of a PDF file in your folder
    target_pdf = "Melissa Andria D'Souza Final Resume.pdf" 
    
    print(f"Opening: {target_pdf}...")
    content = extract_text_from_pdf(target_pdf)
    
    if content.startswith("Error:"):
        print(content)
    else:
        analyze_text(content)