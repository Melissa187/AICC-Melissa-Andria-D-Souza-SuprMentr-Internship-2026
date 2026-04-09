#Assignment (03/04/2026)

#Assignment Name : NLP Mini App
#Description : Build a chatbot, fake news detector, or keyword extractor.

import streamlit as st
from keybert import KeyBERT

# Initialize the model (downloads a small BERT model on first run)
kw_model = KeyBERT()

st.title("🔑 NLP Keyword Extractor")
st.subheader("Extract meaningful keywords using BERT embeddings")

# User Input
text_input = st.text_area("Paste your article or text here:", height=200)

# Extraction Settings
num_keywords = st.slider("Number of keywords to extract:", 1, 10, 5)

if st.button("Extract Keywords"):
    if text_input.strip() != "":
        with st.spinner('Analyzing text...'):
            # Extract keywords
            keywords = kw_model.extract_keywords(text_input, 
                                                keyphrase_ngram_range=(1, 2), 
                                                stop_words='english', 
                                                top_n=num_keywords)
            
            st.write("### Results:")
            for word, score in keywords:
                # Displays keyword and its confidence score
                st.success(f"**{word}** (Confidence: {score:.4f})")
    else:
        st.warning("Please enter some text first!")