# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.

user_data = None
filename = 'user_data.txt'
with open(filename, mode='wt', encoding='utf-8') as f:
    while True:
        user_data = input('Введите данные: ')
        if not user_data:
            break
        f.write(f'{user_data}\n')
        f.flush()
