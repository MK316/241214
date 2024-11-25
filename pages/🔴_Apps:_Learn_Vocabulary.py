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
if 'answers' not in st.session_state:
    st.session_state['answers'] = {}
if 'score' not in st.session_state:
    st.session_state['score'] = 0
if 'remaining' not in st.session_state:
    st.session_state['remaining'] = len(verbs)

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
    verb_count = st.number_input("How many verbs would you like to practice?", min_value=1, max_value=len(verbs), key="verb_count")

    if 'quiz_list' not in st.session_state or st.session_state.quiz_list is None:
        st.session_state.quiz_list = random.sample(list(verbs.items()), k=verb_count)

    if st.button("Start Quiz"):
        # Pick a random verb from the list
        if not st.session_state.quiz_list:
            st.session_state.quiz_list = random.sample(list(verbs.items()), k=verb_count)
        verb, forms = random.choice(st.session_state.quiz_list)
        form_type = random.choice(['past', 'past participle'])
        user_answer = st.text_input(f"What is the {form_type} form of {verb}?", key="user_answer")
        submit_answer = st.button("Check Answer")

        if submit_answer:
            correct_form = forms[0] if form_type == 'past' else forms[1]
            if user_answer.lower().strip() == correct_form.lower():
                st.success("Correct! Good job!")
                st.session_state.score += 1
                st.session_state.remaining -= 1
                st.session_state.quiz_list.remove((verb, forms))
            else:
                st.error("Try again later.")

            if st.session_state.remaining > 0:
                st.write(f"Remaining verbs to practice: {st.session_state.remaining}")
            else:
                st.write("Quiz completed!")

            if st.session_state.quiz_list:
                st.button("Next")
