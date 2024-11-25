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

# Initialize or reset session state variables
if 'quiz_list' not in st.session_state:
    st.session_state.quiz_list = []
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'current_verb' not in st.session_state:
    st.session_state.current_verb = None
if 'current_form' not in st.session_state:
    st.session_state.current_form = None
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

# Function to initialize the quiz
def initialize_quiz():
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    st.session_state.current_index = 0
    st.session_state.quiz_started = True
    load_next_verb()

# Function to load the next verb
def load_next_verb():
    if st.session_state.current_index < len(st.session_state.quiz_list):
        verb, forms = st.session_state.quiz_list[st.session_state.current_index]
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
        st.session_state.current_index += 1
    else:
        st.session_state.current_verb = None
        st.success("Quiz completed! Great job!")
        st.session_state.quiz_started = False

# Function to check the answer
def check_answer():
    if st.session_state.current_verb:
        verb, forms = verbs[st.session_state.current_verb]
        correct_form = forms[0] if st.session_state.current_form == 'past' else forms[1]
        user_answer = st.session_state.user_answer.strip().lower()
        if user_answer == correct_form.lower():
            st.success("Correct! Good job!")
        else:
            st.error(f"Incorrect. The correct answer was '{correct_form}'.")

# Main layout
st.header("Verb Tense Practice App")

# Verb count input (rely entirely on key)
st.number_input(
    "How many verbs would you like to practice?",
    min_value=1,
    max_value=len(verbs),
    value=5,
    key="verb_count"
)

# Start quiz button
if st.button("Start Quiz"):
    initialize_quiz()

# Display current question and answer input
if st.session_state.quiz_started and st.session_state.current_verb:
    form_type = "past" if st.session_state.current_form == 'past' else "past participle"
    st.write(f"What is the {form_type} form of '{st.session_state.current_verb}'?")
    st.text_input("Your answer:", key="user_answer")  # Managed directly by Streamlit

    # Check answer button
    if st.button("Check Answer"):
        check_answer()

    # Next question button
    if st.button("Next"):
        load_next_verb()
