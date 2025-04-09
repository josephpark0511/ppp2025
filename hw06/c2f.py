def f2c(t_f):
    return(t_f-32)*5/9
temp_c =int(input("섭씨온도를 입력하세요==>>"))
temp_f = f2c(temp_c)
print(f"{temp_c}C =>{temp_f:.2f}F 입니다")





