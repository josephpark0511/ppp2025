#숫자 n이 주어졌을 때, 1부터 n까지의 합을 구하시오. 함수명은 sum_n(n)
def sum_n(n):
    return (n * (n + 1)/2)
n =int(input("숫자를 입력하시오==>"))
print(sum_n(n))

#if __name__ == "__main__":
    #sum_n(n)