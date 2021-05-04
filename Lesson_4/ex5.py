# Реализовать формирование списка, используя функцию range() и возможности
# генератора. В список должны войти четные числа от 100 до 1000 (включая
# границы). Необходимо получить результат вычисления произведения всех
# элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

# result = reduce(lambda x, y: x*y, [elem for elem in range(10, 1001, 2)])

min_elem = 10
max_elem = 1001
even_list = [elem for elem in range(min_elem, max_elem, 2)]
result = reduce(lambda elem1, elem2: elem1 * elem2, even_list)

if __name__ == '__main__':
    print(result)
