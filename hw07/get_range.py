# 1-n까지 리스트를 돌려주는 함수를 만드시오. 함수는 get_range_list(n)
def get_range_list(n):
    return list(range(1, n + 1))
n = int(input("숫자를 입력하시오==>>"))

print(get_range_list(5))

if __name__ == '__main__':
    (get_range_list(n))