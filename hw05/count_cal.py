fruit_cal = {"한라봉": 0.5, "딸기": 0.34, "바나나": 0.77}

total = 0
for fruit in fruit_cal:
    eat = int(input(f"{fruit} 몇 g 먹었나요? "))
    cal = (fruit_cal[fruit] * eat)
    total += cal
    print(f"{fruit}: {cal:.2f} kcal")

print(f"총 칼로리는 {total:.2f} kcal입니다.")
