import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from wordcloud import WordCloud
import streamlit.components.v1 as components  # For embedding YouTube videos
from pydub import AudioSegment
import io
from gtts import gTTS  # Google Text-to-Speech
import tempfile

# Existing functions
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Additional functions for new features
def convert_to_wav(audio_file):
    try:
        sound = AudioSegment.from_mp3(audio_file)
        buffer = io.BytesIO()
        sound.export(buffer, format="wav")
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.error(f"An error occurred: {str(e)}. This format may require external dependencies not available in this environment.")

def text_to_speech(text, language):
    lang_code = {
        "🇰🇷 Korean": {"lang": "ko", "tld": None},
        "🇺🇸 English (AmE)": {"lang": "en", "tld": "us"},
        "🇬🇧 English (BrE)": {"lang": "en", "tld": "co.uk"},
        "🇫🇷 French": {"lang": "fr", "tld": None},
        "🇪🇸 Spanish": {"lang": "es", "tld": None},
        "🇨🇳 Chinese": {"lang": "zh", "tld": None},
        "🇯🇵 Japanese": {"lang": "ja", "tld": None}
    }
    try:
        lang = lang_code[language]["lang"]
        tld = lang_code[language]["tld"]
        if tld:
            tts = gTTS(text=text, lang=lang, tld=tld)
        else:
            tts = gTTS(text=text, lang=lang)
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Streamlit tabs including new tabs for Multi-TTS and Generating melody
tabs = st.tabs(["📈 QR", "⏳ Timer", "👥 Grouping", "⛅ Word Cloud", "🔊 Multi-TTS", "🎵 Generating Melody"])

# Existing tabs' content...

# New Tab 5: Multi-Text to Speech Application
with tabs[4]:
    st.header("Multi-Text to Speech Application")
    st.write("Enter text and choose a language to generate the corresponding audio.")
    user_input = st.text_area("Enter text here...")
    language = st.selectbox("Language", ["🇰🇷 Korean", "🇺🇸 English (AmE)", "🇬🇧 English (BrE)", "🇫🇷 French", "🇪🇸 Spanish", "🇨🇳 Chinese", "🇯🇵 Japanese"])
    if st.button('Generate Speech'):
        if user_input:
            audio_file_path = text_to_speech(user_input, language)
            if audio_file_path:
                with open(audio_file_path, "rb") as audio_file:
                    st.audio(audio_file, format='audio/mp3')

# New Tab 6: Generate your own melody
with tabs[5]:
    st.header("Generate your own melody")
    st.caption("Using this app, the user can generate a downloadable audio file.")
    st.caption("The sequence 'do, re, mi, fa...' is called the solfege system, or solfège, a method used to teach pitch and sight singing in music. Each syllable corresponds to a note on a musical scale, allowing for easy vocalization and learning of musical notation.")
    appurl = "https://melody-play.streamlit.app/"
    button_html = f"<a href='{appurl}' target='_blank'><button style='color: black; background-color: #CCFF99; border: none; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>Open Melody App</button></a>"
    st.markdown(button_html, unsafe_allow_html=True)
