import ex1
from ex2 import print_user_info

numbers = (5, 2)
print(ex1.devision(*numbers))

user = {'имя': 'Alex', 'фамилия': 'Johnson', 'год рождения': 1976,
        'город проживания': 'Los Angeles', 'email': 'ajohnson@contoso.com',
        'телефон': '+1(213)893-1239'}
print_user_info(name=user['имя'], surname=user['фамилия'],
                birth_year=user['год рождения'],
                city=user['город проживания'], email=user['email'],
                phone_number=user['телефон'])
