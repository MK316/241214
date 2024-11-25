import streamlit as st
import pandas as pd
import random

# Step 1: Load CSV data from URL
data_url = "https://raw.githubusercontent.com/MK316/241214/refs/heads/main/data/verb_sample.csv"

if data_url:
    try:
        # Read the CSV file
        verb_data = pd.read_csv(data_url)
        if 'Verb' not in verb_data.columns or 'Regularity' not in verb_data.columns:
            st.error("The CSV file must have 'Verb' and 'Regularity' columns.")
        else:
            # Initialize session state
            if 'selected_verbs' not in st.session_state:
                st.session_state.selected_verbs = []
            if 'test_verbs' not in st.session_state:
                st.session_state.test_verbs = []
            if 'current_verb' not in st.session_state:
                st.session_state.current_verb = None
            if 'feedback' not in st.session_state:
                st.session_state.feedback = ""
            if 'answered' not in st.session_state:
                st.session_state.answered = False  # Track whether feedback is shown
            if 'show_next_button' not in st.session_state:
                st.session_state.show_next_button = False  # Track whether "Next" button should appear

            # Step 2: Tab structure
            tab1, tab2 = st.tabs(["Select Verbs", "Practice"])

            # Tab 1: Select verbs
            with tab1:
                st.header("Select Verbs for Practice")

                # Reset selection button
                if st.button("Reset Selection"):
                    st.session_state.selected_verbs = []
                    st.session_state.test_verbs = []
                    st.session_state.current_verb = None
                    st.session_state.feedback = ""
                    st.session_state.answered = False
                    st.session_state.show_next_button = False
                    # Reset all checkboxes
                    for i, row in verb_data.iterrows():
                        st.session_state[f'verb_checkbox_{i}'] = False
                    st.success("Selections have been reset. You can choose new verbs.")

                # Display verbs with checkboxes
                selected_verb_indices = []
                for i, row in verb_data.iterrows():
                    verb = row['Verb']
                    if st.checkbox(verb, key=f'verb_checkbox_{i}'):
                        selected_verb_indices.append(i)

                # Submit button to collect selected verbs
                if st.button("Submit Selection"):
                    st.session_state.selected_verbs = verb_data.loc[selected_verb_indices, 'Verb'].tolist()
                    st.session_state.test_verbs = st.session_state.selected_verbs.copy()
                    st.session_state.current_verb = None
                    st.session_state.feedback = ""
                    st.session_state.answered = False
                    st.session_state.show_next_button = False
                    st.success(f"Selected verbs: {st.session_state.selected_verbs}")

            # Tab 2: Practice
            with tab2:
                st.header("Practice Verbs")

                if not st.session_state.selected_verbs:
                    st.warning("No verbs selected. Please go to Tab 1 and select verbs first.")
                else:
                    if not st.session_state.test_verbs:
                        st.success("Completed! You practiced all the selected verbs.")
                    else:
                        # Show the current verb
                        if not st.session_state.current_verb:
                            st.session_state.current_verb = random.choice(st.session_state.test_verbs)
                            st.session_state.feedback = ""
                            st.session_state.answered = False
                            st.session_state.show_next_button = False

                        if not st.session_state.answered:
                            # Display the current question
                            st.write(f"Is '{st.session_state.current_verb}' regular or irregular?")
                            answer = st.radio(
                                "Choose one:",
                                options=["Regular", "Irregular"],
                                key="answer_radio"
                            )

                            # Submit answer button
                            if st.button("Submit Answer"):
                                # Check the answer
                                correct_answer = verb_data.loc[
                                    verb_data['Verb'] == st.session_state.current_verb, 'Regularity'
                                ].values[0]

                                if answer.lower() == correct_answer.lower():
                                    st.session_state.feedback = f"Correct: {st.session_state.current_verb} is {correct_answer}."
                                    st.session_state.test_verbs.remove(st.session_state.current_verb)
                                else:
                                    st.session_state.feedback = f"Incorrect: {st.session_state.current_verb} is {correct_answer}."

                                st.session_state.answered = True
                                st.session_state.show_next_button = True

                        # Show feedback
                        if st.session_state.answered:
                            st.write(st.session_state.feedback)

                        # Next question button
                        if st.session_state.show_next_button:
                            if st.button("Next Question"):
                                st.session_state.current_verb = None
                                st.session_state.feedback = ""
                                st.session_state.answered = False
                                st.session_state.show_next_button = False
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
