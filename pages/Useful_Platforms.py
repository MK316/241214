import streamlit as st

# Function to create a green button
def green_button(label, url):
    button_html = f"""
    <a href="{url}" target="_blank">
        <button style="
            color: white;
            background-color: #4CAF50;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;">
            {label}
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)

# Add tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["📍Python", "📍Coding", "📍Github", "📍Gradio", "📍Huggingface", "📍Streamlit", "📍Other digital tools"])

# Tab 1: Python
with tab1:
    st.header("1: Python")
    st.write("Python is a versatile programming language known for its simplicity and readability. It's widely used for web development, data analysis, artificial intelligence, and more.")
    green_button("Learn More About Python", "https://www.python.org")


# Tab 2: Coding
with tab2:
    st.header("Tab 2: Coding Online")
    st.write("Google Colab is a cloud-based platform that allows you to write and execute Python code in your browser. It is especially useful for machine learning, data analysis, and collaborative coding projects.")
    green_button("Visit Google Colab", "https://colab.research.google.com")


# Tab 3: Github
with tab3:
    st.header("3: Github")
    st.write("GitHub is a platform for version control and collaboration. It helps developers manage and share code effectively.")
    green_button("Visit Github", "https://github.com")

# Tab 4: Gradio
with tab4:
    st.header("4: Gradio")
    st.write("Gradio makes it easy to create and share machine learning models with intuitive web-based interfaces.")
    green_button("Explore Gradio", "https://gradio.app")

# Tab 5: Huggingface
with tab5:
    st.header("5: Huggingface")
    st.write("Huggingface provides tools and libraries for natural language processing and machine learning, including pre-trained models.")
    green_button("Discover Huggingface", "https://huggingface.co")

# Tab 6: Streamlit
with tab6:
    st.header("6: Streamlit")
    st.write("Streamlit is a Python library that enables you to build interactive web applications for data science and machine learning.")
    green_button("Visit Streamlit", "https://streamlit.io")

# Tab 7: Others
with tab7:
    st.header("7: Digital Tools for Education")
    st.markdown("""
    Below is a selection of digital tools that can enhance teaching and learning experiences:

    - **[Google Classroom](https://classroom.google.com)**  
      A free service for schools, non-profits, and anyone with a personal Google account, Google Classroom makes it easy for learners and instructors to connect—inside and outside of schools.

    - **[Kahoot!](https://kahoot.com)**  
      Kahoot! is a game-based learning platform used as educational technology in schools and other educational institutions. Its learning games, "Kahoots", are user-generated multiple-choice quizzes that can be accessed via a web browser or the Kahoot app.

    - **[Zoom for Education](https://zoom.us/education)**  
      Zoom helps universities and schools improve student outcomes with secure video communication services for hybrid classrooms, office hours, administrative meetings, and more.

    - **[Canva for Education](https://www.canva.com/education/)**
      Empower your students to learn and express themselves in incredible ways using this intuitive design tool, which is freely available for K-12 teachers and their students.

    - **[Edmodo](https://new.edmodo.com)**  
      Edmodo is an educational technology company offering a communication, collaboration, and coaching platform to K-12 schools and teachers. The network enables teachers to share content, distribute quizzes, assignments, and manage communication with students, colleagues, and parents.

    Each tool offers unique features that can be utilized in different educational settings, helping to facilitate a more interactive and engaging learning environment.
    """, unsafe_allow_html=True)
