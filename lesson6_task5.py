class Stationery():
    title = ''
    def draw(self):
       print("Запуск отрисовки")

class Pen(Stationery):
    title = 'pen'

    def draw(self):
        print(f"Пишу с помощью {self.title}")

class Pencil(Stationery):
    title = 'pencil'

    def draw(self):
        print(f"Рисую с помощью {self.title}")

class Handle(Stationery):
    title = 'handle'

    def draw(self):
        print(f"Закрашиваю с помощью {self.title}")

s1 = Pen()
s1.draw()

s2 = Pencil()
s2.draw()

s3 =  Handle()
s3.draw()