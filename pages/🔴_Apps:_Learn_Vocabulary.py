import streamlit as st
import pandas as pd
import random

# Step 1: Load CSV data from URL
data_url = st.text_input("Enter the URL of the CSV file (with 'Verb', 'Regularity', 'Past', and 'PP' columns):")

if data_url:
    try:
        # Read the CSV file
        verb_data = pd.read_csv(data_url)
        required_columns = {'Verb', 'Regularity', 'Past', 'PP'}
        if not required_columns.issubset(set(verb_data.columns)):
            st.error(f"The CSV file must contain the following columns: {', '.join(required_columns)}.")
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
            tab1, tab2, tab3 = st.tabs(["Select Verbs", "Practice", "Practice 2"])

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

            # Tab 2: Practice Regularity
            with tab2:
                st.header("Practice Regularity")

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

            # Tab 3: Practice Past and Past Participle
            with tab3:
                st.header("Practice Past and Past Participle")

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
                            st.write(f"Provide the past and past participle forms of '{st.session_state.current_verb}'.")

                            past_answer = st.text_input("Past:", key="past_answer")
                            pp_answer = st.text_input("Past Participle:", key="pp_answer")

                            # Submit answer button
                            if st.button("Submit Answer"):
                                # Check the answers
                                correct_past = verb_data.loc[
                                    verb_data['Verb'] == st.session_state.current_verb, 'Past'
                                ].values[0]
                                correct_pp = verb_data.loc[
                                    verb_data['Verb'] == st.session_state.current_verb, 'PP'
                                ].values[0]

                                if (past_answer.lower() == correct_past.lower() and
                                        pp_answer.lower() == correct_pp.lower()):
                                    st.session_state.feedback = f"Correct: {st.session_state.current_verb} - {correct_past} - {correct_pp}."
                                    st.session_state.test_verbs.remove(st.session_state.current_verb)
                                else:
                                    st.session_state.feedback = f"Incorrect: {st.session_state.current_verb} - {correct_past} - {correct_pp}."

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
