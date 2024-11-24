import streamlit as st

st.set_page_config(page_title="Welcome to Symposium session I")

st.title("MK316")
st.write("Welcome to the main page of the app!")
st.caption("Symposium schedule: 1:30PM~3PM, 2024. 12. 14")

img_url = "https://github.com/MK316/241214/raw/main/image/bg-02.png"
st.image(img_url, caption="\"In preparation\"", use_column_width=True)
