# 소득(income) 변수 선언
income = 5500  # 단위: 만원
tax = 0        # 초기값 설정

# 누진세 계산
if income <= 2000:
    tax = income * 0.05
    level = "저소득층"
elif income <= 5000:
    # 2,000만원까지는 5%, 초과분은 30%
    tax = (2000 * 0.05) + (income - 2000) * 0.30
    level = "중간소득층"
else:
    # 2,000만원까지 5% + 3,000만원까지 30% + 초과분 50%
    tax = (2000 * 0.05) + ((3000-2000) * 0.30) + (income - 5000) * 0.50
    level = "고소득층"

# 결과 출력
print("소득:", income, "만원")
print("소득 수준:", level)
print("예상 세금:", tax, "만원")
