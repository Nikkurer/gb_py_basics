# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может
# продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма
# вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
# вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.


def user_input():
    input_error = False
    user_numbers = []
    message = 'Введите числа через пробел: '
    raw_numbers = input(message).split()
    for index in range(len(raw_numbers)):
        try:
            user_numbers.append(float(raw_numbers[index]))
        except ValueError:
            input_error = True
            break
    return user_numbers, input_error


def sum_input():
    error = False
    numbers_sum = 0
    while not error:
        numbers, error = user_input()
        numbers_sum = numbers_sum + sum(numbers)
    return numbers_sum


if __name__ == '__main__':
    print(sum_input())
