import streamlit as st

# 페이지 설정
st.set_page_config(page_title="내 소개", layout="wide")

# 제목
st.title("👋 자기소개")
st.write("안녕하세요. 제 자기소개를 해보겠습니다.")
st.markdown("---")

# 프로필 섹션
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("프로필")
    # 나중에 이미지 추가 가능
    st.write("이름: 전효린")
    st.write("생년월일: 2007-07-14")
    st.write("사는 곳: 구미")
    st.write("직업: 대학생")

st.markdown("---")

# 취미 섹션
st.subheader("🎯 취미")
col1 = st.columns(1)[0]
with col1:
    st.write("**취미**")
    st.write("- 영화 보기")
    st.write("- 노래 듣기")
    st.write("- 탁구하기")

st.markdown("---")

# 연락처 섹션
st.subheader("📧 연락처")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**이메일**")
    st.write("wjsgyfls1691@gmail.com")
with col2:
    st.write("**전화**")
    st.write("010-1234-5678")
with col3:
    st.write("**포트폴리오**")
    st.write("[링크](https://example.com)")
