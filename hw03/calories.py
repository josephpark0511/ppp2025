#칼로리 구하기 (과일마다 섭취 g를 입력받아서 칼로리 출력하기
hanrabong =int(input("한라봉 몇 그램 먹었는지 입력하시오"))
strawberries=int(input(" 딸기(설향) 몇 그램 먹었는지 입력하시오"))
banana=int(input("바나나 몇 그램 먹었는지 입력하시오"))
hanra= hanrabong*0.5
strawberry = strawberries*0.41
bananana=banana*0.77
print("한라봉을 섭취한 칼로리는 {}kcal/g , 딸기(설향)을 섭취한 칼로리는 {} kcal/g ,바나나를 섭취한 칼로리는 {} "
      " kcal/g 입니다".format(hanra, strawberry, bananana))


