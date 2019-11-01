# coding: utf-8

print("Вводите строку из нескольких слов, разделённых пробелами:")
s = input()

l = s.split()

#for i in range(len(l)):
#    print(f"{i+1} - {l[i][:10]}")

for i,el in enumerate(l):
    print(f"{i + 1} - {el[:10]}")