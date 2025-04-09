#int 또는 math을 활용하여 사다리꼴의 넓이를 구하여라.
upper = int(input("윗변을 입력하시오=>"))
lower =int(input("밑변을 입력하시오=>"))
height = int(input("높이를 입력하시오=>"))
area1 = (upper+lower)*(height)/2
print("윗변 = {}, 아랫변= {}, 높이={}일 때". format( upper, lower, height))
print("사다리꼴의 면적은 = {}입니다". format(area1))