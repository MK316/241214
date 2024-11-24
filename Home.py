import streamlit as st

st.set_page_config(page_title="Welcome to Symposium session I")

st.title("Main Page")
st.write("Welcome to the main page of the app!")

img_url = "https://github.com/MK316/241214/raw/main/image/bg-02.png"
st.image(img_url, caption="\"In preparation\"", use_column_width=True)
