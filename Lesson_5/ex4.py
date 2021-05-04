# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.

numerals = ('Один', 'Два', 'Три', 'Четыре')
result = ''

with open('ex4.txt', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        numeral, number = line.split('-')
        number = int(number)
        result = f'{result}{numerals[number - 1]} - {number}\n'

with open('ex4_rus.txt', 'wt', encoding='utf-8') as output_file:
    output_file.write(result)
