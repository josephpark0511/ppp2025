def get_weather_data(filename,col_idx):
    weather_datas = []
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_rain_events(rainfalls):
    count =0
    count_list =[]
    for rain in rainfalls:
        if rain > 0:
            count +=1
        else:
            if count >0 :
                count_list.append(count)
    if count >0:
        count_list.append(count)

    return count_list

def sumifs(rainfalls, months, selected = [6,7,8]):
    total = 0
    for i in range(len(rainfalls)):
        month = months[i]
        rain = rainfalls[i]
        if month in selected:
            total += rain

    return total


def get_weather_data1_int(filename,col_idx):
    weather_datas = []
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(int(float(tokens[col_idx])))
    return weather_datas

def rainfalls_sum(rainfalls):
    count = 0
    count_list = []
    for rain in rainfalls:
        if rain > 0:
            count += rain
        else:
            if count > 0:
                count_list.append(count)
                count = 0
    if count > 0:
        count_list.append(count)
    return max(count_list)



def main():
    filename = "weather(146)_2022-2022 (3).csv"
    rainfalls = get_weather_data(filename,9)
    print(f" 4번: 최장 연속 강우일수는 {max(get_rain_events(rainfalls))}일 입니다.")
    rain_event = get_weather_data(filename,9)
    rain_event = rainfalls_sum(rainfalls)
    print(f" 5번 : 강우 이벤트 중 최대 강수량은 {(rain_event):.1f}mm 입니다.")

    top3_tmax =sorted(get_weather_data(filename,3))[-3:]
    print(f" 6번:  가장 더운 날 top3는  {(top3_tmax)}C 입니다.")
    months = get_weather_data(filename,1)
    print(f"1번: 여름철 총 강수량은{sumifs(rainfalls, months, selected =[6,7,8]):.1f}mm 입니다")

    filename_20y ="weather(146)_2001-2022 (2).csv"
    rainfalls_1 = get_weather_data1_int(filename_20y,9)
    years = get_weather_data1_int(filename_20y,0)
    print(f"2021년 총 강수량은 {sumifs(rainfalls_1, years, selected =[2021]):.1f}mm 입니다")
    print(f"2022년 총 강수량은 {sumifs(rainfalls_1, years, selected = [2022]):.1f}mm 입니다")





if __name__ == '__main__':
    main()