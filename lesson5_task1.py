# coding: utf-8

f = open('lesson5_task1.txt','w')
while True:
    print("Введите данные для записи в файл. Пустая строка - выход из программы")
    s=input()
    if not s:
        break
    f.write(s+'\n')
f.close()