# coding: utf-8


goods_list = []

answer_yes = ['y','yes','да','д']
answer = 'y'
answer = input("Начать работу? ").lower()
i = 0
while answer in answer_yes:
    goods_dict = {"название": None, "цена": None, "количество": None, "ед.": None}
    name =  input("Введите название товара: ")
    goods_dict["название"] = name
    price = int(input("Введите цену товара: "))
    goods_dict["цена"] = price
    quantity = int(input("Введите количество товара: "))
    goods_dict["количество"] = quantity
    unit = input("Введите единицу измерения товара: ")
    goods_dict["ед."] = unit
    i = i + 1
    goods_list.append((i,goods_dict))
    answer = input("Хотите ввести еще один товар? ").lower()

answer = input("Сформировать аналитику? ").lower()
if answer in answer_yes:
    goods_dict = {"название": [], "цена": [], "количество": [], "ед.": []}
    for k in range(len(goods_list)):
        t = goods_list[k]
        d = t[1]
        name = d["название"]
        goods_dict["название"].append(name)
        price = d["цена"]
        goods_dict["цена"].append(price)
        quantity = d["количество"]
        goods_dict["количество"].append(quantity)
        unit = d["ед."]
        goods_dict["ед."].append(unit)
    goods_dict["название"] = list(set(goods_dict["название"]))
    goods_dict["цена"] = list(set(goods_dict["цена"]))
    goods_dict["количество"] = list(set(goods_dict["количество"]))
    goods_dict["ед."] = list(set(goods_dict["ед."]))
    print(goods_dict)
else:
    print("Пока!")
