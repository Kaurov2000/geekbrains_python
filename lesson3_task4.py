# coding: utf-8

def my_func(x,y,variant = 1):
    if variant == 1:
        return x ** y
    else:
        a = 1
        for i in range(1,abs(y) + 1):
            a = a * x
        return 1 / a

try:
    x = float(input("Введите действительное положительное число x: "))
    y = int(input("Введите целое отрицательное число y: "))
    if y >= 0:
        raise ValueError

    print(my_func(x, y, 1))
    print(my_func(x, y, 2))

except ValueError:
    print("Одно из чисел введено неправильно")

