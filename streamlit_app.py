import streamlit as st

# 페이지 설정
st.set_page_config(page_title="내 소개", layout="wide")

# 제목
st.title("👋 자기소개")
st.write("안녕하세요. 저는 전효린입니다. 자기소개를 입력해주세요.")
st.markdown("---")

# 프로필 섹션
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("프로필")
    # 나중에 이미지 추가 가능
    st.write("이름: 여기에 이름 추가")
    st.write("생년월일: YYYY-MM-DD")
    st.write("직업: 여기에 직업 추가 (학생, 교사, 회사원 등)")

with col2:
    st.subheader("소개")
    st.write("여기에 자기소개 내용을 작성해주세요.")

st.markdown("---")

# 경험 섹션
st.subheader("📚 경험 및 스킬")
col1, col2 = st.columns(2)
with col1:
    st.write("**주요 경험**")
    st.write("- 항목 1")
    st.write("- 항목 2")
    st.write("- 항목 3")

with col2:
    st.write("**스킬**")
    st.write("- 스킬 1")
    st.write("- 스킬 2")
    st.write("- 스킬 3")

st.markdown("---")

# 연락처 섹션
st.subheader("📧 연락처")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**이메일**")
    st.write("your.email@example.com")
with col2:
    st.write("**전화**")
    st.write("010-0000-0000")
with col3:
    st.write("**포트폴리오**")
    st.write("[링크](https://example.com)")
