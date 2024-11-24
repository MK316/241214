import streamlit as st

# Define the GitHub URLs
urls = {
    "Project 1": "https://github.com/MK316/F2024/blob/main/README.md",
    "Project 2": "https://github.com/yourusername/project2",
    "Project 3": "https://github.com/yourusername/project3"
}

# Create radio buttons to select the project
project = st.radio("Choose a GitHub project:", list(urls.keys()))

# Button to open the selected project's GitHub page
if st.button('Open GitHub Project'):
    # JavaScript to open a new tab with the selected project's URL
    js = f"window.open('{urls[project]}')"  # JavaScript to open a new tab
    st.components.v1.html(f"<script>{js}</script>", height=0, width=0)

st.write(f"You selected: {project}")
