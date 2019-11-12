# coding: utf-8

my_dict =  {'One':'Один', 'Two':'Два', 'Three':'Три','Four':'Четыре'}

f1 = open('lesson5_task4.txt','r',encoding='utf-8')
f2 = open('lesson5_task4.out','w',encoding='utf-8')

for str in f1:
    key, splitter, value = str.split()
    key = my_dict[key]
    f2.write(f"{key} {splitter} {value}\n")

f1.close()
f2.close()