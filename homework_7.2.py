# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для опредления расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Cloth(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def formula(self):
        pass

    def __add__(self, other):
        Cloth.result += self.formula + other.formula
        return Costume(0)

    def __str__(self):
        return f'{Cloth.result}'


class Coat(Cloth):
    @property
    def formula(self):
        return round(self.param / 6.5) + 0.5


class Costume(Cloth):
    @property
    def formula(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(44)
costume = Costume(160)
print(coat + costume + coat)
