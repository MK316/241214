import streamlit as st
import random

# Define verbs dictionary
verbs = {
    'ask': ['asked', 'asked'],
    'be': ['was/were', 'been'],
    'begin': ['began', 'begun'],
    'call': ['called', 'called'],
    'choose': ['chose', 'chosen']
}

def initialize_quiz():
    # Ensure the verb count is initialized from the session state
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    st.session_state.current_index = 0
    load_next_verb()

def load_next_verb():
    if st.session_state.quiz_list:
        verb, forms = st.session_state.quiz_list.pop(0)
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
    else:
        st.session_state.current_verb = None
        st.success("Quiz completed! Great job!")

def check_answer():
    verb, forms = verbs[st.session_state.current_verb]
    correct_form = forms[0] if st.session_state.current_form == 'past' else forms[1]
    if st.session_state.user_answer.lower().strip() == correct_form.lower():
        st.success("Correct! Good job!")
    else:
        st.error(f"Incorrect. The correct answer was '{correct_form}'. Try again!")

st.header("Verb Tense Practice App")
# Initialize verb_count if not already in session state
if 'verb_count' not in st.session_state:
    st.session_state.verb_count = 5

# Setup number input with key, which automatically manages session state
verb_count = st.number_input("How many verbs would you like to practice?", min_value=1, max_value=len(verbs), value=st.session_state.verb_count, key='verb_count')

if st.button("Start Quiz"):
    initialize_quiz()

if 'current_verb' in st.session_state and st.session_state.current_verb:
    form_type = "past" if st.session_state.current_form == 'past' else "past participle"
    st.write(f"What is the {form_type} form of '{st.session_state.current_verb}'?")
    st.session_state.user_answer = st.text_input("Your answer:", key="user_answer")

    if st.button("Check Answer"):
        check_answer()

    if st.session_state.current_verb and st.button("Next"):
        load_next_verb()
