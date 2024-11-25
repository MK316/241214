import streamlit as st
import random

# Define verbs
verbs = {
    'ask': ['asked', 'asked'],
    'be': ['was/were', 'been'],
    'begin': ['began', 'begun'],
    'call': ['called', 'called'],
    'choose': ['chose', 'chosen']
}

# Ensure proper initialization of session variables
if 'verb_count' not in st.session_state:
    st.session_state.verb_count = 5
if 'quiz_list' not in st.session_state:
    st.session_state.quiz_list = []
if 'current_verb' not in st.session_state:
    st.session_state.current_verb = None
if 'current_form' not in st.session_state:
    st.session_state.current_form = None
if 'answer_checked' not in st.session_state:
    st.session_state.answer_checked = False
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = ''

def start_quiz():
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    st.session_state.remaining = len(st.session_state.quiz_list)
    get_next_verb()

def get_next_verb():
    if st.session_state.quiz_list:
        verb, forms = st.session_state.quiz_list.pop(0)
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
        st.session_state.answer_checked = False
        st.session_state.user_answer = ''
    else:
        st.session_state.current_verb = None
        st.success("Quiz completed! Great job!")

def check_answer():
    verb, forms = st.session_state.current_verb, verbs[st.session_state.current_verb]
    correct_form = forms[0] if st.session_state.current_form == 'past' else forms[1]
    if st.session_state.user_answer.lower().strip() == correct_form.lower():
        st.success("Correct! Good job!")
        st.session_state.answer_checked = True
    else:
        st.error("Incorrect. Try again!")

tabs = st.tabs(["Verb List", "Verb Practice"])

with tabs[0]:
    st.header("List of English Verbs")
    for verb, forms in verbs.items():
        st.write(f"**{verb}** - Past: {forms[0]}, Past Participle: {forms[1]}")

with tabs[1]:
    st.header("Verb Practice")
    if st.button("Start Quiz"):
        start_quiz()

    if st.session_state.current_verb:
        form_type = "past" if st.session_state.current_form == 'past' else "past participle"
        st.write(f"What is the {form_type} form of '{st.session_state.current_verb}'?")
        st.session_state.user_answer = st.text_input("Your answer:", value=st.session_state.user_answer)

        if st.button("Check Answer"):
            check_answer()

        if st.session_state.answer_checked:
            if st.button("Next"):
                get_next_verb()
