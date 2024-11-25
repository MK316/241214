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

def start_quiz():
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    st.session_state.remaining = len(st.session_state.quiz_list)
    st.session_state.answer_checked = False  # Ensure this is initialized here
    get_next_verb()

def get_next_verb():
    if st.session_state.quiz_list:
        verb, forms = st.session_state.quiz_list.pop(0)
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
        st.session_state.answer_checked = False  # Reset check flag
    else:
        st.session_state.current_verb = None
        st.success("Quiz completed! Great job!")

def check_answer():
    verb, forms = st.session_state.current_verb, verbs[st.session_state.current_verb]
    correct_form = forms[0] if st.session_state.current_form == 'past' else forms[1]
    if st.session_state.user_answer.lower().strip() == correct_form.lower():
        st.success("Correct! Good job!")
        st.session_state.answer_checked = True  # Mark the answer as checked
    else:
        st.error("Incorrect. Try again!")

# Streamlit app layout
st.header("Verb Tense Practice App")
if 'quiz_list' not in st.session_state:
    st.session_state.verb_count = 5
    st.session_state.answer_checked = False  # Initialize here to ensure it's always available

verb_count = st.number_input("How many verbs would you like to practice?", min_value=1, max_value=len(verbs), value=st.session_state.verb_count)
st.session_state.verb_count = verb_count

if st.button("Start Quiz") or 'current_verb' not in st.session_state:
    start_quiz()

if 'current_verb' in st.session_state and st.session_state.current_verb:
    form_type = "past" if st.session_state.current_form == 'past' else "past participle"
    question = f"What is the {form_type} form of '{st.session_state.current_verb}'?"
    st.write(question)
    user_answer = st.text_input("Your answer:", key="user_answer")

    if st.button("Check Answer"):
        check_answer()

    if st.session_state.get('answer_checked', False):  # Use get to safely check the flag
        if st.button("Next"):
            get_next_verb()
