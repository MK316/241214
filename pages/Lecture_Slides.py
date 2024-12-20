import streamlit as st
from PIL import Image
import os

# CSS to adjust the alignment of the dropdown to match the buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  /* Adjust this value to align with the buttons */
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "lectureslides"  # Ensure this is correct relative to your app's location
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

# Initialize session state variables if they do not exist
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0  # Start with the first slide

# Function to load and display the image based on the current index with resizing
def display_image():
    slide_path = os.path.join(slides_path, slide_files[st.session_state.slide_index])
    image = Image.open(slide_path)
    
    # Set your desired width for resizing
    desired_width = 1200  # Adjust this value as needed
    aspect_ratio = image.height / image.width
    new_height = int(desired_width * aspect_ratio)
    resized_image = image.resize((desired_width, new_height))

    st.image(resized_image, caption=f"Slide {st.session_state.slide_index + 1} of {num_slides}")

# Create tabs
tab1, tab2 = st.tabs(["🌱 Slides", "🌱 Videos"])

with tab1:

    # Arrange 'Start', 'Previous', 'Next', and 'Slide Selector' in a single row
    col1, col2, col3, col4 = st.columns([1, 1, 1, 5])
    
    with col1:
        if st.button("⛳", key="start", help="Reset to the first slide"):
            st.session_state.slide_index = 0

    with col2:
        if st.button("◀️", key="previous", help="Go back to the previous slide"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1
            else:
                st.warning("This is the first slide.")

    with col3:
        if st.button("▶️", key="next", help="Go to the next slide"):
            if st.session_state.slide_index < num_slides - 1:
                st.session_state.slide_index += 1
            else:
                st.warning("This is the end of the slides.")

    with col4:
        # Display slide selector dropdown
        selected_slide = st.selectbox("",
                                      options=[f"Slide {i + 1}" for i in range(num_slides)],
                                      index=st.session_state.slide_index)

        # Update slide index if dropdown selection changes
        selected_slide_index = int(selected_slide.split()[-1]) - 1
        if selected_slide_index != st.session_state.slide_index:
            st.session_state.slide_index = selected_slide_index

    # Display the image
    display_image()

with tab2:
    st.write("SORA by OpenAI (Dec. 2024).")
    
    # URL of the YouTube video
    video_url = 'https://youtu.be/Gk4-bm7XImg?si=QmCL2K0omouypmg5'
    
    # Display the YouTube video in the Streamlit app
    st.video(video_url)

    # Second video
    st.caption("AI video example")
    
    video_url2 = "https://youtu.be/mvGOeLSXqdo?si=2yS6mc6cSuoU2r5T"
    st.video(video_url2)

    # Third video
    st.caption("Music generated with SUNO ai")
    video_url3 = "https://youtu.be/_cO8AeRjL88?si=Jv75Kv-ppBsj_v1l"
    st.video(video_url3)
