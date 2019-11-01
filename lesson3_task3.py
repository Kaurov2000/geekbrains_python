# encoding = 'utf-8'

def my_func(a,b,c):
    l = [a,b,c]
    l.sort(reverse=True)
    sum1 = l.pop(0)
    l.sort(reverse=True)
    sum2 = l.pop(0)
    return sum1 + sum2

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

print(my_func(a,b,c))