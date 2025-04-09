import math

x1=int(input("x1의 좌표를 입력하시오"))
y1=int(input("y1의 좌표를 입력하시오"))
x2=int(input("x2의 좌표를 입력하시오"))
y2=int(input("y2의 좌표를 입력하시오"))
distance = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
print("x1, y1, x2, y2를 각각 입력 받아서 두 지점의 거리는 {}입니다".format(distance))