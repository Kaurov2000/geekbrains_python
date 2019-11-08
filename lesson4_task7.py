# encoding = 'utf-8'

def fibo_gen(x):
    for i in range(x,1,-1):
        yield i

try:
    x = int(input("Введите целое неотрицательное число: "))
    if x <= 0:
        raise ValueError

    factorial = 1
    i = 1
    for el in fibo_gen(x):
        factorial = factorial * el
        i = i + 1
        if i > 15:
            break

    if i < 16:
        print(f"Факториал числа равен {factorial}")
    else:
        print(f"Произведение первых 15 чисел при вычислении факториала равно {factorial}")

except ValueError:
    print("Допущена ошибка при вводе числа")