def get_weather_data(filename, col_idx):
    weather_datas =[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            print(tokens[col_idx])
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def count_bigger_days(nums, criteria):
    cnt = 0
    for num in nums:
        if num>= criteria:
            cnt += 1
    return cnt




def main():
    filename ="./weather(146)_2022-2022 (3).csv"
    rainfalls = get_weather_data(filename,9)
    count_over5_rain = count_bigger_days(rainfalls, 5)
    print(f" 5mm 이상 강우일수는 = {count_over5_rain}일 입니다")


if __name__== "__main__":
    main()
