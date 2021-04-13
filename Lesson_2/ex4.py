def get_string():
    message = 'Введите строку из нескольких слов: '
    return input(message).split()


def print_words():
    array = get_string()
    for element in enumerate(array):
        print(f'{element[0] + 1}\t{element[1]:10}')


if __name__ == '__main__':
    print_words()
