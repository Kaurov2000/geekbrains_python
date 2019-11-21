class ElemenNotNumber(Exception):
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return f"Введенный элемент {self.x} не является числом"
class NumList:
    num_list=[]
    def add_num(self,x):
        try:
            self.__num_checker(x)
        except ElemenNotNumber as e:
            print(e)
        else:
            self.num_list.append(x)
    def __num_checker(self,x):
        for d in x:
            if not d.isdigit():
                raise ElemenNotNumber(x)
    def __str__(self):
        return str(self.num_list)

nlist = NumList()
while True:
    x = input(f"Введите {len(nlist.num_list)} элемент списка или пустую строку для выхода: ")
    if x == '':
       break
    else:
        nlist.add_num(x)
print(nlist)
