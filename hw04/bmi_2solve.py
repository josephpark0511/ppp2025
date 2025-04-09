#03의 BMI 계산결과에 따라 아래 텍스트를 참고하여, 비만 정도를 표시하시오.
height = float(input("키가 얼마인가요?=>"))
weight = float(input("몸무게는 얼마인가요?=>"))
height_m =height /100
BMI = weight/(height_m*height_m)
if (BMI>=23) and (BMI<25):
    print("당신은 전 단계 비만 입니다")
elif (BMI>=25) and (BMI <30):
    print("당신은 1단계 비만 입니다")
elif (BMI>=30) and (BMI<35):
    print("당신은 2단계 비만 입니다.")
elif (BMI>=35):
    print("당신은 3단계 비만 입니다")
else:
    print("당신은 정상입니다.")




