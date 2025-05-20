import streamlit as st
import matplotlib.pyplot as plt

# 시뮬레이션 데이터 (온도, 시간에 따라 산화막 두께 증가)
time = list(range(0, 31))
thickness = [0.11 * t for t in time]  # 단순 가정 모델

st.title("Semiconductor Process Simulator")
st.write("Oxidation process: Estimate oxide thickness by time.")

# 결과 요약
st.write(f"Estimated oxide thickness after 30 mins: {thickness[-1]:.2f} nm")

# 그래프 출력
fig, ax = plt.subplots()
ax.plot(time, thickness)
ax.set_xlabel("Time (min)")
ax.set_ylabel("Oxide Thickness (nm)")
ax.set_title("Oxide Thickness vs Time")

st.pyplot(fig)
