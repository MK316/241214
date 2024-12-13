import streamlit as st

st.set_page_config(page_title="Welcome to Symposium session I")

st.markdown("## 2024 제1회 경상 디지털 교육 나눔 한마당")
st.caption("주최: 경상국립대학교 사범대학")
st.write("💦 Symposium schedule: 1:00PM~2:30PM, 2024. 12. 14")
st.caption("발표 관련 자료들이 업로드될 예정입니다.")

img_url = "https://github.com/MK316/241214/raw/main/image/bg-02.png"
# Updated parameter to use_container_width=True
st.image(img_url, caption="\"In preparation (Last updated: Nov.24)\"", use_container_width=True)

img_QR = "https://github.com/MK316/241214/raw/main/image/241214QR.jpg"
st.image(img_QR, caption="이 페이지에 접속하려면 QR :-)", width=100)
