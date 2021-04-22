# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

import sys


def salary(x, y, z):
    return x * y + z


if __name__ == '__main__':
    hours_worked = float(sys.argv[1])
    rate = float(sys.argv[2])
    premium = float(sys.argv[3])
    print(salary(hours_worked, rate, premium))
