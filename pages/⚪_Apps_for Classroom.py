import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from wordcloud import WordCloud
import streamlit.components.v1 as components
from pydub import AudioSegment
import io
from gtts import gTTS
import tempfile

# Function to create word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Convert MP3 to WAV function
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
        "🇬🇧 English (BrE)": {"lang": "en", "tld": "co.uk"},  # Use tld for UK English
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

# QR Code tab
with tabs[0]:
    st.subheader("QR Code Generator")
    qr_link = st.text_input("Enter a link to generate a QR code:")
    if st.button("Generate QR Code"):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_link)
        qr.make(fit=True)
        qr_img = qr.make_image(fill='black', back_color='white')
        qr_img = qr_img.convert('RGB').resize((600, 600))
        st.image(qr_img, caption="Generated QR Code", use_column_width=False, width=400)

# Timer tab
with tabs[1]:
    huggingface_space_url = "https://MK-316-mytimer.hf.space"
    st.components.v1.html(f"""
        <iframe src="{huggingface_space_url}" width="100%" height="600px" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """, height=600)

# Grouping tab
with tabs[2]:
    st.subheader("👥 Grouping Tool")
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    members_per_group = st.number_input("Members per Group", min_value=1, value=5)
    if st.button("Submit"):
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            df = df.sample(frac=1).reset_index(drop=True)
            grouped = np.array_split(df, np.ceil(len(df) / members_per_group))
            st.write(grouped)

# Word Cloud tab
with tabs[3]:
    st.subheader("🌌 Word Cloud Generator")
    user_input = st.text_area("Enter text to generate a word cloud:")
    if st.button("Generate Word Cloud"):
        if user_input.strip():
            wordcloud = create_wordcloud(user_input)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)

# Multi-Text to Speech Application
with tabs[4]:
    st.header("Multi-Text to Speech Application")
    user_input = st.text_area("Enter text here...")
    language = st.selectbox("Language", ["🇰🇷 Korean", "🇺🇸 English (AmE)", "🇬🇧 English (BrE)", "🇫🇷 French", "🇪🇸 Spanish", "🇨🇳 Chinese", "🇯🇵 Japanese"])
    if st.button('Generate Speech'):
        if user_input:
            audio_file_path = text_to_speech(user_input, language)
            if audio_file_path:
                with open(audio_file_path, "rb") as audio_file:
                    st.audio(audio_file, format='audio/mp3')

# Generate your own melody tab
with tabs[5]:
    st.header("Generate your own melody")
    appurl = "https://melody-play.streamlit.app/"
    button_html = f"<a href='{appurl}' target='_blank'><button style='color: black; background-color: #CCFF99; border: none; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>Open Melody App</button></a>"
    st.markdown(button_html, unsafe_allow_html=True)
