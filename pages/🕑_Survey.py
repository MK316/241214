import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter

# Initialize session state for survey responses if not already done
if 'mc_responses' not in st.session_state:
    st.session_state.mc_responses = []

def store_mc_response(answers):
    st.session_state.mc_responses.append(answers)

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

with tab3:
    st.header("Results of Survey 1")
    if st.session_state.mc_responses:
        # Initialize counters for each question
        counter1 = Counter([response[0] for response in st.session_state.mc_responses])
        counter2 = Counter([response[1] for response in st.session_state.mc_responses])
        counter3 = Counter([response[2] for response in st.session_state.mc_responses])

        # Create subplots for each question's results
        fig, axs = plt.subplots(1, 3, figsize=(18, 6))

        # Pie chart for Question 1
        axs[0].pie(counter1.values(), labels=counter1.keys(), autopct='%1.1f%%', startangle=90)
        axs[0].set_title("Favorite Colors")

        # Bar plot for Question 2
        axs[1].bar(counter2.keys(), counter2.values(), color='g')
        axs[1].set_title("Coffee or Tea")
        axs[1].set_ylabel("Counts")

        # Bar plot for Question 3
        axs[2].bar(counter3.keys(), counter3.values(), color='r')
        axs[2].set_title("Preference for Working from Home")
        axs[2].set_ylabel("Counts")

        # Show the plots
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.write("No responses yet.")
