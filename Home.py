import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="FlashLearn", layout="wide")




def masthead():
    st.markdown(
        """
        <style>
        .masthead {
            background-color: #262730;
            color: white;
            text-align: center;
            padding: 420px 0;
        }
        .masthead .button {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #AA41FE;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }
        .masthead .button:hover {
            background-color: #DBD5F3;
        }

        /* FlashLearn button styles */
        .flashlearn-btn {
            margin: 0;
            height: auto;
            background: transparent;
            padding: 0;
            border: none;
            --border-right: 6px;
            --text-stroke-color: rgba(201, 187, 187, 0.6);
            --animation-color: #8806df;
            --fs-size: 2em;
            letter-spacing: 3px;
            text-decoration: none;
            font-size: 150px;
            font-family: "Arial";
            position: relative;
            color: transparent;
            -webkit-text-stroke: 1px var(--text-stroke-color);
        }
        .flashlearn-btn .hover-text {
            position: absolute;
            box-sizing: border-box;
            content: attr(data-text);
            color: var(--animation-color);
            width: 0%;
            inset: 0;
            border-right: var(--border-right) solid var(--animation-color);
            overflow: hidden;
            transition: 0.5s;
            -webkit-text-stroke: 1px var(--animation-color);
        }
        .flashlearn-btn:hover .hover-text {
            width: 100%;
            filter: drop-shadow(0 0 23px var(--animation-color));
        }
        </style>
        <div class="masthead">
            <button class="flashlearn-btn" data-text="Awesome">
                <span class="actual-text">&nbsp;FlashLearn&nbsp;</span>
                <span aria-hidden="true" class="hover-text">&nbsp;FlashLearn&nbsp;</span>
            </button>
            <br><br><br><br>
            <a class="button" style="font-size:30px;" href="/get_started"><b>Get Started</b></a>
        </div>
        """,
        unsafe_allow_html=True,
    )



# About Section
def about_section():
    st.markdown(
        """
        <style>
        .about-section {
            background-color: #DBD5F3;
            color: #262730;
            padding: 200px 20px;
            
        }
        .about-section h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        .about-section p {
            font-size: 1.25rem;
            margin: 0 auto;
            max-width: 800px;
        }
        </style>
        
        <div class="about-section" style="text-align: justify;">
            <h2> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <b>About Us</b>
            </h2>


            
        Welcome to <b>FlashLearn</b>, your ultimate learning companion 
            designed to make studying smarter and more efficient. Our 
            platform specializes in two essential tools for learners and 
            educators alike: <b>Flashcards<b/> and <b>Document Summarization</b>. Whether
              you're a student preparing for exams, a teacher creating 
              engaging content, or a professional organizing complex 
              information, FlashLearn has you covered.


         With our Flashcard Generator, you can turn any document into
           interactive and impactful flashcards for active recall and 
           retention. Our Summarization Tool simplifies lengthy documents,
             extracting the key points and ideas so you can focus on what 
             truly matters. At FlashLearn, we believe in empowering your 
             learning journey by saving time, enhancing productivity, and
               making education enjoyable. Join us today and unlock the
                 potential of smart learning!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Main Content
masthead()  # Render the Masthead section
about_section()  # Render the About section
