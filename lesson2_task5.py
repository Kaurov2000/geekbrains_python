# coding: utf-8

my_list = [7, 5, 3, 3, 2]

n = int(input("Введите рейтинг - натуральное число: "))

i = 0
m = my_list[i]
while n <= my_list[i]:
    i = i + 1
    if i == len(my_list):
        break
    m = my_list[i]
my_list.insert(i,n)
print(f"Добавлено на позицию {i}:")
print(my_list)