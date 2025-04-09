def is_leap_year():
    y = int(input("연도를 입력하세요==>>>"))
    return y % 4 == 0 and y % 100 != 0
if is_leap_year():
    print(" True, 윤년 입니다")
else:
    print("False, 윤년 아닙니다")







def main():
    pass
if __name__ == '__main__':
    main()