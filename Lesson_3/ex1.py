# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def devision(dividend: float, divider: float) -> float or str:
    """
    Делит первый параметр на второй.
    :param dividend:
    :param divider:
    :returns: Частное от деления первого параметра на второй
    """
    try:
        return dividend / divider
    except ZeroDivisionError:
        return 'На ноль делить ешё не умею =('


message = 'Пожалуйста, введите через пробел делимое и делитель: '

if __name__ == '__main__':
    try:
        numbers = map(float, input(message).split())
    except ValueError:
        print('Некорректный ввод! Введите числа')
        exit(1)

    print(devision(*numbers))
