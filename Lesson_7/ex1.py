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

    def fill_matrix(self):
        for row in range(self.rows):
            self.data.append(
                [number for number in random.sample(range(99), self.columns)])

    def __len__(self):
        return len(self.data)

    def __str__(self):
        matrix_str = ''
        for row in self.data:
            # TODO: Заменить вложенный цикл на функцию
            for element in row:
                matrix_str = f'{matrix_str}{element:2d} '
            matrix_str = f'{matrix_str}\n'
        return matrix_str

    def add(self, matrix):
        result = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            result.data.append([])
            for element in range(self.columns):
                new_element = self.data[row][element] + matrix.data[row][
                    element]
                result.data[row].append(new_element)
        return result


if __name__ == '__main__':
    mx1 = Matrix(3, 3)
    mx1.fill_matrix()
    mx2 = Matrix(3, 3)
    mx2.fill_matrix()
    print(mx1)
    print(mx2)
    print(mx1.add(mx2))
