#1. 숫자 리스트를 매개변수로 받아서 평균을 구하는 함수를 완성하시오. 함수는 average(nums)
def average(nums):
    if len(nums) ==0:
        return 0
    return sum(nums) / len(nums)

print(average([1,2,3,4,5,]))







def main():
    pass
if __name__ == '__main__':
    main()