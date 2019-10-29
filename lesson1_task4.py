# coding: utf-8

n = int(input("Введите целое положительное число: "))

max = 0
while n > 0:
    m = n % 10
    if m > max:
        max = m
    n = n // 10

print(f"Максимальная цмфра в числе - это {max}")
