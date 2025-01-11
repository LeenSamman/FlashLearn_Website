# FlashLearn - Flashcard and Summarization App
## Overview

FlashLearn is a platform designed to assist learners,students and educators by offering 3 primary functionalities:

- Flashcard Generator: Transform your uploaded documents into interactive flashcards with customizable colors and card counts.
- Document Summarizer:  Generate summaries based on your preferred word count and summarization model.
- Interactive UI: A user-friendly interface created with Streamlit, enabling seamless navigation and customization.

  
FlashLearn utilizes  AI technologies, including Google Gemini api, T5 api , and SpaCy, to provide high-quality summaries and flashcards, making learning smarter and more efficient.

**The website serve what we learn in the cloud computing course by utilizing API's ,using python libraries such as SpaCy ,setting up the project with virtual environment and uploading the project on GitHub.**

# GitHub Files Description 
- **Home.py** :	The main entry point of the application. This script sets up the home page and navigation to other pages(1_Flashcards.py , /2_Summarization.py,get_started.py ), these pages located in Pages folder.
- **pages/1_Flashcards.py**: 	Handles the functionality for generating flashcards. Users can upload a document and specify the number of cards to generate.
- **pages/2_Summarization.py**	Manages the document summarization feature. Users can upload a PDF, choose the summarization model, and set parameters.
- **pages/get_started.py** :	The intermediate page for selecting tasks such as document summarization or flashcard generation.
- **requirements.txt**:	Contains a list of all Python dependencies required to run the application. These can be installed via pip install -r requirements.txt.






# Prerequisites

- Python 3.10+
- Virtual Environment (venv) or any environment manager
- Required dependencies listed in requirements.txt



# Installation and Setup

1. Clone the Repository:
git clone https://github.com/LeenSamman/FlashLearn_Website.git
cd FlashLearn_Website

2.  Create the virtual environment:
python -m venv FlashCardsVenv

3.  Activate the virtual environment
On Windows: FlashCardsVenv\Scripts\activate
On macOS/Linux:source FlashCardsVenv/bin/activate

4.  Install Dependencies:

Using the requirements.txt file: pip install -r requirements.txt

5.  Run the Application: 
streamlit run Home.py



# Authors
Beesan Al-Attal
Layan Balbisi
Leen Samman
Zaina Abu-Nasser

# Supervisor
Professor Mu’nis Qasaymeh

