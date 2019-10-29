# encoding = 'utf-8'

a = int(input("Введите время в секундах: "))

hour = a // 3600
if hour // 10 == 0:
    hour = '0' + str(hour)
a = a % 3600
minute = a // 60
if minute // 10 == 0:
    minute = '0' + str(minute)
second = a % 60
if second // 10 == 0:
    second = '0' + str(second)

print(f"{hour:2}:{minute:2}:{second:2}")