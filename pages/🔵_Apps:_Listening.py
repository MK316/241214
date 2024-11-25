import streamlit as st
from gtts import gTTS
import os
import random
from PIL import Image

# Ensure required image files are available in the directory
images = ["https://github.com/MK316/241214/raw/main/image/dog.jpg", "https://github.com/MK316/241214/raw/main/image/cat.jpg", "https://github.com/MK316/241214/raw/main/image/cat.png"]
for img in images:
    if not os.path.exists(img):
        st.warning(f"Image file '{img}' not found in the directory.")

# Tab structure
tab1, tab2, tab3 = st.tabs(["Audio Quiz: Match the Sound", "Dictation Practice", "Fill-in-the-Gap Listening"])

# Tab 1: Audio Quiz - Match the Sound
with tab1:
    st.header("Audio Quiz: Match the Sound")
    st.write("Listen to the audio and choose the image that matches the sound.")

    # Generate random audio
    options = ["dog", "cat", "bird"]
    target = random.choice(options)
    tts = gTTS(text=f"The sound is {target}.", lang="en")
    tts_file = f"{target}_audio.mp3"
    tts.save(tts_file)

    # Play the audio
    st.audio(tts_file, format="audio/mp3")

    # Display image options
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("dog.png", caption="Dog")
        dog_selected = st.radio("Choose:", ["Select"], key="dog_radio")
    with col2:
        st.image("cat.png", caption="Cat")
        cat_selected = st.radio("Choose:", ["Select"], key="cat_radio")
    with col3:
        st.image("bird.png", caption="Bird")
        bird_selected = st.radio("Choose:", ["Select"], key="bird_radio")

    # Submit button
    if st.button("Submit Answer", key="quiz_submit"):
        user_choice = "dog" if "Select" in dog_selected else "cat" if "Select" in cat_selected else "bird"
        if user_choice == target:
            st.success("Correct! Well done.")
        else:
            st.error(f"Incorrect. The correct answer is {target.capitalize()}.")

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
