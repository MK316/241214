import streamlit as st
import os

# Set path to slides folder
slides_folder = "/Slides"  # Adjust this path based on your setup
slides = sorted([f for f in os.listdir(slides_folder) if f.endswith('.png')])

# Initialize session state for the slide index
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# Function to update the slide index and re-render
def update_slide_index(new_index):
    if 0 <= new_index < len(slides):
        st.session_state.slide_index = new_index

# Display the current slide image
slide_path = os.path.join(slides_folder, slides[st.session_state.slide_index])
st.image(slide_path, use_column_width=True)

# Navigation buttons and index input
col1, col2, col3 = st.columns([1, 1, 2])

# Previous button
with col1:
    if st.button("Previous"):
        if st.session_state.slide_index > 0:
            update_slide_index(st.session_state.slide_index - 1)
        else:
            st.warning("This is the first page of the slides.")

# Next button
with col2:
    if st.button("Next"):
        if st.session_state.slide_index < len(slides) - 1:
            update_slide_index(st.session_state.slide_index + 1)
        else:
            st.warning("This is the end of the slide.")

# Go to specific slide
with col3:
    selected_index = st.number_input("Go to slide number:", min_value=1, max_value=len(slides), value=st.session_state.slide_index + 1, step=1)
    go_to_clicked = st.button("Go to")
    
    if go_to_clicked:
        update_slide_index(selected_index - 1)  # Adjust for zero-based index

# Display slide information
st.write(f"Slide {st.session_state.slide_index + 1} of {len(slides)}")
