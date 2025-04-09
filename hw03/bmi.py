height = int(input("키가 얼마인가요?=>"))
weight = int(input("몸무게는 얼마인가요?=>"))
BMI = weight/(height*height)
height_m =height /100
print("키는 {}, 몸무게는 {}, BMI = {}".format(weight, height, BMI))
print("BMI({})/ ({}*{})이다".format(  BMI,weight,height))