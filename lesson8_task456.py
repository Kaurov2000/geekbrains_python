import copy


class AmountError(Exception):
    def __init__(self, x, y, wh, eq_name):
        self.x = x
        self.y = y
        self.wh = wh
        self.eq_name = eq_name

    def __str__(self):
        return f"Нельзя забрать {self.x} единиц техники {self.eq_name} со склада {self.wh}, т.к. их всего {self.y}"


class ExitMenu(Exception):
    def __init__(self):
        print("back to main menu")


class Warehouse:
    def __init__(self, wh_name):
        self.wh_name = wh_name
        self.total_equipment_amount = 0
        self.equipment = {"Printer": [], "Scanner":  [], "Copier": []}

    def __str__(self):
        ret = f"{self.wh_name}: \n"
        for eq_type in self.equipment.keys():
            for eq in self.equipment[eq_type]:
                ret = ret + f"{eq_type} " + f"{str(eq)}\n"
        return ret

    def get_equipment(self, eq):
        flag = False
        for p in self.equipment[eq.__class__.__name__]:
            if p.model == eq.model:
                p.amount += eq.amount
                flag = True
        if not flag:
            self.equipment[eq.__class__.__name__].append(eq)

    def remove_equipment(self, eq):
        flag = False
        for p in self.equipment[eq.__class__.__name__]:
            if p.model == eq.model:
                if p.amount < eq.amount:
                    raise AmountError(eq.amount, p.amount, self.wh_name, eq.model)
                elif p.amount == eq.amount:
                    self.equipment[eq.__class__.__name__].remove(eq)
                    flag = True
                else:
                    p.amount -= eq.amount
                    flag = True
        if not flag:
            raise AmountError(eq.amount, 0, self.wh_name, eq.model)

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

    def __str__(self):
        return f"{self.model} - {self.amount}"


class Printer(OfficeEquipment):
    def __init__(self, model, print_method, color, amount):
        OfficeEquipment.__init__(self, model, amount)
        self.print_method = print_method
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, model, resolution, amount):
        OfficeEquipment.__init__(self, model, amount)
        self.resolution = resolution


class Copier(Printer, Scanner):
    def __init__(self, model, print_method, color, resolution, amount):
        Printer.__init__(self, model, print_method, color, 0)
        Scanner.__init__(self, model, resolution, amount)


class MainMenu:
    def show_menu(self):
        while True:
            print("Добро пожаловать на Склад Оргтехики")
            print("Вы можете: ")
            print("[1] - получить технику на Центральный склад")
            print("[2] - передать технику между складом и подразделениями")
            print("[3] - создать подразделение")
            print("Выйти из программы, если введете любой другой ответ")
            answer = input("Какое действие вы хотите совершить? ")
            if answer == '1':
                try:
                    eq = self.create_equipment()
                    CWH.get_equipment(eq)
                except ExitMenu:
                    continue
            elif answer == '2':
                print("Откуда переместить оборудование?")
                wh_from = self.choose_wh()
                print("Куда переместить оборудование?")
                wh_to = self.choose_wh()
                eq = self.choose_equipment(wh_from)
                wh_from.move_equipment(wh_to, eq)
            elif answer == '3':
                self.create_wh()
            else:
                print("Досвидания!")  # exit
                break

    def create_equipment(self):
        t = input("Выберите тип оборудования: 1 - Принтер, 2 - Сканер, 3 - Копир: ")
        if t == '1':
            model = input("Введите модель: ")
            print_method = input("Введите технологию печати: ")
            color = input("Цветной? ")
            if color == 'True':
                color = True
            elif color == 'False':
                color = False
            else:
                print(f"Неверное значение {color}")
                raise ExitMenu
            amount = input("Введите количество: ")
            try:
                amount = int(amount)
            except ValueError:
                print(f"Неверное значение {amount}")
                raise ExitMenu
            return Printer(model, print_method, color, amount)
        elif t == '2':
            model = input("Введите модель: ")
            resolution = input("Введите разрешение сканирования: ")
            amount = input("Введите количество: ")
            try:
                amount = int(amount)
            except ValueError:
                print(f"Неверное значение {amount}")
                raise ExitMenu
            return Scanner(model, resolution, amount)
        elif t == '3':
            model = input("Введите модель: ")
            print_method = input("Введите технологию печати: ")
            color = input("Цветной? ")
            if color == 'True':
                color = True
            elif color == 'False':
                color = False
            else:
                print(f"Неверное значение {color}")
                raise ExitMenu
            resolution = input("Введите разрешение сканирования: ")
            amount = input("Введите количество: ")
            try:
                amount = int(amount)
            except ValueError:
                print(f"Неверное значение {amount}")
                raise ExitMenu
            return Copier(model, print_method, color, resolution, amount)
        else:
            print("Неизвестный тип оборудования")
            raise ExitMenu

    def choose_wh(self):
        i = 0
        for wh in WH_LIST:
            i += 1
            print(f"{i} - {wh.wh_name}")
        ans = int(input("Укажите склад: "))
        return WH_LIST[ans-1]

    def choose_equipment(self, wh):
        i = 0
        l = []
        print("На складе есть следующие типы оборудования: ")
        for eq_type in wh.equipment.keys():
            i += 1
            l.append(eq_type)
            print(f"{i} - {eq_type}")
        ans = int(input("Укажите тип: "))
        eq_list = wh.equipment.get(l[ans-1])
        print("На складе есть следующее оборудование этого типа: ")
        i = 0
        for eq in eq_list:
            i += 1
            print(f"{i} - {eq}")
        ans = int(input("Укажите оборудование: "))
        eq = copy.copy(eq_list[ans-1])
        eq.amount = int(input("Укажите количество:"))
        return eq

    def create_wh(self):
        wh_name = input("Введите название подразделения: ")
        new_wh = Warehouse(wh_name)
        WH_LIST.append(new_wh)


CWH = Warehouse('Central Warehouse')
AD = Warehouse('Accounts Department')
WH_LIST = [CWH, AD]
p1 = Printer('Epson L220', 'inc', True, 5)
CWH.get_equipment(p1)
p2 = Printer('Xerox 3020BI', 'laser', False, 6)
CWH.get_equipment(p2)
s = Scanner('HP ScanJet 3200', 4800, 3)
CWH.get_equipment(s)
c = Copier("Canon MF3010", 'laser', False, 4800, 7)
CWH.get_equipment(c)
CWH.move_equipment(AD, p2)

mm = MainMenu()
mm.show_menu()

for d in WH_LIST:
    print(d)

