# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод init()), который должен принимать данные (список списков) для
# формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы. Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
# привычном виде.
#
# Далее реализовать перегрузку метода add() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.
import random


class Matrix:
    rows: int
    columns: int
    data: list

    def __init__(self, rows, columns):
        self.data = []
        self.rows = rows
        self.columns = columns
        for row in range(self.rows):
            self.data.append(
                [number for number in random.sample(range(20), self.columns)])

    def __str__(self):
        matrix_str = ''
        for row in self.data:
            for element in row:
                matrix_str = f'{matrix_str}{element:2d} '
            matrix_str = f'{matrix_str}\n'
        return matrix_str


if __name__ == '__main__':
    mx1 = Matrix(3, 3)
    mx2 = Matrix(3, 3)
    print(mx1, '\n')
    print(mx2)
