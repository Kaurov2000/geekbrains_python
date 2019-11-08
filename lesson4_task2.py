# encoding = 'utf-8'

init_str = input("Введите список чисел через пробел: ")
init_list = init_str.split()
try:
    num_list = [float(el) for el in init_list]
    result_list = [num_list[i] for i in range(1,len(num_list)) if  num_list[i] > num_list[i-1]]
    print(f"Список элементов, которые больше предыдущего: {result_list}")
except ValueError:
    print("Допущена ошибка при вводе числа")
