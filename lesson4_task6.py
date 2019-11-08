# encoding = 'utf-8'

from itertools import count,cycle

def infinite_iterator(start):
    global end
    if not end:
        end = start * 10
    for i in count(start):
        print(i)
        if i == end:
            break

def infinite_cycle(my_list):
    global end
    if not end:
        end = 10
    j = 0
    for i in cycle(my_list):
        print(i)
        j = j + 1
        if j == len(my_list) * end:
            break

print("Я могу:")
print("1 - генерировать целые числа, начиная с указанного")
print("2 - повторять элементы списка")
answer = input("Чего вы хотите? ")
if answer == '1':
    try:
        start = int(input("Введите стартовое значение: "))
    except ValueError:
        print("Допущена ошибка при вводе числа")
    try:
        end = int(input("Введите конечное значение или пропустите этот шаг: "))
    except ValueError:
        end = ''
    infinite_iterator(start)

elif answer == '2':
    a = (input("Введите список, используя пробел для разделения элементов: ")).split()
    try:
        end = int(input("Введите количество повторов или пропустите этот шаг: "))
    except ValueError:
        end = ''
    infinite_cycle(a)

else:
    print("Неизвестный ответ")


