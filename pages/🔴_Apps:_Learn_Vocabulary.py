import streamlit as st
import random

# Sample verb dictionary
verbs = {
    'ask': ['asked', 'asked'],
    'be': ['was/were', 'been'],
    'begin': ['began', 'begun'],
    'call': ['called', 'called'],
    'choose': ['chose', 'chosen']
}

# Functions for quiz logic
def start_quiz():
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    st.session_state.remaining = len(st.session_state.quiz_list)
    get_next_verb()

def get_next_verb():
    if st.session_state.quiz_list:
        verb, forms = st.session_state.quiz_list.pop()
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
    else:
        st.session_state.current_verb = None
        st.success("Quiz completed! Great job!")

def check_answer():
    verb, forms = st.session_state.current_verb, verbs[st.session_state.current_verb]
    correct_form = forms[0] if st.session_state.current_form == 'past' else forms[1]
    if st.session_state.user_answer.lower().strip() == correct_form.lower():
        st.success("Correct! Good job!")
        st.session_state.score += 1
    else:
        st.error("Incorrect. Try again!")
    get_next_verb()

# Setting up the app interface with tabs
tabs = st.tabs(["Verb List", "Verb Practice"])

with tabs[0]:
    st.header("List of English Verbs")
    for verb, forms in verbs.items():
        st.write(f"**{verb}** - Past: {forms[0]}, Past Participle: {forms[1]}")

with tabs[1]:
    st.header("Verb Practice")
    if 'verb_count' not in st.session_state:
        st.session_state.verb_count = 5  # Default number of verbs to practice
    verb_count = st.number_input("How many verbs would you like to practice?", min_value=1, max_value=len(verbs), value=st.session_state.verb_count)
    st.session_state.verb_count = verb_count  # Update session state

    if st.button("Start Quiz"):
        start_quiz()

    if 'current_verb' in st.session_state and st.session_state.current_verb:
        form_type = st.session_state.current_form
        st.write(f"What is the {form_type} form of '{st.session_state.current_verb}'?")
        st.session_state.user_answer = st.text_input("Your answer:")
        if st.button("Check Answer"):
            check_answer()
