# encoding = 'utf-8'

revenue = int(input("Введите выручку: "))
expence = int(input("Введите издержки: "))

if revenue > expence:
    print("Фирма работала с прибылью")
    profit = revenue-expence
    print(f"Рентбельность составляет {profit / revenue * 100:5.4} %")
    personnel = int(input("Введите численность сотрудников: "))
    print(f"Прибыль на одного сотрудника составляет {profit / personnel} ")
elif revenue < expence:
    print("Фирма работала в убыток")
else:
    print("Фирма сработала в ноль")