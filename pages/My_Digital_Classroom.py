import streamlit as st
import requests

# Function to fetch and display GitHub Markdown content
def fetch_github_readme(url):
    # Convert GitHub page URL to raw content URL
    raw_url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to load content from GitHub."

def main():
    st.caption('My digital classroom: Github platform')

    # Set up tabs
    tabs = st.tabs(["DL&EE", "📗 Fall 2024", "📓 Spring 2024", "📓 Fall 2023", "📓 Spring 2023", "〽️ 2022"])

    # Fall 2024 content
    with tabs[0]:
    #    st.subheader("Digital Literacy & English Education")
        st.markdown("### 디지털 리터러시와 영어 교육")
        st.markdown("+ 대상: 2학년 예비 영어 교사")
        st.caption("이 강좌는 예비 영어 교사를 대상으로 디지털 리터러시와 AI 리터러시를 소개하여, 졸업 후 교사로서 미래 디지털 환경에 적응하고 선도할 수 있는 역량을 기르는 것을 목표로 함.")
        st.markdown("###강의개요:")
        st.markdown("1. **기초코딩**")
        st.caption("학생들은 Python의 기본 개념과 문법을 배우며, 이를 활용하여 간단한 디지털 도구와 언어 학습 관련 프로그램을 작성")
        st.markdown("2. **디지털 도구 탐색")
        st.caption("언어 교육에 활용할 수 있는 다양한 디지털 도구(예: SUNO ai, Elevenlabs, Speechnotes 등)를 탐구하고, 교실 수업과 온라인 학습 환경에 효과적으로 적용하는 방법 탐색")
        st.markdown("3. **디지털기반 교수설")
        st.caption("디지털 도구를 활용하여 영어 수업 계획을 작성하고, 학생들과 디지털 상호작용을 효율적으로 진행하는 방법을 학습")
        st.markdown("4. **디지털 상호작용 전략")
        st.caption("교사와 학생 간의 디지털 커뮤니케이션 방법과 윤리적인 활용법, 디지털 환경에서 학습 참여를 유도하는 방법을 탐구")
        st.markdown("5. **언어학습 앱디자인 및 개발 프로젝")
        st.caption("학기 말에는 디지털 도구를 활용하여 창의적인 언어 학습 활동 애플리케이션을 설계 및 개발하는 팀 프로젝트를 진행합니다. 이를 통해 학습한 내용을 실제 교육 현장에서 적용할 수 있는 실질적인 경험을 제공")
        st.markdown("###기대 효과:")
        st.caption("이 강좌를 통해 학생들은 디지털 시대에 요구되는 교사로서의 전문성을 기르고, 미래의 디지털 교육 환경에서 자신감을 가지고 수업을 진행할 수 있는 준비를 갖출 수 있을 것으로 기대됨.")

    with tabs[1]:
    #    st.subheader("Fall 2024 Courses")
        fall_url = 'https://github.com/MK316/MK-316/blob/main/pages/fall2024.md'
        fall_content = fetch_github_readme(fall_url)
        st.markdown(fall_content, unsafe_allow_html=True)
   
    
    # Spring 2024 content
    with tabs[2]:
    #    st.subheader("Spring 2024 Courses")
        spring_url = 'https://github.com/MK316/MK-316/blob/main/pages/spring2024.md'
        spring_content = fetch_github_readme(spring_url)
        st.markdown(spring_content, unsafe_allow_html=True)

    # Additional Content tab (optional)
    with tabs[3]:
    #    st.subheader("Fall 2023 Courses")
        # Placeholder URL for additional content if needed
        # Uncomment and update the URL if you have content for this tab
        fall2023_url = 'https://github.com/MK316/Fall2023/blob/main/README.md'
        additional_content = fetch_github_readme(fall2023_url)
        st.markdown(additional_content, unsafe_allow_html=True)


    with tabs[4]:
        # st.subheader("Spring 2023 Courses")
        # Placeholder URL for additional content if needed
        # Uncomment and update the URL if you have content for this tab
        additional_url = 'https://github.com/MK316/Spring2023/blob/main/README.md'
        additional_content = fetch_github_readme(additional_url)
        st.markdown(additional_content, unsafe_allow_html=True)

    # Additional Content tab (optional)
    with tabs[5]:
        st.subheader("Started to learn Python coding since Feb. 2022")
        # Placeholder URL for additional content if needed
        # Uncomment and update the URL if you have content for this tab

        st.markdown("+ [Github]('https://github.com/MK316')")
        img_url = "https://github.com/MK316/241214/raw/main/image/lady.png"
        st.image(img_url, width = 300, caption="It would've been wise to start coding back when I could actually see the screen without squinting... (to myself)")


if __name__ == "__main__":
    main()
