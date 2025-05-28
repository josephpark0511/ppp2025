def read_db(filename):
    calorie_dic = {}
    with open(filename, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
        # print(lines)
        for line in lines[1:]:
            tokens = line.split(",")
            line = line.strip()
            calorie_dic[tokens[0]] = int(tokens[1]) / int(tokens[2])

    return calorie_dic


def main():
    fruit_cal = read_db("./calorie_db (3).csv")
    fruit_eat = {
        "쑥": 200,
        "바나나": 200,
    }

    total = 0
    for item in fruit_eat:
        total += (fruit_cal[item] * fruit_eat[item])
    print(f" 총 칼로리는 {total}cal입니다")


if __name__ == '__main__':
    main()