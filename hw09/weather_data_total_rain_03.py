def get_weather_data(filename, col_idx):
    weather_datas =[]
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            print(tokens[col_idx])
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_rain_events(rainfalls):
    events = []
    c_days =0
    for rain in rainfalls:
         if rain >0:
             c_days += 1
         else:
             if c_days > 0:
                 events.append(c_days)
                 c_days =0
    return events




def main():
    filename ="./weather(146)_2022-2022 (3).csv"
    rainfalls = get_weather_data(filename, 9)
    print(f"총 강수량은 = {sum(rainfalls):.1f}mm")



if __name__ == '__main__':
    main()