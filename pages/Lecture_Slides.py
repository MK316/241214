import streamlit as st
from PIL import Image
import os

# Set up the path to the slides folder
slides_path = "slides"  # Ensure this is correct relative to your app's location
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

# Initialize session state variables if they do not exist
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0  # Start with the first slide

# Function to load and display the image based on the current index
def display_image():
    slide_path = os.path.join(slides_path, slide_files[st.session_state.slide_index])
    image = Image.open(slide_path)
    st.image(image, caption=f"Slide {st.session_state.slide_index + 1} of {num_slides}")

# Create tabs
tab1, tab2 = st.tabs(["Slides", "Other Content"])

with tab1:


    # Arrange 'Start', 'Previous', 'Next', and 'Slide Selector' in a single row
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
    
    with col1:
        start_clicked = st.button("⛳ Start", key="start", help="Reset to the first slide")
    with col2:
        previous_clicked = st.button("◀️ Previous", key="previous", help="Go back to the previous slide")
    with col3:
        next_clicked = st.button("▶️ Next", key="next", help="Go to the next slide")
    with col4:
        slide_number = st.selectbox("", options=[f"Slide {i + 1}" for i in range(num_slides)], key="slide_select")

    # Button actions
    if start_clicked:
        st.session_state.slide_index = 0

    if previous_clicked:
        if st.session_state.slide_index > 0:
            st.session_state.slide_index -= 1
        else:
            st.warning("This is the first slide.")

    if next_clicked:
        if st.session_state.slide_index < num_slides - 1:
            st.session_state.slide_index += 1
        else:
            st.warning("This is the end of the slides.")

    # Update the slide index if the user selects a slide directly
    selected_slide_index = int(slide_number.split()[-1]) - 1
    if selected_slide_index != st.session_state.slide_index:
        st.session_state.slide_index = selected_slide_index

    # Display the image
    display_image()

with tab2:
    st.write("This is the content for the second tab.")
