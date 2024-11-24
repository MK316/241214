import streamlit as st

# JavaScript to automatically open a new tab
def auto_open_url(url):
    js = f"<script>window.open('{url}');</script>"
    st.components.v1.html(js, height=0, width=0)

# URL you want to open
github_url = "https://github.com/yourusername/yourrepository"

# Function call to open the URL automatically
auto_open_url(github_url)

st.title('Page Title')
st.write("This page will automatically open a GitHub page when loaded.")
