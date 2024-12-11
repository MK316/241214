import streamlit as st
from PIL import Image
import os

# CSS for styling and alignment
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  # Adjust this to align with buttons
    }
    </style>
    """, unsafe_allow_html=True)

slides_path = "slide-1212"  # Adjust based on your directory structure
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

def display_image():
    if slide_files:
        image_path = os.path.join(slides_path, slide_files[st.session_state.slide_index])
        image = Image.open(image_path)
        st.image(image, caption=f"Slide {st.session_state.slide_index + 1} of {num_slides}")

tab1, tab2 = st.tabs(["🌱 Slides", "🌱 Videos"])

with tab1:
    display_image()  # Display the image at the top

    # Navigation buttons and dropdown for slide selection
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
    
    with col1:
        if st.button("⛳ Start"):
            st.session_state.slide_index = 0
            display_image()

    with col2:
        if st.button("◀️ Previous") and st.session_state.slide_index > 0:
            st.session_state.slide_index -= 1
            display_image()

    with col3:
        if st.button("▶️ Next") and st.session_state.slide_index < num_slides - 1:
            st.session_state.slide_index += 1
            display_image()

    with col4:
        selected_index = st.selectbox(
            "Choose a slide:",
            [f"Slide {i + 1}" for i in range(num_slides)],
            index=st.session_state.slide_index
        )
        new_index = int(selected_index.split()[-1]) - 1
        if new_index != st.session_state.slide_index:
            st.session_state.slide_index = new_index
            display_image()

with tab2:
    st.write("This is the content for the second tab.")

