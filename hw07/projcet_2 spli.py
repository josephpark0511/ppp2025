#1번과제에서 만든 함수를 이용하며, 메인에서 split()함수를 이용하여 여러 값을 한줄로 입력
def average(nums):
    if len(nums) ==0:
        return 0
    return sum(nums) / len(nums)
user_input = input("숫자를 입력하시오==>>")
num_list = user_input.split()
nums_list = []
for s in num_list:
    nums_list.append(int(s))
print(f"평균은", average(nums_list),"입니다")





def main():
    pass
if __name__ == "__main__":
    main()