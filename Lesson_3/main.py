import ex1
from ex2 import print_user_info
from ex3 import my_func

numbers = (5, 2)
print(f'Задание 1:\n{ex1.devision(*numbers)}\n')

print('Задание 2')
user = {'имя': 'Alex', 'фамилия': 'Johnson', 'год рождения': 1976,
        'город проживания': 'Los Angeles', 'email': 'ajohnson@contoso.com',
        'телефон': '+1(213)893-1239'}
print_user_info(name=user['имя'], surname=user['фамилия'],
                birth_year=user['год рождения'],
                city=user['город проживания'], email=user['email'],
                phone_number=user['телефон'])
print('\n')

print(f'Задание 3:\n{my_func(-3, -5, 2)}')
