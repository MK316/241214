import streamlit as st

# Function to create a green button
def green_button(label, url):
    button_html = f"""
    <a href="{url}" target="_blank">
        <button style="
            color: white;
            background-color: #3399FF;
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
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📍Pronunciation-Checker", "📍App2", "📍App3", "📍App4", "📍App5", "📍App6"])

# Tab 1: Python
with tab1:
    st.header("1: PronunciationChecker")
    st.write("")
    green_button("Clic to open the APP", "https://mk-316-pronunciationfeedback.hf.space/")



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

