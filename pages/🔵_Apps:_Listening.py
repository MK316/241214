import streamlit as st
from gtts import gTTS
import random

# Updated image URLs
image_urls = {
    "dog": "https://github.com/MK316/241214/raw/main/image/dog.jpg",
    "cat": "https://github.com/MK316/241214/raw/main/image/cat.jpg",
    "bird": "https://github.com/MK316/241214/raw/main/image/bird.jpg"
}

# Example dictation sentences
dictation_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Streamlit is a powerful tool for building apps.",
    "Python is fun to learn and easy to use.",
    "The cat is sleeping on the couch.",
    "Birds are chirping in the morning."
]

# Example sentences with blanks for Tab 3
fill_in_the_gap_data = [
    {"full_sentence": "The cat is sleeping on the couch.", "gap_sentence": "The ___ is sleeping on the couch.", "answers": ["cat"]},
    {"full_sentence": "The dog barked at the stranger.", "gap_sentence": "The ___ barked at the stranger.", "answers": ["dog"]},
    {"full_sentence": "Birds are chirping in the morning.", "gap_sentence": "___ are chirping in the morning.", "answers": ["birds"]},
]

# Initialize session state for Tab 1
if "target" not in st.session_state:
    st.session_state.target = random.choice(list(image_urls.keys()))
if "feedback_tab1" not in st.session_state:
    st.session_state.feedback_tab1 = ""

# Initialize session state for Tab 2
if "remaining_sentences_tab2" not in st.session_state:
    st.session_state.remaining_sentences_tab2 = dictation_sentences.copy()
if "current_sentence_tab2" not in st.session_state:
    st.session_state.current_sentence_tab2 = None
if "feedback_tab2" not in st.session_state:
    st.session_state.feedback_tab2 = ""
if "show_next_question_tab2" not in st.session_state:
    st.session_state.show_next_question_tab2 = False

# Initialize session state for Tab 3
if "remaining_sentences_tab3" not in st.session_state:
    st.session_state.remaining_sentences_tab3 = fill_in_the_gap_data.copy()
if "current_sentence_tab3" not in st.session_state:
    st.session_state.current_sentence_tab3 = None
if "feedback_tab3" not in st.session_state:
    st.session_state.feedback_tab3 = ""
if "show_next_question_tab3" not in st.session_state:
    st.session_state.show_next_question_tab3 = False

# Functions to reset state for each tab
def next_question_tab1():
    st.session_state.target = random.choice(list(image_urls.keys()))
    st.session_state.feedback_tab1 = ""

def next_question_tab2():
    if st.session_state.remaining_sentences_tab2:
        st.session_state.current_sentence_tab2 = random.choice(st.session_state.remaining_sentences_tab2)
        st.session_state.feedback_tab2 = ""
        st.session_state.show_next_question_tab2 = False
    else:
        st.session_state.current_sentence_tab2 = None

def next_question_tab3():
    if st.session_state.remaining_sentences_tab3:
        st.session_state.current_sentence_tab3 = random.choice(st.session_state.remaining_sentences_tab3)
        st.session_state.feedback_tab3 = ""
        st.session_state.show_next_question_tab3 = False
    else:
        st.session_state.current_sentence_tab3 = None

# Start the first question if not already set
if not st.session_state.current_sentence_tab2 and st.session_state.remaining_sentences_tab2:
    next_question_tab2()
if not st.session_state.current_sentence_tab3 and st.session_state.remaining_sentences_tab3:
    next_question_tab3()

# Tab structure
tab1, tab2, tab3 = st.tabs(["🎧 Audio Quiz: Match the Sound", "📝 Dictation Practice", "🎧 Fill-in-the-Gap Listening"])

