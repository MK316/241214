import streamlit as st

st.title("Presenter: ")
img_url = "https://github.com/MK316/241214/raw/main/image/speaker.png"
# Updated to use the new parameter
st.image(img_url, use_container_width=True)
# st.markdown("[경상국립대학교 영어교육과 홈페이지](https://englishedu.gnu.ac.kr)")
# st.markdown("[나의 수업 APP gallery](https://mk316home.streamlit.app)")
# Set up HTML for small buttons side by side
buttons_html = """
<div style="display: flex; flex-direction: row; gap: 10px;">
    <a href="https://englishedu.gnu.ac.kr" target="_blank">
        <button style="background-color: #4CAF50; color: white; border: none; padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px;">경상국립대학교 영어교육과 홈페이지</button>
    </a>
    <a href="https://mk316home.streamlit.app" target="_blank">
        <button style="background-color: #008CBA; color: white; border: none; padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px;">나의 수업 APP gallery</button>
    </a>
</div>
"""

# Render the HTML with the buttons in Streamlit
st.markdown(buttons_html, unsafe_allow_html=True)

img_url2 = "https://github.com/MK316/241214/raw/main/image/KeywordCloud_231129.png"
# Updated to use the new parameter
st.image(img_url2, use_container_width=True)
st.markdown("### 🌱 My Digital Literacy Education keywords:")
st.markdown("1. **Independent Digital Competency**")
st.markdown("2. **Content-empowered Digital Literacy**")
st.markdown("3. **Self-sufficient Teaching Tools**")
