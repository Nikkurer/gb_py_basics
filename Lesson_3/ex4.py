"""
Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении
задания необходимо обойтись без встроенной функции возведения числа в
степень.

** Подсказка:** попробуйте решить задачу двумя способами. Первый —
возведение в степень с помощью оператора **. Второй — более сложная
реализация без оператора **, предусматривающая использование цикла.
"""


# def my_func_v1(x, y):
#     return x**y

def my_func(x: float, y: int) -> float:
    """
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :returns: x в степени y
    """
    iterations = abs(y) - 1
    product = 1 / x
    for _ in range(iterations):
        product = product * 1 / x
    return product


if __name__ == '__main__':
    x = 2
    y = -3
    print(my_func(x, y))
