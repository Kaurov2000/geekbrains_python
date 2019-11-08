# encoding = 'utf-8'

def devide_numbers(a,b):
    """
    Функция возвращает результат деления первого аргумента на второй.
    В случае деления на ноль, функция вернет строку с описанием ошибки
    :param a:
    :param b:
    :return: a / b
    """
    if b != 0:
        return a / b
    else:
        return 'division by zero'

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print(devide_numbers(a,b))