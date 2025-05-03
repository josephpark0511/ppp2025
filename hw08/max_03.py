def maximum(nums):
    return max(nums)

def main():
    nums = []
    text = " "
    with open("numbers2.txt") as f:
        texts = f.readlines()
        for text in texts:
            nums.append(int(text.strip()))
        print(f"주어진 숫자의 최댓값은 {maximum(nums)} 입니다")

if __name__ == "__main__":
    main()