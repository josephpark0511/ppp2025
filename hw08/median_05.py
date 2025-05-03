def median(nums):
    sorted_nums = sorted(nums)
    if len(nums)%2 ==0:
        return (sorted_nums[len(nums)//2-1]+sorted_nums[len(nums)//2]) /2
    elif len(nums) ==0:
        return 0
    else:
        return sorted_nums[len(nums) // 2]

def main():
    nums = []
    text = " "
    with open("numbers2.txt") as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.strip()))
            text += " "+line.strip()
    print(f"중앙값은 {median(nums)} 입니다")



if __name__ == "__main__":
    main()