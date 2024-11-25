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

# Initialize or ensure session state is properly set
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.quiz_list = []
    st.session_state.answer_checked = False
    st.session_state.show_next = False
    st.session_state.user_answer = ''

# Start or reset the quiz
def initialize_quiz():
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    st.session_state.current_index = 0
    load_next_verb()

# Load the next verb for the quiz
def load_next_verb():
    if st.session_state.current_index < len(st.session_state.quiz_list):
        verb, forms = st.session_state.quiz_list[st.session_state.current_index]
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
        st.session_state.current_index += 1
        st.session_state.answer_checked = False
    else:
        st.success("Quiz completed! Great job!")
        st.session_state.show_next = False  # No more questions, hide 'Next' button

# Check the user's answer
def check_answer():
    verb, forms = verbs[st.session_state.current_verb]
    correct_form = forms[0] if st.session_state.current_form == 'past' else forms[1]
    if st.session_state.user_answer.strip().lower() == correct_form.lower():
        st.success("Correct! Good job!")
        st.session_state.show_next = True
    else:
        st.error(f"Incorrect. The correct answer was '{correct_form}'. Try again!")
        st.session_state.show_next = False

# Setup UI
st.header("Verb Tense Practice App")
if 'verb_count' not in st.session_state:
    st.session_state.verb_count = 5

st.session_state.verb_count = st.number_input("How many verbs would you like to practice?", min_value=1, max_value=len(verbs), value=st.session_state.verb_count)

if st.button("Start Quiz"):
    initialize_quiz()

if 'current_verb' in st.session_state and st.session_state.current_verb:
    form_type = "past" if st.session_state.current_form == 'past' else "past participle"
    st.write(f"What is the {form_type} form of '{st.session_state.current_verb}'?")
    st.session_state.user_answer = st.text_input("Your answer:", key="user_answer")

    if st.button("Check Answer"):
        check_answer()

    if st.session_state.show_next and st.button("Next"):
        load_next_verb()
