# Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в
# файле и выводить ее на экран.
import random

# result = ' '.join(map(str, [random.randrange(1, 50) for i in range(20)]))
numbers_list = [random.randrange(1, 50) for i in range(20)]
result = ' '.join(map(str, numbers_list))

with open('ex5.txt', 'wt', encoding='utf-8') as output_file:
    output_file.write(result)

with open('ex5.txt', 'rt', encoding='utf-8') as input_file:
    # print(sum(map(int, input_file.readline().split())))
    # input_file.seek(0)
    numbers_raw = input_file.readline()
    numbers_sum = sum(map(int, numbers_raw.split()))
    print(numbers_sum)
