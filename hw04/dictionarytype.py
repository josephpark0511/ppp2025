#칼로리 구하기 (과일마다 섭취 g를 입력받아서 칼로리 출력하기
hanrabong =float(input("한라봉 몇 그램 먹었는지 입력하시오==>"))
strawberries=float(input(" 딸기(설향) 몇 그램 먹었는지 입력하시오==>"))
banana=float(input("바나나 몇 그램 먹었는지 입력하시오==>"))
calories =  {'한라봉': 50, '딸기': 34, '바나나': 77}
eat_hanrabong = (calories['한라봉'] * hanrabong/100)
eat_strawberries = (calories['딸기'] * strawberries/100 )
eat_banana = (calories['바나나']  * banana/100)
total_calories =(eat_hanrabong + eat_strawberries + eat_banana)
print("한라봉을 섭취한 칼로리는 {}kcal/g , 딸기(설향)을 섭취한 칼로리는 {} kcal/g ,바나나를 섭취한 칼로리는 {} "
      " kcal/g 입니다".format( eat_hanrabong, eat_strawberries, eat_banana))
print("과일을 섭취한 총 칼로리는 {}kcal/g 입니다.".format(total_calories))






