# Представлен список чисел. Определить элементы списка, не имеющие
# повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения
# задания обязательно использовать генератор.
#
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [2, 7, 23, 1, 3, 10, 4, 11]
import random


def unique_list(orig):
    return [number for number in orig if orig.count(number) == 1]


original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

if __name__ == '__main__':
    orig_len = 40
    original_list = [random.randint(0, 20) for _ in range(orig_len)]
    print(f'{original_list}\n{unique_list(original_list)}')
