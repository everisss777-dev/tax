# 소득(income)과 세금(tax) 변수 선언
income = 5500  # 단위: 만원
tax = 0  # 초기값 설정

# 소득 수준에 따라 세금 계산 및 분류
if income < 2000:
    level = "저소득층"
    tax = income * 0.1   # 세율 5%
elif income < 5000:
    level = "중간소득층"
    tax = income * 0.30   # 세율 30%
else:
    level = "고소득층"
    tax = income * 0.50   # 세율 50%

# 결과 출력
print("소득:", income, "만원")
print("소득 수준:", level)
print("예상 세금:", tax, "만원")
