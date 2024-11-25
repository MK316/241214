import streamlit as st
import pandas as pd
import random

# Step 1: Load CSV file
uploaded_file = st.file_uploader("Upload a CSV file with 'Verb' and 'Regularity' columns", type=['csv'])

if uploaded_file:
    # Read the CSV file
    verb_data = pd.read_csv(uploaded_file)
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

        # Step 2: Tab structure
        tab1, tab2 = st.tabs(["Select Verbs", "Practice"])

        # Tab 1: Select verbs
        with tab1:
            st.header("Select Verbs for Practice")

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
                    # Randomly select a verb if none is currently selected
                    if not st.session_state.current_verb:
                        st.session_state.current_verb = random.choice(st.session_state.test_verbs)

                    # Display the current verb question
                    st.write(f"Is '{st.session_state.current_verb}' regular or irregular?")
                    answer = st.radio(
                        "Choose one:",
                        options=["Regular", "Irregular"],
                        key='answer_radio',
                    )

                    # Submit button for answering
                    if st.button("Submit Answer / Next"):
                        # Get the correct answer
                        correct_answer = verb_data.loc[
                            verb_data['Verb'] == st.session_state.current_verb, 'Regularity'
                        ].values[0]

                        if answer.lower() == correct_answer.lower():
                            st.session_state.feedback = f"Correct: {st.session_state.current_verb} is {correct_answer}."
                            # Create a new list excluding the current verb
                            st.session_state.test_verbs = [
                                verb for verb in st.session_state.test_verbs
                                if verb != st.session_state.current_verb
                            ]
                            st.session_state.current_verb = None  # Reset for the next question
                        else:
                            st.session_state.feedback = f"Incorrect: {st.session_state.current_verb} is {correct_answer}."

                        st.write(st.session_state.feedback)
