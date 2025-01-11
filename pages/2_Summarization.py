import streamlit as st
from PyPDF2 import PdfReader
import os
import re
from heapq import nlargest
from collections import Counter

# Gemini imports
import google.generativeai as genai

# T5 imports
from transformers import pipeline

# SpaCy imports
import spacy

# Helper functions
def extract_text_from_pdf(file):
    """Extract text from an uploaded PDF file."""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def summarize_with_spacy(text, num_words):
    """Summarize text using SpaCy, ensuring the summary doesn't exceed num_words."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    sentences = list(doc.sents)

    word_frequencies = Counter()
    for word in doc:
        if not word.is_stop and not word.is_punct and word.pos_ in {"NOUN", "VERB", "ADJ"}:
            word_frequencies[word.text.lower()] += 1

    max_frequency = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency

    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in sentence:
            if word.text.lower() in word_frequencies:
                sentence_scores[i] = sentence_scores.get(i, 0) + word_frequencies[word.text.lower()]

    # Sort sentences based on score and select top sentences
    top_sentences = nlargest(len(sentences), sentence_scores, key=sentence_scores.get)
    
    # Assemble the summary and ensure it doesn't exceed num_words
    summary = []
    word_count = 0
    for i in sorted(top_sentences):
        sentence = str(sentences[i])
        sentence_word_count = len(sentence.split())
        
        # Check if adding the sentence would exceed the word limit
        if word_count + sentence_word_count <= num_words:
            summary.append(sentence)
            word_count += sentence_word_count
        else:
            # Break if word count exceeds the desired limit
            break

    # Join the summary and return
    return " ".join(summary)

def summarize_with_t5(text, summary_length):
    """Summarize text using T5."""
    summarization_pipeline = pipeline("summarization", model="t5-small")
    chunks = re.split(r'(?<=[.!?])\s+', text)
    summaries = []

    for chunk in chunks:
        if chunk:
            max_len = min(summary_length, len(chunk.split()))
            summary = summarization_pipeline(chunk, max_length=max_len, min_length=max_len // 2, do_sample=False)
            summaries.append(summary[0]['summary_text'])

    return " ".join(summaries)

def configure_gemini(api_key):
    """Configure the Gemini model."""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

def summarize_with_gemini(model, text, summary_length):
    """Summarize text using Gemini."""
    prompt = f"Summarize the following text in about {summary_length} words:\n{text}"
    response = model.generate_content(prompt)
    return response.text

# Streamlit app
def main():
    st.title("Summarize Your Text 🤺")

    # Sidebar options
    st.sidebar.header("Settings")
    model_choice = st.sidebar.selectbox("Choose a summarization model", ["SpaCy", "T5", "Gemini"])

    if model_choice == "Gemini":
        api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

    # Set minimum summary length to 65
    summary_length = st.sidebar.slider("Summary length (words or sentences)", min_value=65, max_value=500, value=65)

    # File upload
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
        #st.write("Extracted Text:", text[:500], "...")  # Display a snippet of the text

        if st.button("Summarize"):
            if model_choice == "SpaCy":
                summary = summarize_with_spacy(text, summary_length)
            elif model_choice == "T5":
                summary = summarize_with_t5(text, summary_length)
            elif model_choice == "Gemini":
                if api_key:
                    model = configure_gemini(api_key)
                    summary = summarize_with_gemini(model, text, summary_length)
                else:
                    st.error("Please enter a valid Gemini API key.")
                    return

            st.subheader("Summary")
            st.write(summary)

if __name__ == "__main__":
    main()
