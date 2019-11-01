# encoding = 'utf-8'

def person_data(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}", end = '; ')

data={}
while True:
    key = input("Введите название поля данных: ")
    if not key:
        break
    value = input("Введите значение: ")
    if not value:
        break
    data[key] = value

if data:
    person_data(**data)
