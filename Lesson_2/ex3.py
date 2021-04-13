def get_month():
    message = 'Введите номер месяца: '
    month = input(message)
    if not month.isnumeric() or int(month) > 12:
        print('ОШИБКА! Вы ввели некорректные данные!')
        exit(1)
    return int(month)


def detect_season():
    month = get_month()
    seasons = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8),
               'осень': (9, 10, 11)}
    for season in seasons:
        if month in seasons[season]:
            return season


if __name__ == '__main__':
    detect_season()
