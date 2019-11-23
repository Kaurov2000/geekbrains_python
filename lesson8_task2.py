class MyException(Exception):
    def __init__(self,txt):
        self.txt = txt

a = 100
b = 0
try:
    if b == 0:
        raise MyException("Нельзя делить на ноль")
    else:
        c = a / b
except MyException as err:
    print(err)
else:
    print(c)


