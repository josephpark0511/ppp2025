x1=int(input("x1의 좌표를 입력하시오 ==>"))
y1=int(input("y1의 좌표를 입력하시오==>"))
if x1 and y1 >0:
    print("입력한 좌표는 1사분면 입니다")
elif x1 <0 and y1>0:
    print("입력한 좌표는 2사분면 입니다")
elif x1<0 and y1<0:
    print("입력한 좌표는  3사분면 입니다")
elif x1==0 and (y1>0 or y1<0):
    print("입력한 좌표는 y축 위에 있습니다.")
elif x1 == 0 and (x1 > 0 or x1 < 0):
    print("입력한 좌표는 x축 위에 있습니다.")
elif x1 == 0 and y1==0:
    print(" 입력한 좌표는 원점 입니다.")
else:
    print("입력한 좌표는 4사분면 입니다")



