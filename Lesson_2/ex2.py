message = 'Введите елементы списка через пробел: '


def elements_exchange():
    array = input(message).split()
    for element in array:
        index = array.index(element)
        try:
            array[index + 1]
            if index % 2 == 0:
                array[index], array[index + 1] = array[index + 1], array[index]
        except IndexError:
            break
    print(array)


if __name__ == "__main__":
    elements_exchange()
