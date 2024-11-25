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

def initialize_quiz():
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    st.session_state.remaining = len(st.session_state.quiz_list)
    st.session_state.current_index = 0  # Initialize index for quiz_list
    st.session_state.answer_checked = False
    st.session_state.show_next = False  # Controls the display of the Next button

def get_next_verb():
    if st.session_state.remaining > 0:
        verb, forms = st.session_state.quiz_list[st.session_state.current_index]
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
        st.session_state.answer_checked = False
        st.session_state.user_answer = ''
        st.session_state.current_index += 1
        st.session_state.remaining -= 1
    else:
        st.session_state.current_verb = None
        st.success("Quiz completed! Great job!")

def check_answer():
    verb, forms = verbs[st.session_state.current_verb]
    correct_form = forms[0] if st.session_state.current_form == 'past' else forms[1]
    if st.session_state.user_answer.lower().strip() == correct_form.lower():
        st.success("Correct! Good job!")
        st.session_state.show_next = True  # Allow the Next button to be shown
    else:
        st.error("Incorrect. Try again!")
        st.session_state.show_next = False

st.header("Verb Tense Practice App")
if 'verb_count' not in st.session_state:
    st.session_state.verb_count = 5
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

if st.button("Start Quiz"):
    initialize_quiz()
    st.session_state.quiz_started = True

if st.session_state.quiz_started:
    if st.session_state.current_verb:
        form_type = "past" if st.session_state.current_form == 'past' else "past participle"
        question = f"What is the {form_type} form of '{st.session_state.current_verb}'?"
        st.write(question)
        st.session_state.user_answer = st.text_input("Your answer:", key="user_answer")

        if st.button("Check Answer"):
            check_answer()

        if st.session_state.show_next and st.button("Next"):
            get_next_verb()
