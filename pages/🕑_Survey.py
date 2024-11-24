import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

# Initialize session state for survey responses if not already done
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
    st.header("Survey 2 - Text Input")
    text_response = st.text_area("Describe your ideal work environment:")
    if st.button("Submit Survey 2"):
        store_text_response(text_response)
        st.success("Survey 2 submitted successfully!")

with tab3:
    st.header("Results of Survey 1")
    if st.session_state.mc_responses:
        # Create subplots for each question's results
        fig, axs = plt.subplots(3, 1, figsize=(8, 12))
        
        # Plotting results using Seaborn
        sns.countplot(x=[response[0] for response in st.session_state.mc_responses], ax=axs[0], palette='viridis')
        axs[0].set_title("Favorite Colors")
        
        sns.countplot(x=[response[1] for response in st.session_state.mc_responses], ax=axs[1], palette='Set2')
        axs[1].set_title("Coffee or Tea")
        
        sns.countplot(x=[response[2] for response in st.session_state.mc_responses], ax=axs[2], palette='Set1')
        axs[2].set_title("Work From Home Preference")

        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.write("No responses yet.")

with tab4:
    st.header("Word Cloud from Survey 2 Responses")
    if st.session_state.text_responses:
        from wordcloud import WordCloud
        
        combined_text = " ".join(st.session_state.text_responses)
        wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(combined_text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.write("No text responses yet.")
