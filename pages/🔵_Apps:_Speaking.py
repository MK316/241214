import streamlit as st

# Function to create a green button
def green_button(label, url):
    button_html = f"""
    <a href="{url}" target="_blank">
        <button style="
            color: white;
            background-color: #3399FF;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;">
            {label}
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)

# Add tabs
tab1, tab2, tab3, tab4= st.tabs(["📍Pronunciation-Checker", "📍Yes-no question", "📍Foreign accent", "📍Borrowing words"])

# Tab 1: Python
with tab1:
    st.header("1: PronunciationChecker")
    st.write("")
    green_button("Click to open the APP", "https://mk-316-pronunciationfeedback.hf.space/")



# Tab 2: Coding
with tab2:
    st.header("Tab 2: Yes-no question")
    st.write("Convert a statement (be-verb) to a yes-no question.")
    green_button("Click to open the APP", "https://MK-316-yesno-converter.hf.space")


# Tab 3: Github
with tab3:
    st.header("3: Foreign accents")
    st.write("English words with foreign accents")
    green_button("Click to open the APP", "https://MK-316-foreignaccent.hf.space")

# Tab 4: Github
with tab4:
    st.header("4: Borrowing words")
    st.write("Commonly used English words in Korean vs. American accents")
    green_button("Click to open the APP", "https://MK-316-korean-english.hf.space")

