# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.

def print_user_info(**fields):
    """
    Выводит данные о пользователе в одну строку
    :param fields: данные о пользователе
    """
    output = ''
    for field, value in fields.items():
        output = f'{output}{field}: {value} '
    print(output)


def user_input(func):
    try:
        return func(input(prompt))
    except ValueError:
        print('Некорректный ввод! Введите корректные данные')


if __name__ == '__main__':
    user = {'имя': str, 'фамилия': str, 'год рождения': int,
            'город проживания': str, 'email': str, 'телефон': str}

    print('Введите данные о пользователе: ')
    for field, value in user.items():
        prompt = f'{field}: '
        success = False
        while not success:
            user[field] = user_input(value)
            success = True

    print_user_info(name=user['имя'], surname=user['фамилия'],
                    birth_year=user['год рождения'],
                    city=user['город проживания'], email=user['email'],
                    phone_number=user['телефон'])
