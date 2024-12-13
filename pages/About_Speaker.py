import streamlit as st

st.title("Presenter: ")
img_url = "https://github.com/MK316/241214/raw/main/image/speaker.png"
# Updated to use the new parameter
st.image(img_url, use_container_width=True)
st.caption("https://englishedu.gnu.ac.kr")

st.markdown("+ Interested in digital literacy training for prospective English teachers")
st.caption("Digital Literacy & English Education (Spring 2023, Spring 2024)")
img_url2 = "https://github.com/MK316/241214/raw/main/image/KeywordCloud_231129.png"
# Updated to use the new parameter
st.image(img_url2, use_container_width=True)
st.markdown("+ **My Digital Literacy Education keywords:**")
st.markdown("1. **Independent Digital Competency**")
st.markdown("2. **Self-sufficient Teaching Tools**")
st.markdown("3. **Content-empowered Digital Literacy**")
