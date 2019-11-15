class Worker:

    def __init__(self,name,surname,position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 100000, "bonus": 60000}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

p1 = Position("Ivan","Petrov", "director")
p2 = Position("Vasiliy",'Zaycev','programmer')

p1._income = {"wage":150000,'bonus':100000}

print(f"{p1.get_full_name()} - {p1.position}, он зарабатывает {p1.get_total_income()}")
