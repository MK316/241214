import streamlit as st
import os

# Set path to slides folder
slides_folder = "./slides"  # Adjust this path as needed based on your setup
slides = sorted([f for f in os.listdir(slides_folder) if f.endswith('.png')])

# Initialize session state for the slide index
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# Tab structure
tab1, tab2 = st.tabs(["Slideshow", "Other Tab"])

# First tab for slideshow
with tab1:
    st.title("Slideshow")

    # Display the current slide image
    slide_path = os.path.join(slides_folder, slides[st.session_state.slide_index])
    st.image(slide_path, use_column_width=True)

    # Navigation buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous"):
            # Move to the previous slide
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(slides)
    with col2:
        if st.button("Next"):
            # Move to the next slide
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(slides)

# Second tab for other content
with tab2:
    st.write("This is the content for the second tab.")
