# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать
# параметр, соответствующий количеству ячеек клетки (целое число). В классе
# должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление
# клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
# разность количества ячеек двух клеток больше нуля, иначе выводить
# соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр
# класса и количество ячеек в ряду. Данный метод позволяет организовать
# ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n***...,
# где количество ячеек между \n равно переданному аргументу. Если ячеек на
# формирование ряда не хватает, то в последний ряд записываются все
# оставшиеся. Например, количество ячеек клетки равняется 12, количество
# ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****. Подсказка:
# подробный список операторов для перегрузки доступен по ссылке.
class Cell:
    cell_number: int

    def __init__(self, cell_number: int):
        if isinstance(cell_number, int):
            self.cell_number = cell_number

    def __add__(self, other: 'Cell'):
        if isinstance(other, Cell):
            result = self.cell_number + other.cell_number
        else:
            raise TypeError
        return Cell(result)

    def __sub__(self, other: 'Cell'):
        if isinstance(other, Cell):
            result = self.cell_number - other.cell_number
            if result > 0:
                return Cell(result)
            else:
                print(f'Операция не допустима. Результат меньше или равен 0')
                exit(1)
        else:
            raise TypeError

    def __mul__(self, other: 'Cell'):
        if isinstance(other, Cell):
            result = self.cell_number * other.cell_number
            return Cell(result)
        else:
            raise TypeError

    def __truediv__(self, other: 'Cell'):
        if isinstance(other, Cell):
            result = self.cell_number // other.cell_number
            return Cell(result)
        else:
            raise TypeError

    def make_order(self, other: 'Cell', elements: int):
        row = f'{"*" * elements}\n'
        cycles, rest = divmod(other.cell_number, elements)
        result = f'{row * cycles}{"*" * rest}'
        return result


if __name__ == '__main__':
    first = Cell(5)
    second = Cell(3)
    print((first + second).cell_number)
    print((first - second).cell_number)
    print((first / second).cell_number)
    print((first * second).cell_number)
    print(second.make_order(first, 3))
    print((second - first).cell_number)
