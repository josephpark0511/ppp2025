def minimum(nums):
    return min(nums)


def main():
    nums = []
    with open("numbers2.txt") as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.strip()))
        print(f"주어진 수의 최솟값은 {minimum(nums)} 입니다")

if __name__ == '__main__':
    main()