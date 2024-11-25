import streamlit as st
import pandas as pd
import random

# Step 1: Load CSV data from URL
data_url = "https://raw.githubusercontent.com/MK316/241214/refs/heads/main/data/verb_sample.csv"
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
            if 'test_verbs_tab2' not in st.session_state:
                st.session_state.test_verbs_tab2 = []
            if 'test_verbs_tab3' not in st.session_state:
                st.session_state.test_verbs_tab3 = []
            if 'current_verb_tab2' not in st.session_state:
                st.session_state.current_verb_tab2 = None
            if 'current_verb_tab3' not in st.session_state:
                st.session_state.current_verb_tab3 = None
            if 'feedback_tab2' not in st.session_state:
                st.session_state.feedback_tab2 = ""
            if 'feedback_tab3' not in st.session_state:
                st.session_state.feedback_tab3 = ""
            if 'answered_tab2' not in st.session_state:
                st.session_state.answered_tab2 = False
            if 'answered_tab3' not in st.session_state:
                st.session_state.answered_tab3 = False
            if 'show_next_button_tab2' not in st.session_state:
                st.session_state.show_next_button_tab2 = False
            if 'show_next_button_tab3' not in st.session_state:
                st.session_state.show_next_button_tab3 = False

            # Tab structure
            tab1, tab2, tab3 = st.tabs(["Select Verbs", "Practice Regularity", "Practice Forms"])

            # Tab 1: Select verbs
            with tab1:
                st.header("Select Verbs for Practice")

                if st.button("Reset Selection", key="reset_selection"):
                    st.session_state.selected_verbs = []
                    st.session_state.test_verbs_tab2 = []
                    st.session_state.test_verbs_tab3 = []
                    st.session_state.current_verb_tab2 = None
                    st.session_state.current_verb_tab3 = None
                    st.success("Selections have been reset. You can choose new verbs.")

                selected_verb_indices = []
                for i, row in verb_data.iterrows():
                    verb = row['Verb']
                    if st.checkbox(verb, key=f'verb_checkbox_{i}'):
                        selected_verb_indices.append(i)

                if st.button("Submit Selection", key="submit_selection"):
                    st.session_state.selected_verbs = verb_data.loc[selected_verb_indices, 'Verb'].tolist()
                    st.session_state.test_verbs_tab2 = st.session_state.selected_verbs.copy()
                    st.session_state.test_verbs_tab3 = st.session_state.selected_verbs.copy()
                    st.success(f"Selected verbs: {st.session_state.selected_verbs}")

            # Tab 2: Practice Regularity
            with tab2:
                st.header("Practice Regularity")

                if not st.session_state.selected_verbs:
                    st.warning("No verbs selected. Please go to Tab 1 and select verbs first.")
                else:
                    if not st.session_state.test_verbs_tab2:
                        st.success("Completed! You practiced all the selected verbs.")
                    else:
                        if not st.session_state.current_verb_tab2:
                            st.session_state.current_verb_tab2 = random.choice(st.session_state.test_verbs_tab2)
                            st.session_state.feedback_tab2 = ""
                            st.session_state.answered_tab2 = False
                            st.session_state.show_next_button_tab2 = False

                        if not st.session_state.answered_tab2:
                            st.write(f"Is '{st.session_state.current_verb_tab2}' regular or irregular?")
                            answer = st.radio("Choose one:", ["Regular", "Irregular"], key="answer_radio_tab2")

                            if st.button("Submit Answer", key="submit_answer_tab2"):
                                correct_answer = verb_data.loc[
                                    verb_data['Verb'] == st.session_state.current_verb_tab2, 'Regularity'
                                ].values[0]
                                if answer.lower() == correct_answer.lower():
                                    st.session_state.feedback_tab2 = f"Correct: {st.session_state.current_verb_tab2} is {correct_answer}."
                                    st.session_state.test_verbs_tab2.remove(st.session_state.current_verb_tab2)
                                else:
                                    st.session_state.feedback_tab2 = f"Incorrect: {st.session_state.current_verb_tab2} is {correct_answer}."

                                st.session_state.answered_tab2 = True
                                st.session_state.show_next_button_tab2 = True

                        if st.session_state.answered_tab2:
                            st.write(st.session_state.feedback_tab2)

                            if st.button("Next Question", key="next_question_tab2"):
                                st.session_state.current_verb_tab2 = None
                                st.session_state.feedback_tab2 = ""
                                st.session_state.answered_tab2 = False
                                st.session_state.show_next_button_tab2 = False

            # Tab 3: Practice Forms
            with tab3:
                st.header("Practice Past and Past Participle")

                if not st.session_state.selected_verbs:
                    st.warning("No verbs selected. Please go to Tab 1 and select verbs first.")
                else:
                    if not st.session_state.test_verbs_tab3:
                        st.success("Completed! You practiced all the selected verbs.")
                    else:
                        if not st.session_state.current_verb_tab3:
                            st.session_state.current_verb_tab3 = random.choice(st.session_state.test_verbs_tab3)
                            st.session_state.feedback_tab3 = ""
                            st.session_state.answered_tab3 = False
                            st.session_state.show_next_button_tab3 = False

                        if not st.session_state.answered_tab3:
                            st.write(f"Provide the past and past participle forms of '{st.session_state.current_verb_tab3}'.")

                            past_answer = st.text_input("Past:", key="past_answer_tab3")
                            pp_answer = st.text_input("Past Participle:", key="pp_answer_tab3")

                            if st.button("Submit Answer", key="submit_answer_tab3"):
                                correct_past = verb_data.loc[
                                    verb_data['Verb'] == st.session_state.current_verb_tab3, 'Past'
                                ].values[0]
                                correct_pp = verb_data.loc[
                                    verb_data['Verb'] == st.session_state.current_verb_tab3, 'PP'
                                ].values[0]

                                if (past_answer.lower() == correct_past.lower() and
                                        pp_answer.lower() == correct_pp.lower()):
                                    st.session_state.feedback_tab3 = f"Correct: {st.session_state.current_verb_tab3} - {correct_past} - {correct_pp}."
                                    st.session_state.test_verbs_tab3.remove(st.session_state.current_verb_tab3)
                                else:
                                    st.session_state.feedback_tab3 = f"Incorrect: {st.session_state.current_verb_tab3} - {correct_past} - {correct_pp}."

                                st.session_state.answered_tab3 = True
                                st.session_state.show_next_button_tab3 = True

                        if st.session_state.answered_tab3:
                            st.write(st.session_state.feedback_tab3)

                            if st.button("Next Question", key="next_question_tab3"):
                                st.session_state.current_verb_tab3 = None
                                st.session_state.feedback_tab3 = ""
                                st.session_state.answered_tab3 = False
                                st.session_state.show_next_button_tab3 = False

    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
