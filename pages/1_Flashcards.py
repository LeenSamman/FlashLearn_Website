import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as genai

# Configure the Google Generative AI API
genai.configure(api_key="AIzaSyCSOkYoJdDUckd9RYmJlQoTmOmsC4hiPj8")  # Replace with your actual API key

# Streamlit UI
st.title("Generate  Flashcards 🎈")
st.write("Upload a PDF, specify the number of flashcards, and customize their design.")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# Input for number of flashcards
num_of_cards = st.slider("Select the number of flashcards to generate:", min_value=1, max_value=25, step=1)

###############################
st.write("### Customize Flashcard Colors")

# Create two columns
cols = st.columns(2)

# Labels and default colors for the color pickers
labels = ["Choose the main card color:", "Choose the hover card color (lighter shade):"]
default_colors = ["#FFA07A", "#FFCCCB"]

# Initialize an empty dictionary to store selected colors
selected_colors = {}

# Add color pickers to the columns using a loop
for i, col in enumerate(cols):
    with col:
        selected_colors[i] = st.color_picker(labels[i], default_colors[i])

# Access selected colors
card_color = selected_colors[0]
hover_color = selected_colors[1]



###############################
# CSS Styling
st.markdown(
    f"""
    <style>
    .flip-card {{
        background-color: transparent;
        width: 1000px;
        height: 200px;
        perspective: 1000px;
        margin: 20px auto;
    }}
    .flip-card-inner {{
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }}
    .flip-card:hover .flip-card-inner {{
        transform: rotateY(180deg);
    }}
    .flip-card-front, .flip-card-back {{
        position: absolute;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border: 2px solid {card_color};
        border-radius: 1rem;
        box-shadow: 0 8px 14px 0 rgba(0, 0, 0, 0.2);
    }}
    .flip-card-front {{
        background: {card_color};
        color: black;
        font-size: 25px;
    }}
    .flip-card-back {{
        background: {hover_color};
        color: black;
        font-size: 25px;
        transform: rotateY(180deg);

    }}
    </style>
    """,
    unsafe_allow_html=True,
)

if uploaded_file is not None:
    # Extract text from the PDF
    text = ""
    pdf_reader = PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Text preprocessing and chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)



    # Button to generate flashcards
    if st.button("Generate Flashcards!"):
        try:
            # Use the Google Generative AI API to generate flashcards
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(
                f"Using the following text chunks, generate {num_of_cards} interactive and impactful QA flashcards. "
                "Focus on making the questions thought-provoking and the answers concise yet meaningful for active recall. "
                "Provide only the QA pairs in the following indexed format for consistency: \n\n"
                "1. Q: [Your question here]\n"
                "   A: [Your answer here]\n\n"
                "2. Q: [Your question here]\n"
                "   A: [Your answer here]\n\n"
                "... \n\n"
                "Ensure there is no additional text, framing, or commentary beyond the indexed QA pairs:\n\n"
                f"{chunks}"
            )



            # Parse the flashcards
            flashcards = response.text.split("\n\n")  # Split by double newline
            for flashcard in flashcards:
                if flashcard.strip():  # Skip empty lines
                    try:
                        parts = flashcard.split("A:")  # Split into Question and Answer
                        question = parts[0].replace("Q:", "").strip()
                        answer = parts[1].strip()

                        # Display each flashcard using HTML
                        st.markdown(
                            f"""
                            <div class="flip-card">
                                <div class="flip-card-inner">
                                    <div class="flip-card-front">
                                        <h3>{question}</h3>
                                    </div>
                                    <div class="flip-card-back">
                                        <p>{answer}</p>
                                    </div>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    except Exception as e:
                        st.warning(f"Malformed flashcard skipped: {flashcard}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
