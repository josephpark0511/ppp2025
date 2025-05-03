def average_num(nums):
    return sum(nums)/ len(nums)


def main():
    nums= []
    with open("numbers2.txt") as f:
        texts = f.readlines()
        for text in texts:
            nums.append(int(text.strip()))
        print(f"주어진 숫자의 평균값은 {average_num(nums)}입니다")




if __name__ == "__main__":
    main()