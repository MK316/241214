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

# Initialize session state variables
if 'verb_count' not in st.session_state:
    st.session_state.verb_count = 5  # Default verb count
if 'current_verb' not in st.session_state:
    st.session_state.current_verb = None
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

def start_quiz():
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    get_next_verb()

def get_next_verb():
    if st.session_state.quiz_list:
        verb, forms = st.session_state.quiz_list.pop(0)
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
    else:
        st.success("Quiz completed! Great job!")
        st.session_state.quiz_started = False

def check_answer(user_answer, correct_form):
    if user_answer.lower().strip() == correct_form.lower():
        st.success("Correct! Good job!")
        get_next_verb()
    else:
        st.error("Incorrect. Try again!")

tabs = st.tabs(["Verb List", "Verb Practice"])

with tabs[0]:
    st.header("List of English Verbs")
    for verb, forms in verbs.items():
        st.write(f"**{verb}** - Past: {forms[0]}, Past Participle: {forms[1]}")

with tabs[1]:
    st.header("Verb Practice")
    if not st.session_state.quiz_started:
        verb_count = st.number_input("How many verbs would you like to practice?", min_value=1, max_value=len(verbs), value=st.session_state.verb_count)
        if st.button("Start Quiz"):
            st.session_state.verb_count = verb_count
            start_quiz()
            st.session_state.quiz_started = True

    if st.session_state.quiz_started and st.session_state.current_verb:
        form_type = "past" if st.session_state.current_form == 'past' else "past participle"
        st.write(f"What is the {form_type} form of '{st.session_state.current_verb}'?")
        user_answer = st.text_input("Your answer:")
        if st.button("Check Answer"):
            verb, forms = st.session_state.current_verb, verbs[st.session_state.current_verb]
            correct_form = forms[0] if form_type == 'past' else forms[1]
            check_answer(user_answer, correct_form)
