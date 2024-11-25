
import streamlit as st

# Function to create a yellow button
def yellow_button(label, url):
    button_html = f"""
    <a href="{url}" target="_blank">
        <button style="
            color: black;
            background-color: #FFDD57;
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
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍏 APP 1", "🍰 APP 2", "🍬 APP 3", "🍩 APP 4", "🍒 APP 5"])

# Tab 1
with tab1:
    st.header("Tab 1: About Python")
    st.write("Python is a powerful, versatile programming language used for a wide range of applications, from web development to data analysis.")
    yellow_button("Learn More", "https://www.python.org")

# Tab 2
with tab2:
    st.header("Tab 2: Streamlit")
    st.write("Streamlit is an open-source app framework for Machine Learning and Data Science projects.")
    yellow_button("Visit Streamlit", "https://streamlit.io")

# Tab 3
with tab3:
    st.header("Tab 3: Pandas")
    st.write("Pandas is a data manipulation and analysis library for Python, designed to handle structured data easily.")
    yellow_button("Explore Pandas", "https://pandas.pydata.org")

# Tab 4
with tab4:
    st.header("Tab 4: NumPy")
    st.write("NumPy is the fundamental package for numerical computing in Python.")
    yellow_button("Learn About NumPy", "https://numpy.org")

# Tab 5
with tab5:
    st.header("Tab 5: Machine Learning")
    st.write("Machine Learning is a subset of AI that enables systems to learn and improve from experience without explicit programming.")
    yellow_button("Discover ML", "https://scikit-learn.org")
