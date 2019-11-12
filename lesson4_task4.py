# encoding = 'utf-8'

init_str = input("Введите список чисел через пробел: ")
init_list = init_str.split()
try:
    num_list = [float(el) for el in init_list] #перевожу в тип float, чтобы учесть, что 5 и 5.0 - одно и то же число
    result_list = [x for x in num_list if num_list.count(x) == 1]
    print(f"Элементы списка, не имеющие повторений: {result_list}")
except ValueError:
    print("Допущена ошибка при вводе числа")