class AmountError(Exception):
    def __init__(self,x,y,wh,eq_name):
        self.x = x
        self.y = y
        self.wh = wh
        self.eq_name = eq_name
    def __str__(self):
        return f"Нельзя забрать {self.x} единиц техники {self.eq_name} со склада {self.wh}, т.к. их всего {self.y}"

class Warehouse:
    def __init__(self,wh_name):
        self.wh_name = wh_name
        self.total_equipment_amount = 0
        self.equipment = {"Printer": [], "Scanner":  [], "Copier": []}
    def get_equipment(self, eq):
        flag = False
        for p in self.equipment[eq.__class__.__name__]:
            if p.model == eq.model:
                p.amount += eq.amount
                flag = True
        if not flag:
            self.equipment[eq.__class__.__name__].append(eq)
    def remove_equipment(self,eq):
        flag = False
        for p in self.equipment[eq.__class__.__name__]:
            if p.model == eq.model:
                if p.amount < eq.amount:
                    raise AmountError(eq.amount,p.amount,self.wh_name,eq.model)
                elif p.amount == eq.amount:
                    self.equipment[eq.__class__.__name__].remove(eq)
                else:
                    p.amount -= eq.amount
                    flag = True
        if not flag:
            raise AmountError(eq.amount,0,self.wh_name,eq.model)
    def move_equipment(self, other, eq):
        try:
            self.remove_equipment(eq)
        except AmountError as err:
            print(err)
        else:
            other.get_equipment(eq)

class OfficeEquipment:
    def __init__(self, model, amount):
        self.amount = amount
        self.model = model

class Printer(OfficeEquipment):
    def __init__(self, model, print_method, color, amount):
        OfficeEquipment.__init__(self,model, amount)
        self.print_method = print_method
        self.color = color

class Scanner(OfficeEquipment):
    def __init__(self, model, resolution, amount):
        OfficeEquipment.__init__(self, model, amount)
        self.resolution = resolution

class Copier(Printer,Scanner):
    def __init__(self, model, print_method, color, resolution, amount):
        Printer.__init__(self, model, print_method, color, 0)
        Scanner.__init__(self, model, resolution, amount)

cwh = Warehouse('Central Warehouse')
ad = Warehouse('Acounts Department')
p1 = Printer('Epson L220', 'inc', True, 5)
cwh.get_equipment(p1)
p2 = Printer('Xerox 3020BI','laser',False,6)
cwh.get_equipment(p2)
s = Scanner('HP ScanJet 3200', 4800, 3)
cwh.get_equipment(s)
c = Copier("Canon MF3010", 'laser', False, 4800, 7)
cwh.get_equipment(c)
cwh.move_equipment(ad,p2)
print(cwh.equipment)
print(ad.equipment)

