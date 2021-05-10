# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и
# рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
# методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

class Clothes:
    name: str
    fabric_amount: float

    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    size: float

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_fabric_amount(self):
        self.fabric_amount = self.size / 6.5 + 0.5
        return self.fabric_amount


class Suite(Clothes):
    height: float

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def get_fabric_amount(self):
        self.fabric_amount = self.height * 2 + 0.3
        return self.fabric_amount


if __name__ == '__main__':
    suite = Suite('костюм', 1.83)
    print(f'На {suite.name} необходимо {suite.get_fabric_amount():.2f} '
          f'метров ткани')
    coat = Coat('шинель', 52)
    print(f'На {coat.name} необходимо {coat.get_fabric_amount():.2f} '
          f'метров ткани')
    print(f'Всего понадобится {suite.fabric_amount + coat.fabric_amount} '
          f'метров ткани')
