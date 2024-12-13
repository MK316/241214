import streamlit as st

# Title for the page
st.title("Sample Lesson Plans by Students")

# Introduction or description
st.write("Explore a collection of English class lesson plans created by students. Click on any of the links below to view the details in a new tab.")

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
