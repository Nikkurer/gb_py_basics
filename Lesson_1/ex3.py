def iter_sum():
    numbers = []
    cycles = 3
    message = 'Введите число:'
    number = input(message)
    for cycle in range(cycles):
        numbers.append(int(number * (cycle + 1)))
    print('Сумма чисел {} равна {:,}'.format(numbers,
                                             sum(numbers)).replace(',', ' '))


if __name__ == "__main__":
    iter_sum()
