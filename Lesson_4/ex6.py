# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо
# предусмотреть условие, при котором повторение элементов списка будет
# прекращено.
from itertools import count, cycle

if __name__ == '__main__':
    numbers = []
    start, end = 2, 10
    for num in count(start):
        numbers.append(num)
        if num >= end:
            break
    print(numbers)
    for number in cycle(numbers):
        print(number)
        if number == max(numbers):
            break
