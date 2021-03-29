length=float(input("키를 입력하세요.(소숫점 첫번째 자리까지):"))
weight=float(input("몸무게를 입력하세요.(소숫점 첫번째 자리까지):"))
SW=float((length-100)*0.9)
BMI=float(weight-SW)*100/SW
if(BMI<=10):
    print("비만도 계산 결과 (%.1f) 이므로 정상"%BMI)
elif(BMI>10 and BMI<=20):
    print("비만도 계산 결과 (%.1f) 이므로 과체중"%BMI)
elif(BMI>20):
    print("비만도 계산 결과 (%.1f) 이므로 비만"%BMI)
