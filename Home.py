import streamlit as st

st.set_page_config(page_title="Welcome to Symposium session I")

st.title("Main Page")
st.write("Welcome to the main page of the app!")

img_url = "https://github.com/MK316/241214/blob/bcc1ad402c8cc9e3ce8b679bd55d88f29e985bc9/image/bg-02.png"
st.image(img_url, caption="\"In preparation\"", use_column_width=True)
