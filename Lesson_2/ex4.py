def get_number():
    message = 'Введите натуральное число: '
    element = input(message)
    if not element.isnumeric():
        print('ОШИБКА! Вы ввели некорректные данные!')
        exit(1)
    return int(element)


def rating():
    numbers = [7, 5, 3, 3, 2]
    number = get_number()
    for element in numbers:
        if element < number:
            index = numbers.index(element)
            break
        elif element == number:
            index = numbers.index(element)
        else:
            index = numbers.index(element) + 1
    numbers.insert(index, number)
    return numbers


if __name__ == '__main__':
    rating()
