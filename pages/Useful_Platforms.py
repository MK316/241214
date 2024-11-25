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
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Coding", "Github", "Gradio", "Huggingface", "Streamlit"])

# Tab 1: Coding
with tab1:
    st.header("Tab 1: Coding")
    st.write("Coding is the foundation of building software and applications. It empowers you to create tools, solve problems, and innovate in the digital space.")
    green_button("Learn More About Coding", "https://www.w3schools.com")

# Tab 2: Github
with tab2:
    st.header("Tab 2: Github")
    st.write("GitHub is a platform for version control and collaboration. It helps developers manage and share code effectively.")
    green_button("Visit Github", "https://github.com")

# Tab 3: Gradio
with tab3:
    st.header("Tab 3: Gradio")
    st.write("Gradio makes it easy to create and share machine learning models with intuitive web-based interfaces.")
    green_button("Explore Gradio", "https://gradio.app")

# Tab 4: Huggingface
with tab4:
    st.header("Tab 4: Huggingface")
    st.write("Huggingface provides tools and libraries for natural language processing and machine learning, including pre-trained models.")
    green_button("Discover Huggingface", "https://huggingface.co")

# Tab 5: Streamlit
with tab5:
    st.header("Tab 5: Streamlit")
    st.write("Streamlit is a Python library that enables you to build interactive web applications for data science and machine learning.")
    green_button("Visit Streamlit", "https://streamlit.io")