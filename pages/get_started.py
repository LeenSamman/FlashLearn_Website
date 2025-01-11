import streamlit as st



# Set up the page configuration
st.set_page_config(page_title="Get Started", layout="wide")

# CSS for card styling
st.markdown(
    """
    <style>
    .card {
        width: 500px;
        background: white;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.09);
        padding: 36px;
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 20px;
        transition: transform 0.3s ease-in-out;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .circle {
        width: 96px;
        height: 96px;
        background: #7C3AED; /* Violet-500 */
        border-radius: 50%;
        position: absolute;
        right: -20px;
        top: -28px;
    }
    .circle p {
        position: absolute;
        bottom: 24px;
        left: 28px;
        color: white;
        font-size: 1.5rem; /* 2xl */
        font-weight: bold;
    }
    .icon {
        fill: #7C3AED; /* Violet-500 */
        width: 48px;
        margin-bottom: 16px;
    }
    .card h1 {
        font-weight: bold;
        font-size: 1.25rem; /* xl */
        margin-bottom: 12px;
    }
    .card p {
        font-size: 0.875rem; /* sm */
        color: #71717A; /* Zinc-500 */
        line-height: 1.5rem;
    }
    .button {
        display: inline-block;
        padding: 10px 20px;
        margin-top: 10px;
        background-color: #7C3AED;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-size: 1rem;
        text-align: center;
    }
    .button:hover {
        background-color: #5b2ea6;
    }

    h1{
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 20px;
        color: #7C3AED;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header text
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

    .custom-header {
        text-align: left;
        font-family: 'Anton', sans-serif;
        font-weight: 400;
        font-style: normal;
        color: #4CAF50; /* Green color */
        margin-bottom: 20px;
        
    }
    </style>
    <h2 class="custom-header" style="font-size: 70px;">Choose Your Path To Productivity 🚀</h2>
    """,
    unsafe_allow_html=True,
)

st.write("<br><br><br><br><br>", unsafe_allow_html=True)

# Display cards in columns
cols = st.columns(2)

with cols[0]:
    st.markdown(
        """
        <div class="card">
            <div class="circle">
                <p>01</p>
            </div>
            <div class="icon">
                <svg xmlns="http://www.w3.org/2000/svg" id="Layer_1" data-name="Layer 1" viewBox="0 0 24 24">
                    <path d="m24,6.928v13.072h-11.5v3h5v1H6.5v-1h5v-3H0V4.5c0-1.379,1.122-2.5,2.5-2.5h12.98c-.253.295-.54.631-.856,1H2.5c-.827,0-1.5.673-1.5,1.5v14.5h22v-10.993l1-1.079Zm-12.749,3.094C19.058.891,19.093.855,19.11.838c1.118-1.115,2.936-1.113,4.052.002,1.114,1.117,1.114,2.936,0,4.052l-8.185,8.828c-.116,1.826-1.623,3.281-3.478,3.281h-5.59l.097-.582c.043-.257,1.086-6.16,5.244-6.396Zm2.749,3.478c0-1.379-1.122-2.5-2.5-2.5-2.834,0-4.018,3.569-4.378,5h4.378c1.378,0,2.5-1.121,2.5-2.5Zm.814-1.073l2.066-2.229c-.332-1.186-1.371-2.057-2.606-2.172-.641.749-1.261,1.475-1.817,2.125,1.117.321,1.998,1.176,2.357,2.277Zm.208-5.276c1.162.313,2.125,1.134,2.617,2.229l4.803-5.18c.737-.741.737-1.925.012-2.653-.724-.725-1.908-.727-2.637,0-.069.08-2.435,2.846-4.795,5.606Z"></path>
                </svg>
            </div>
            <h1 style="color: black; font-size:50px;">Summarization</h1>
            <a class="button" href="http://localhost:8501/Summarization" style="color:  #dbd5f3; text-decoration: none;font-size:20px;"><b>Summarize Your Document</b></a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cols[1]:
    st.markdown(
        """
        <div class="card">
            <div class="circle">
                <p>02</p>
            </div>
            <div class="icon">
                <svg xmlns="http://www.w3.org/2000/svg" id="Layer_1" data-name="Layer 1" viewBox="0 0 24 24">
                    <path d="m24,6.928v13.072h-11.5v3h5v1H6.5v-1h5v-3H0V4.5c0-1.379,1.122-2.5,2.5-2.5h12.98c-.253.295-.54.631-.856,1H2.5c-.827,0-1.5.673-1.5,1.5v14.5h22v-10.993l1-1.079Zm-12.749,3.094C19.058.891,19.093.855,19.11.838c1.118-1.115,2.936-1.113,4.052.002,1.114,1.117,1.114,2.936,0,4.052l-8.185,8.828c-.116,1.826-1.623,3.281-3.478,3.281h-5.59l.097-.582c.043-.257,1.086-6.16,5.244-6.396Zm2.749,3.478c0-1.379-1.122-2.5-2.5-2.5-2.834,0-4.018,3.569-4.378,5h4.378c1.378,0,2.5-1.121,2.5-2.5Zm.814-1.073l2.066-2.229c-.332-1.186-1.371-2.057-2.606-2.172-.641.749-1.261,1.475-1.817,2.125,1.117.321,1.998,1.176,2.357,2.277Zm.208-5.276c1.162.313,2.125,1.134,2.617,2.229l4.803-5.18c.737-.741.737-1.925.012-2.653-.724-.725-1.908-.727-2.637,0-.069.08-2.435,2.846-4.795,5.606Z"></path>
                </svg>
            </div>
            <h1 style="color: black;font-size:50px;">Flashcards</h1>
            <a class="button" href="http://localhost:8501/Flashcards" style="color:  #dbd5f3 ; text-decoration: none;font-size:20px;"><b>Create Your Flashcards</b></a>

        </div>
        """,
        unsafe_allow_html=True,
    )
