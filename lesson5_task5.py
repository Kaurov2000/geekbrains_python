# coding: utf-8
from functools import reduce

def sum_num(a, b):
    return a + b

with open('lesson5_task5.txt','w+') as f:
    while True:
        s=input("Введите набор чисел, разделенных пробелами. Пустая строка - выход из программы\n")
        if not s:
            break
        f.write(s + '\n')
    f.seek(0)
    sum = 0
    for str in f:
        my_list = map(int, str.split())
        sum = sum + reduce(sum_num, my_list)

print(f"Сумма чисел в файле {f.name} равна {sum}")