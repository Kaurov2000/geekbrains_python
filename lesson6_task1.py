from time import sleep,clock
from itertools import cycle

class TrafficLight:

    def running(self):
        """Я использую цикл светофора как в жизни, а не как в условии задачи"""
        running_cycle = {'Red':7,'Green': 10,'Yellow':2}
        for i in cycle(running_cycle.keys()):
            self.__color = i
            print(f"Uptime is {round(clock(),2)} seconds, color changed to {self.__color}")
            sleep(running_cycle[i])

t = TrafficLight()
t.running()