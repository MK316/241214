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
if 'correct_answer' not in st.session_state:
    st.session_state.correct_answer = None
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False

# Function to initialize the quiz
def initialize_quiz():
    st.session_state.quiz_list = random.sample(list(verbs.items()), k=st.session_state.verb_count)
    st.session_state.current_index = 0
    st.session_state.quiz_started = True
    st.session_state.show_feedback = False
    load_next_verb()

# Function to load the next verb
def load_next_verb():
    if st.session_state.current_index < len(st.session_state.quiz_list):
        verb, forms = st.session_state.quiz_list[st.session_state.current_index]
        st.session_state.current_verb = verb
        st.session_state.current_form = random.choice(['past', 'past participle'])
        st.session_state.correct_answer = forms[0] if st.session_state.current_form == 'past' else forms[1]
        st.session_state.show_feedback = False  # Reset feedback state for the new question
    else:
        st.session_state.current_verb = None
        st.success("Quiz completed! Great job!")
        st.session_state.quiz_started = False

# Function to check the answer
def check_answer():
    if st.session_state.current_verb:
        user_answer = st.session_state.user_answer.strip().lower()
        correct_answer = st.session_state.correct_answer.strip().lower()
        if user_answer == correct_answer:
            st.success("Correct! Good job!")
        else:
            st.error(f"Incorrect. The correct answer was '{st.session_state.correct_answer}'. Keep trying—you'll get it next time!")
        st.session_state.show_feedback = True  # Show feedback

# Function to move to the next question
def move_to_next_question():
    st.session_state.current_index += 1
    load_next_verb()

# Main layout
st.header("Verb Tense Practice App")

# Verb count input
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
    if not st.session_state.show_feedback:
        # Show the current question
        form_type = "past" if st.session_state.current_form == 'past' else "past participle"
        st.write(f"What is the {form_type} form of '{st.session_state.current_verb}'?")
        st.text_input("Your answer:", key="user_answer")  # Managed directly by Streamlit

        # Check answer button
        if st.button("Check Answer"):
            check_answer()
    else:
        # Show feedback and automatically load the next question
        st.button("Next Question", on_click=move_to_next_question)
