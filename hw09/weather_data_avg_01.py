def average(nums):
    return sum(nums) / len(nums)

def get_weather_data(filename, col_idx):
    weather_datas =[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            print(tokens[col_idx])
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas





def main():
    filename = "./weather(146)_2022-2022 (3).csv"
    tavgs = get_weather_data(filename, 4)
    print(f" 연평균 기온(avg . of  연평균 ) = {average(tavgs)}도")






if __name__ =='__main__':
    main()