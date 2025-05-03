def total_num(nums):
    return len(nums)

def main():
    with open("numbers2.txt") as f:
        lines =f.readlines()
        print(f"주어진 숫자의 총 갯수는 {(total_num(lines))}개 입니다" )
    return total_num(lines)





if __name__ =='__main__':
    main()