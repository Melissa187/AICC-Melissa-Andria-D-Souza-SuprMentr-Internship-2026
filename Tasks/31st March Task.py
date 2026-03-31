import streamlit as st
import google.generativeai as genai
import os

# 1. Setup API Key (Get yours at aistudio.google.com)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# 2. App UI Configuration
st.set_page_config(page_title="AI Study Assistant", page_icon="📚")
st.title("📚 AI Study Assistant")
st.markdown("Enter a complex topic, and I'll break it down for you.")

# 3. User Input
topic = st.text_input("What do you want to learn today?", placeholder="e.g., Quantum Entanglement, Photosynthesis")

# 4. Logic & API Call
if st.button("Explain It!"):
    if topic:
        with st.spinner(f"Researching {topic}..."):
            try:
                # Initialize the model
                model = genai.GenerativeModel('gemini-pro')
                
                # Create a structured prompt for better results
                prompt = f"""
                You are a world-class tutor. Explain the topic of '{topic}' to a student.
                Include:
                1. A high-level summary.
                2. Three key concepts.
                3. A simple analogy to make it easy to remember.
                """
                
                response = model.generate_content(prompt)
                
                # 5. Display the result
                st.subheader(f"Explanation: {topic}")
                st.write(response.text)
                st.success("Happy Studying!")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic first!")