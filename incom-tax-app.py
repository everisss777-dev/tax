# app.py
import streamlit as st

st.set_page_config(page_title="소득별 세금 계산기", page_icon="💰")

st.title("💰 소득별 세금 계산기")
st.write("단위: **만원** 기준입니다.")

# 입력
income = st.number_input("소득을 입력하세요 (만원)", min_value=0, value=5500, step=100)
tax = 0

# 세율 계산
if income < 2000:
    level = "저소득층"
    tax = income * 0.05
elif income < 5000:
    level = "중간소득층"
    tax = income * 0.30
else:
    level = "고소득층"
    tax = income * 0.50

# 출력
st.subheader("🧾 계산 결과")
st.write(f"**소득 수준:** {level}")
st.write(f"**예상 세금:** {tax:,.1f} 만원")
