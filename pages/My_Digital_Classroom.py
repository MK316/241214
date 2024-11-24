import streamlit as st

# Define the GitHub URLs
urls = {
    "Project 1": "https://github.com/MK316/F2024/blob/main/README.md",
    "Project 2": "https://github.com/yourusername/project2",
    "Project 3": "https://github.com/yourusername/project3"
}

# Create tabs for each project
tab1, tab2, tab3 = st.tabs(["Project 1", "Project 2", "Project 3"])

with tab1:
    st.markdown(f"### Project 1")
    st.markdown(f"[Visit Project 1 on GitHub]({urls['Project 1']})")

with tab2:
    st.markdown(f"### Project 2")
    st.markdown(f"[Visit Project 2 on GitHub]({urls['Project 2']})")

with tab3:
    st.markdown(f"### Project 3")
    st.markdown(f"[Visit Project 3 on GitHub]({urls['Project 3']})")
