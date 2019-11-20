"""
Name: complex
Version: 1.0
Summary: Операции с комплексными числами
"""

class ComplexNumber:
    def __init__ (self,re,im=0):
        self.re = re
        self.im = im
    def __str__(self):
        if self.im < 0:
            return f"{self.re} - {abs(self.im)}j"
        else:
            return f"{self.re} + {abs(self.im)}j"
    def __add__(self,other):
        return ComplexNumber(self.re + other.re, self.im + other.im)
    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)
    def __truediv__(self, other):
        new_re = (self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im ** 2)
        new_im = (self.im * other.re - self.re * other.im) / (other.re ** 2 + other.im ** 2)
        return ComplexNumber(new_re,new_im)

a = ComplexNumber(3,2)
b = ComplexNumber(2,-3)
c = a + b
print(c)
print(f"Проверка: ",complex(3,2) + complex(2,-3))
d = a * b
print(d)
print(f"Проверка: ",complex(3,2) * complex(2,-3))
e =  a / b
print(e)
print(f"Проверка: ",complex(3,2) / complex(2,-3))