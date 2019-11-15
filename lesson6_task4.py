class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self, speed):
        self.speed = speed
        print(f"{self.name} starts moving with speed {speed}")

    def stop(self):
        self.speed = 0
        print(f"{self.name} stopped")

    def turn(self,direction):
        print(f"{self.name} turned {direction}")

    def show_speed(self):
        print(f"{self.name} moves with speed {self.speed}")

class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        print(f"{self.name} moves with speed {self.speed}")
        if self.speed > self.max_speed:
            print(f"{self.name} moves too fast for a towncar")

class SportCar(Car):
    max_speed = 200

class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        print(f"{self.name} moves with speed {self.speed}")
        if self.speed > self.max_speed:
            print(f"{self.name} moves too fast for a workcar")

class PoliceCar(Car):
    max_speed = 100
    is_police = True

car1 = TownCar()
car1.name = 'Sandero'
car1.color = 'red'

car1.go(80)
car1.show_speed()