# Tab 1: Audio Quiz - Match the Sound
with tab1:
    st.header("🎧 Audio Quiz: Match the Image with the Sentence")
    st.write("Listen to the sentence and choose the image that matches it.")

    # Sentences associated with each image
    sentences = {
        "dog": "A dog is in the park.",
        "cat": "A cat is sitting on the mat.",
        "bird": "A bird is on the tree."
    }

    # Generate audio for the current target sentence
    target = st.session_state.target
    target_sentence = sentences[target]
    tts = gTTS(text=target_sentence, lang="en")
    tts_file = f"{target}_sentence_audio.mp3"
    tts.save(tts_file)

    # Play the audio
    st.audio(tts_file, format="audio/mp3")

    # Display image options
    def select_image(selected_target):
        if selected_target == target:
            st.session_state.feedback_tab1 = f"Correct! The sentence was: '{target_sentence}'."
        else:
            st.session_state.feedback_tab1 = f"Incorrect. The correct answer was: '{target_sentence}'."
        st.session_state.target = random.choice(list(image_urls.keys()))  # Load a new target for the next question

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(image_urls["dog"], caption="Dog")
        if st.button("Select Dog", key="select_dog"):
            select_image("dog")

    with col2:
        st.image(image_urls["cat"], caption="Cat")
        if st.button("Select Cat", key="select_cat"):
            select_image("cat")

    with col3:
        st.image(image_urls["bird"], caption="Bird")
        if st.button("Select Bird", key="select_bird"):
            select_image("bird")

    # Display feedback
    if "feedback_tab1" in st.session_state and st.session_state.feedback_tab1:
        st.write(st.session_state.feedback_tab1)


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

        # Text input for user's answer
        user_input = st.text_area("Type what you hear:", key="dictation_input_tab2")

        # Callback function to check the user's answer
        def check_answer_tab2():
            if user_input.strip().lower() == current_sentence.lower():
                st.session_state.feedback_tab2 = "Correct! Well done."
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
            st.button("Next Sentence", on_click=next_question_tab2)

# Tab 3: Fill-in-the-Gap Listening
with tab3:
    st.header("Fill-in-the-Gap Listening")
    st.write("""
        Listen to the sentence and fill in the blanks. 
        Type your answers for the blanks in the text input box below.
        Separate multiple words with commas (e.g., word1, word2, word3).
    """)

    # Check if there are remaining sentences
    if not st.session_state.remaining_sentences_tab3:
        st.success("You have completed all the fill-in-the-gap questions! Great job!")
    else:
        current_sentence_data = st.session_state.current_sentence_tab3
        full_sentence = current_sentence_data["full_sentence"]
        gap_sentence = current_sentence_data["gap_sentence"]
        correct_answers = current_sentence_data["answers"]

        # Generate audio for the full sentence
        tts = gTTS(text=full_sentence, lang="en")
        tts_file = "fill_gap_audio.mp3"
        tts.save(tts_file)

        # Play the audio
        st.audio(tts_file, format="audio/mp3")

        # Display the sentence with blanks
        st.write(f"Sentence: {gap_sentence}")

        # Text input for user's answers
        user_input = st.text_area("Fill in the blanks (separate answers with commas):", key="gap_input_tab3")

        # Callback function to check the user's answer
        def check_answer_tab3():
            user_answers = [word.strip().lower() for word in user_input.split(",")]
            if user_answers == correct_answers:
                st.session_state.feedback_tab3 = "Correct! Well done."
                st.session_state.remaining_sentences_tab3.remove(current_sentence_data)  # Remove completed question
            else:
                st.session_state.feedback_tab3 = f"Incorrect. The correct answer(s) is/are: {', '.join(correct_answers)}."
            st.session_state.show_next_question_tab3 = True

        # Submit Answer button
        st.button("Submit Answer", on_click=check_answer_tab3, key="submit_answer_tab3")

        # Display feedback
        if st.session_state.feedback_tab3:
            st.write(st.session_state.feedback_tab3)

        # Callback function to reset for the next question
        def next_question_tab3():
            if st.session_state.remaining_sentences_tab3:
                st.session_state.current_sentence_tab3 = random.choice(st.session_state.remaining_sentences_tab3)
                st.session_state.feedback_tab3 = ""
                st.session_state.show_next_question_tab3 = False
            else:
                st.session_state.current_sentence_tab3 = None

        # Show "Next Question" button if feedback is displayed
        if st.session_state.show_next_question_tab3:
            st.button("Next Question", on_click=next_question_tab3, key="next_question_tab3")
