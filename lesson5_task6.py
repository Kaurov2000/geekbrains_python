# coding: utf-8

def my_func(str):
    if str.startswith('-'):
        str = '0'
    else:
        str = str.split('(')[0]
    return int(str)

f = open('lesson5_task6.txt','r',encoding='utf-8')
hours_dict = {}
for str in f:
    subj, lect, pract, lab  = str.split()
    hours_dict[subj] = my_func(lect) + my_func(pract) + my_func(lab)

print(hours_dict)
f.close()