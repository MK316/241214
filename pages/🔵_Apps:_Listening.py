import streamlit as st
from gtts import gTTS
import random

# Updated image URLs
image_urls = {
    "dog": "https://github.com/MK316/241214/raw/main/image/dog.jpg",
    "cat": "https://github.com/MK316/241214/raw/main/image/cat.jpg",
    "bird": "https://github.com/MK316/241214/raw/main/image/bird.jpg"
}

# List of dictation sentences
dictation_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Streamlit is a powerful tool for building apps.",
    "Python is fun to learn and easy to use.",
    "The cat is sleeping on the couch.",
    "Birds are chirping in the morning."
]

# Initialize session state for Tab 2
if "remaining_sentences_tab2" not in st.session_state:
    st.session_state.remaining_sentences_tab2 = dictation_sentences.copy()
if "current_sentence_tab2" not in st.session_state:
    st.session_state.current_sentence_tab2 = None
if "feedback_tab2" not in st.session_state:
    st.session_state.feedback_tab2 = ""
if "show_next_question_tab2" not in st.session_state:
    st.session_state.show_next_question_tab2 = False

# Function to reset for the next dictation sentence
def next_sentence_tab2():
    if st.session_state.remaining_sentences_tab2:
        st.session_state.current_sentence_tab2 = random.choice(st.session_state.remaining_sentences_tab2)
        st.session_state.feedback_tab2 = ""
        st.session_state.show_next_question_tab2 = False
    else:
        st.session_state.current_sentence_tab2 = None

# Start the first sentence if not already set
if not st.session_state.current_sentence_tab2 and st.session_state.remaining_sentences_tab2:
    st.session_state.current_sentence_tab2 = random.choice(st.session_state.remaining_sentences_tab2)

# Tab structure
tab1, tab2, tab3 = st.tabs(["Audio Quiz: Match the Sound", "Dictation Practice", "Fill-in-the-Gap Listening"])

# Tab 2: Dictation Practice
with tab2:
    st.header("Dictation Practice")
    st.write("Listen to the audio and type the sentence you hear.")

    # Check if there are remaining sentences
    if not st.session_state.remaining_sentences_tab2:
        st.success("You have completed all the dictation sentences! Great job!")
    else:
        current_sentence = st.session_state.current_sentence_tab2

        # Generate audio for the current sentence
        tts = gTTS(text=current_sentence, lang="en")
        tts_file = "dictation_audio.mp3"
        tts.save(tts_file)

        # Play the audio
        st.audio(tts_file, format="audio/mp3")

        # Text input for user to type the dictation
        user_input = st.text_area("Type what you hear:", key="dictation_input_tab2")

        # Callback function to check the user's answer
        def check_answer_tab2():
            if user_input.strip().lower() == current_sentence.lower():
                st.session_state.feedback_tab2 = "Correct! Well done!"
                st.session_state.remaining_sentences_tab2.remove(current_sentence)  # Remove completed sentence
            else:
                st.session_state.feedback_tab2 = f"Incorrect. The correct sentence was: '{current_sentence}'."
            st.session_state.show_next_question_tab2 = True

        # Submit Answer button
        st.button("Submit Answer", on_click=check_answer_tab2)

        # Display feedback
        if st.session_state.feedback_tab2:
            st.write(st.session_state.feedback_tab2)

        # Show "Next Sentence" button if feedback is displayed
        if st.session_state.show_next_question_tab2:
            st.button("Next Sentence", on_click=next_sentence_tab2)

# Tab 3: Fill-in-the-Gap Listening
with tab3:
    st.header("Fill-in-the-Gap Listening")
    st.write("Listen to the sentence and fill in the blank.")

    # Generate audio for fill-in-the-gap
    full_sentence = "The cat is sleeping on the couch."
    gap_sentence = "The ___ is sleeping on the couch."
    tts = gTTS(text=gap_sentence, lang="en")
    tts_file = "gap_audio.mp3"
    tts.save(tts_file)

    # Play the audio
    st.audio(tts_file, format="audio/mp3")

    # Text input for missing word
    gap_answer = st.text_input("Fill in the blank:", key="gap_input")

    # Submit button
    if st.button("Submit Answer", key="gap_submit"):
        correct_word = "cat"
        if gap_answer.strip().lower() == correct_word:
            st.success("Correct! Well done.")
        else:
            st.error("Incorrect. Try again!")
            st.write(f"The correct answer is: '{correct_word}'.")
