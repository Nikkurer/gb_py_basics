# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1: float, num2: float, num3: float) -> float:
    """
    :param num1: дейсвительное число
    :param num2: дейсвительное число
    :param num3: дейсвительное число
    :returns: сумма двух наибольших аргументов
    """
    numbers = [num1, num2, num3]
    maxes = []
    for index in range(2):
        maxes.append(numbers.pop(numbers.index(max(numbers))))
    return sum(maxes)


if __name__ == '__main__':
    print(my_func(1, 2, 3))
