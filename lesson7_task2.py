from abc import ABC,abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self,size):
        pass
    @abstractmethod
    def material_need(self):
        pass

class Coat(Clothes):
    def __init__(self,size):
        self.size = size
    @property
    def material_need(self):
        return self.size / 6.5 + 0.5

class Jacket(Clothes):
    def __init__(self,height):
        self.height = height
    @property
    def material_need(self):
        return self.height * 2 + 0.3

c = Coat(48)
j = Jacket(1.76)
print(c.material_need)
print(j.material_need)