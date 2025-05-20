import streamlit as st
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
# plt.rcParams['font.family'] = 'NanumGothic'  # 리눅스용 설치 시
plt.rcParams['axes.unicode_minus'] = False  # 음수 부호 깨짐 방지

st.title("반도체 공정 시뮬레이터")

st.sidebar.header("공정 조건 선택")
process = st.sidebar.selectbox("공정 선택", ["산화", "식각", "증착"])
temp = st.sidebar.slider("온도(℃)", 200, 1000, 600)
time = st.sidebar.slider("공정 시간(분)", 1, 120, 30)

st.write(f"선택한 공정: **{process}**, 온도: {temp}℃, 시간: {time}분")

# 예: 산화 두께 간단 시뮬레이션
if process == "산화":
    thickness = 0.1 * (temp / 100) * (time ** 0.5)
    st.write(f"예상 산화막 두께: {round(thickness, 2)} nm")

    fig, ax = plt.subplots()
    ax.plot([0, time], [0, thickness])
    ax.set_xlabel("시간(분)")
    ax.set_ylabel("산화막 두께(nm)")
    ax.set_title("산화막 성장 시뮬레이션")
    st.pyplot(fig)

st.markdown("---")
with st.expander("🔍 공정 이론 보기"):
    st.markdown("""
    - **산화 공정**은 실리콘 웨이퍼에 SiO₂ 막을 형성하는 과정입니다.
    - 일반적으로 고온에서 O₂ 또는 H₂O를 공급해 이뤄지며, Dry vs Wet 방식이 존재합니다.
    """)
