# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
# формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
import random

list_len = 10


def new_list(orig):
    return [original_list[index] for index in range(1, list_len)
            if original_list[index] > original_list[index - 1]]


original_list = [random.randint(1, 200) for _ in range(list_len)]
print(new_list(original_list))
