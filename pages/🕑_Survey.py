import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Initialize session states if not already initialized
if 'mc_responses' not in st.session_state:
    st.session_state.mc_responses = []
if 'text_responses' not in st.session_state:
    st.session_state.text_responses = []

def store_mc_response(answers):
    st.session_state.mc_responses.append(answers)

def store_text_response(text):
    st.session_state.text_responses.append(text)

# Define the app structure with tabs
tab1, tab2, tab3, tab4 = st.tabs(["Survey 1", "Survey 2", "Results 1", "Results 2"])

with tab1:
    st.header("Survey 1 - Multiple Choice Questions")
    q1 = st.radio("What is your favorite color?", ("Blue", "Green", "Red"))
    q2 = st.radio("Coffee or Tea?", ("Coffee", "Tea"))
    q3 = st.radio("Do you prefer working from home?", ("Yes", "No"))
    if st.button("Submit Survey 1"):
        store_mc_response((q1, q2, q3))
        st.success("Survey 1 submitted successfully!")

with tab2:
    st.header("Survey 2 - Text Input for Word Cloud")
    text_response = st.text_area("What words best describe your work environment?")
    if st.button("Submit Survey 2"):
        store_text_response(text_response)
        st.success("Survey 2 submitted successfully!")

with tab3:
    st.header("Results of Survey 1")
    if st.session_state.mc_responses:
        st.write("Responses collected:")
        for response in st.session_state.mc_responses:
            st.write(response)
    else:
        st.write("No responses yet.")

with tab4:
    st.header("Word Cloud from Survey 2 Responses")
    if st.session_state.text_responses:
        combined_text = " ".join(st.session_state.text_responses)
        wordcloud = WordCloud(width=800, height=400).generate(combined_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.write("No text responses yet.")

