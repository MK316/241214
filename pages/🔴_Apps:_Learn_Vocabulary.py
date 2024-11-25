import streamlit as st
import random

# Data Initialization
verbs = {
    'ask': ['asked', 'asked'],
    'be': ['was/were', 'been'],
    'begin': ['began', 'begun'],
    'call': ['called', 'called'],
    'choose': ['chose', 'chosen']
}

# Initialize session states
if 'current_verb' not in st.session_state:
    st.session_state['current_verb'] = None
if 'current_form' not in st.session_state:
    st.session_state['current_form'] = None
if 'quiz_list' not in st.session_state:
    st.session_state['quiz_list'] = []
if 'score' not in st.session_state:
    st.session_state['score'] = 0
if 'remaining' not in st.session_state:
    st.session_state['remaining'] = len(verbs)

# Function to start or continue the quiz
def start_quiz():
    if not st.session_state.quiz_list:
        st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
        st.session_state.remaining = len(st.session_state.quiz_list)
    verb, forms = random.choice(st.session_state.quiz_list)
    st.session_state.current_verb = verb
    st.session_state.current_form = random.choice(['past', 'past participle'])

# Function to check the answer
def check_answer():
    verb, forms = st.session_state.current_verb, verbs[st.session_state.current_verb]
    correct_form = forms[0] if st.session_state.current_form == 'past' else forms[1]
    if st.session_state.user_answer.lower().strip() == correct_form.lower():
        st.success("Correct! Good job!")
        st.session_state.score += 1
        st.session_state.remaining -= 1
        st.session_state.quiz_list.remove((verb, forms))
    else:
        st.error("Try again later.")

# App Layout with Tabs
tabs = st.tabs(["Verb List", "Verb Practice"])

# Tab 1: Verb List
with tabs[0]:
    st.header("List of English Verbs")
    for verb, forms in verbs.items():
        st.write(f"**{verb}** - Past: {forms[0]}, Past Participle: {forms[1]}")

# Tab 2: Verb Practice
with tabs[1]:
    st.header("Verb Practice")
    st.session_state.verb_count = st.number_input("How many verbs would you like to practice?", min_value=1, max_value=len(verbs), key="verb_count", on_change=start_quiz)

    if st.session_state.current_verb:
        st.write(f"What is the {st.session_state.current_form} form of {st.session_state.current_verb}?")
        st.session_state.user_answer = st.text_input("Your answer:", key="user_answer")
    
    if st.button("Check Answer", on_click=check_answer):
        if st.session_state.remaining > 0:
            st.write(f"Remaining verbs to practice: {st.session_state.remaining}")
            start_quiz()  # Get next question ready
        else:
            st.success("Quiz completed! Great job!")
