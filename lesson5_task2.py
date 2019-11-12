
f = open('lesson5_task2.txt','r')
str_dict = {}
i = 1
for str in f:
    str_dict[i] = len(str.split())
    i = i + 1
print(f"В файле {i} строк:")
for j in str_dict.keys():
    print(f"Строка {j} содержит {str_dict[j]} слов")
f.close()