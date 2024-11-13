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

# Button actions
if st.button("Start"):
    st.session_state.slide_index = 0

if st.button("Next"):
    if st.session_state.slide_index < num_slides - 1:
        st.session_state.slide_index += 1
    else:
        st.warning("This is the end of the slide.")

if st.button("Previous"):
    if st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1
    else:
        st.warning("This is the first page of the slides.")

# Input for direct slide navigation
slide_number = st.number_input("Go to slide number:", min_value=1, max_value=num_slides, value=st.session_state.slide_index + 1, step=1)

if st.button("Go to"):
    st.session_state.slide_index = slide_number - 1

# Display the image
display_image()
