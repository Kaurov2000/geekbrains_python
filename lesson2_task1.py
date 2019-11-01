# coding: utf-8

my_list = []
answer_yes = ['y','yes','да','д']
answer = 'y'
print("Программа выводит тип элементов в списке")
answer = input("Начать работу? ").lower()

while answer in answer_yes:
    elem = input("Введите элемент списка: ")

    while True:
        if elem.find(".") != -1:
            try:
                elem = float(elem)
                break
            except:
                pass

        try:
            elem = int(elem)
            break
        except:
            pass

        if elem == 'True':
            elem = True
            break
        if elem == 'False':
            elem = False
            break
        if elem.startswith("["):
            try:
                elem = list(elem)
                break
            except:
                pass
        if elem.startswith("("):
            try:
                elem = tuple(elem)
                break
            except:
                pass

        if elem.startswith("{"):
            elem = elem.replace("{","")
            elem = elem.replace("}", "")
            elem = elem.replace(" ",'')
            elem = elem.replace('"','')
            elem = elem.replace("'", '')
            if elem.find(":") != -1:
                elem_list = elem.split(",")
                my_dict = {}
                for el in elem_list:
                    dict_item = el.split(":")
                    my_dict[dict_item[0]] = dict_item [1]
                elem = my_dict
                break
            else:
                elem_list = elem.split(",")
                elem = set(elem_list)
                break

        break

    my_list.append(elem)
    answer = input("Желаете ввести еще один элемент? ").lower()

if len(my_list) > 0:
    for el in my_list:
        t = str(type(el))
        if t == "<class 'int'>":
            print(f"{el} - это целое число")
        elif t == "<class 'float'>":
            print(f"{el} - это вещественное число")
        elif t == "<class 'bool'>":
            print(f"{el} - это элемент типа 'bool'")
        elif t == "<class 'tuple'>":
            print(f"{el} - это элемент типа кортеж")
        elif t == "<class 'list'>":
            print(f"{el} - это элемент типа список")
        elif t == "<class 'dict'>":
            print(f"{el} - это элемент типа словарь")
        elif t == "<class 'set'>":
            print(f"{el} - это элемент типа множество")
        elif t == "<class 'str'>":
            print(f"{el} - это строка")
