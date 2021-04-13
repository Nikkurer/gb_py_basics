def max_num():
    message = 'Введите целое положительное число:'
    number = input(message)
    max_digit = 0
    for digit in str(number):
        digit = int(digit)
        if digit > max_digit:
            max_digit = digit
    print(f'Максимальная цифра в числе {number}: {max_digit}')


if __name__ == "__main__":
    max_num()
