import streamlit as st
import os

# Set path to slides folder
slides_folder = "./slides"  # Adjust this path as needed based on your setup
slides = sorted([f for f in os.listdir(slides_folder) if f.endswith('.jpg')])

# Initialize session state for the slide index
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# Tab structure
tab1, tab2 = st.tabs(["Slideshow", "Other Tab"])

# First tab for slideshow
with tab1:
    # Display the current slide image
    slide_path = os.path.join(slides_folder, slides[st.session_state.slide_index])
    st.image(slide_path, use_column_width=True)

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    
    # Previous button
    with col1:
        if st.button("Previous"):
            # Move to the previous slide
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(slides)
    
    # Next button
    with col2:
        if st.button("Next"):
            # Move to the next slide
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(slides)
    
    # Go to specific slide
    with col3:
        # Get the slide number from the user
        selected_index = st.number_input("Go to slide number:", min_value=1, max_value=len(slides), value=1, step=1)
        if st.button("Go to"):
            # Update the slide index based on user input
            st.session_state.slide_index = selected_index - 1  # Adjust for zero-based index

# Second tab for other content
with tab2:
    st.write("This is the content for the second tab.")
