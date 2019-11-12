# coding: utf-8
from functools import reduce

def sum_salary(a, b):
    return a + b

f = open('lesson5_task3.txt','r',encoding='utf-8')
my_dict={}
for str in f:
    key, value = str.split()
    my_dict[key] = int(value)
f.close()

ret_list = [key for key in my_dict.keys() if my_dict[key] < 20000]
avg = reduce(sum_salary, my_dict.values()) / len(my_dict.values())
print(f"Сотрудники с окладом меньше 20000:\n {ret_list}")
print(f"Средняя зарплата составляет {avg}")
