class Cell:
    def __init__(self,units):
            self.units = units
    def __add__(self, other):
        new_cell =  Cell(self.units + other.units)
        return new_cell
    def __sub__(self, other):
        sub = self.units - other.units
        if sub > 0:
            new_cell = Cell(sub)
            return new_cell
        else:
            print(f"Операция вычитания клетки, состоящей из {other.units} ячеек, из клетки, состоящей из {self.units}" \
                  + f" ячеек, невозможна")
    def __mul__(self, other):
        new_cell = Cell(self.units * other.units)
        return new_cell
    def __truediv__(self, other):
        new_cell = Cell(self.units // other.units)
        return new_cell
    def make_order(self,n):
        i = 1
        res = f''
        while i < self.units:
            res = res + f'*'
            if i % n == 0:
                res = res + f'\n'
            i = i + 1
        return res

a = Cell(10)
b = Cell(7)
c = a + b
print(c.units)
d = b - a
if d is None:
    print(f"Клетка не существует")
else:
    print(d.units)
d = a - b
if d is None:
    print(f"Клетка не существует")
else:
    print(d.units)
e = a * b
print(e.units)
f = a / b
print(f.units)
print(c.make_order(6))