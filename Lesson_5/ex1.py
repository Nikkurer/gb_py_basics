# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.

user_data = None
filename = 'user_data.txt'
with open(filename, mode='wt', encoding='utf-8') as f:
    while True:
        user_data = input('Введите данные: ')
        if user_data != '':
            f.write(user_data)
            f.flush()
        else:
            break
        f.write('\n')
