# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    numbers = [num1, num2, num3]
    maxes = []
    for index in range(2):
        maxes.append(numbers.pop(numbers.index(max(numbers))))
    return sum(maxes)


if __name__ == '__main__':
    my_func(1, 2, 3)
