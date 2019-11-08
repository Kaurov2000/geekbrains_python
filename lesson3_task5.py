# coding: utf-8


def my_func():
    global exit_command
    s = input()
    if s.find('q') > -1:
        exit_command = 1
        z = s.find('q')
        s = s[:z]
    l = s.split()
    sum = 0
    for i in l:
        try:
            sum = sum + int(i)
        except ValueError:
            print(f"Неверно введенное значение '{i}' исключено из расчета суммы")
    return sum

print("Введите числа, разделенные пробелом или символ 'q' для выхода: \n")
sum = 0
exit_command = 0
while exit_command == 0:
    sum = sum + my_func()
    print(f"Сумма чисел равна: {sum}")