# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

words = []
filename = 'ex2.txt'
with open(filename, mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f'В файле {len(lines)} строк')
    for number, line in enumerate(lines):
        print(f'В {number + 1} строке {len(line.split())} слов')
