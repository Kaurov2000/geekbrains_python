# coding: utf-8

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
s1 = input("Введите первую строку: ")
s2 = input("Введите втрорую строку: ")

result = a + b
print(f"Сумма чисел равна: {result}")
result = a - b
print(f"Разность чисел равна: {result}")
result = a * b
print(f"Произведение чисел равно: {result}")
result = a / b
print(f"Частное чисел равно: {result:4f}")
result = a % b
print(f"Остаток от деления первого числа на второе равен: {result}")
result = a // b
print(f"Целочисленное частное чисел равно: {result}")

print("Сумма строк: ", s1 + s2)
