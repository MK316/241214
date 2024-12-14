import streamlit as st

# Title for the page
st.title("Sample Lesson Plans by Students")

# Introduction or description
st.write("Explore a collection of English class lesson plans created by students. Click on any of the links below to view the details in a new tab. (학생들이 만든 영어 수업 계획 예시입니다. 아래 링크 중 하나를 클릭하면 새 탭에서 세부 정보를 볼 수 있습니다.)")

# List of lesson plans with links to open in a new tab
lesson_plans = {
    "💠 Lesson Plan 1": "https://github.com/psy03",
    "💠 Lesson Plan 2": "https://github.com/MsMc24/G1-finalproject/blob/main/README.md",
    "💠 Lesson Plan 3": "https://github.com/ShieldEdu/G4-finalproject/blob/main/README.md",
    "💠 Lesson Plan 4": "https://github.com/verastudio/G2-finalproject/blob/main/README.md",
}

# Display the list of lesson plans as links
for plan_name, url in lesson_plans.items():
    link = f"[{plan_name}]({url})"
    st.markdown(link, unsafe_allow_html=True)
