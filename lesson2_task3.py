# coding: utf-8

seasons_list = ['Зима','Весна','Лето','Осень','Зима']
seasons_dict = {0:'Зима',1:'Весна',2:'Лето',3:'Осень',4:'Зима'}

m = input("Введите месяц в виде целого числа от 1 до 12: ")
try:
    m = int(m)
    if m > 0 and m <= 12:
        print(f"Это {seasons_list[m // 3]}")
        print(f"Это {seasons_dict[m // 3]}")

    else:
        print("wrong number")
except:
    print("wrong number")

