import streamlit as st
from gtts import gTTS
import random

# Updated image URLs
image_urls = {
    "dog": "https://github.com/MK316/241214/raw/main/image/dog.jpg",
    "cat": "https://github.com/MK316/241214/raw/main/image/cat.jpg",
    "bird": "https://github.com/MK316/241214/raw/main/image/bird.jpg"
}

# Tab structure
tab1, tab2, tab3 = st.tabs(["Audio Quiz: Match the Sound", "Dictation Practice", "Fill-in-the-Gap Listening"])

# Tab 1: Audio Quiz - Match the Sound
with tab1:
    st.header("Audio Quiz: Match the Sound")
    st.write("Listen to the audio and choose the image that matches the sound.")

    # Initialize session state for target and feedback
    if "target" not in st.session_state:
        st.session_state.target = random.choice(list(image_urls.keys()))
    if "feedback" not in st.session_state:
        st.session_state.feedback = ""

    # Generate audio for the target
    target = st.session_state.target
    tts = gTTS(text=f"The sound is {target}.", lang="en")
    tts_file = f"{target}_audio.mp3"
    tts.save(tts_file)

    # Play the audio
    st.audio(tts_file, format="audio/mp3")

    # Display image options with selection buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(image_urls["dog"], caption="Dog")
        if st.button("Select Dog", key="select_dog"):
            if target == "dog":
                st.session_state.feedback = "Correct! The sound was 'Dog'."
            else:
                st.session_state.feedback = f"Incorrect. The correct answer was '{target.capitalize()}'."
            st.session_state.target = random.choice(list(image_urls.keys()))  # Update target

    with col2:
        st.image(image_urls["cat"], caption="Cat")
        if st.button("Select Cat", key="select_cat"):
            if target == "cat":
                st.session_state.feedback = "Correct! The sound was 'Cat'."
            else:
                st.session_state.feedback = f"Incorrect. The correct answer was '{target.capitalize()}'."
            st.session_state.target = random.choice(list(image_urls.keys()))  # Update target

    with col3:
        st.image(image_urls["bird"], caption="Bird")
        if st.button("Select Bird", key="select_bird"):
            if target == "bird":
                st.session_state.feedback = "Correct! The sound was 'Bird'."
            else:
                st.session_state.feedback = f"Incorrect. The correct answer was '{target.capitalize()}'."
            st.session_state.target = random.choice(list(image_urls.keys()))  # Update target

    # Display feedback
    if st.session_state.feedback:
        st.write(st.session_state.feedback)

# Tab 2: Dictation Practice
with tab2:
    st.header("Dictation Practice")
    st.write("Listen to the sentence and type what you hear.")

    # Generate audio for dictation
    dictation_sentence = "The quick brown fox jumps over the lazy dog."
    tts = gTTS(text=dictation_sentence, lang="en")
    tts_file = "dictation_audio.mp3"
    tts.save(tts_file)

    # Play the audio
    st.audio(tts_file, format="audio/mp3")

    # Text input for user's dictation
    user_input = st.text_area("Type what you hear:", key="dictation_input")

    # Submit button
    if st.button("Check Answer", key="dictation_submit"):
        if user_input.strip().lower() == dictation_sentence.lower():
            st.success("Correct! Well done.")
        else:
            st.error("Incorrect. Try again!")
            st.write(f"The correct sentence is: '{dictation_sentence}'.")

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
