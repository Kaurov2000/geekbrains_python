# coding: utf-8

my_list = []
answer_yes = ['y','yes','да','д']
answer = 'y'
print("Программа меняет местами элементы в списке")
answer = input("Начать работу? ").lower()

while answer in answer_yes:
    elem = input("Введите элемент списка: ")
    my_list.append(elem)
    answer = input("Желаете ввести еще один элемент? ").lower()

if len(my_list) > 0:
    i = 0
    while i < len(my_list):
        try:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            i = i + 2
        except:
            i = i + 2

print(my_list)