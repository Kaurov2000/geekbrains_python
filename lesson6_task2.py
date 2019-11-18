class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def evaluate_asphalt_amount(self, density = 25, layers = 5):
        self._density = density
        self._layers = layers
        return round(self._length * self._width * self._density * self._layers / 1000, 3)

lw = input("Введите длину и ширину дороги, разделенные пробелом: ")
try:
    road_lw = map(float, lw.split())
    if len(lw.split()) > 2:
        raise ValueError
except ValueError:
    print("Ошибка при вводе значений")

dl = input("Введите плотность асфальта и количество слоев, либо нажмите Enter для продолжения: ")
try:
    asph_dl = map(float, dl.split())
    if len(dl.split()) > 2:
        raise ValueError
except ValueError:
    print("Ошибка при вводе значений")
r = Road(*road_lw)
print(f"Для покрытия дорожного полотна потребуется {r.evaluate_asphalt_amount(*asph_dl)} тонн асфальта")

