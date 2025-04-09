def gugudan(dan):
    print(f"{dan}단:")
    for i in range(9):
        print(f"{dan}*{i+1} = {dan * (1+i)}")
dan= int(input("숫자를 입력하세요==>>>"))
gugudan(dan)




