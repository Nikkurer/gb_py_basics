# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать
# два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.
import re


class Date:
    date: str

    def __init__(self, date: str):
        if re.match(r'(\d{2}-){2}\d{4}', date):
            self.date = date

    @classmethod
    def to_int(cls, date: str):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def valid(date: str):
        days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day, month, year = Date.to_int(date)
        if 0 < day < days_per_month[month] and 0 < month < 13:
            return True
        else:
            return False


if __name__ == '__main__':
    date_str = '30-02-1975'
    date = Date(date_str)
    print(Date.to_int(date_str))
    if date.valid(date_str):
        print(f'{date_str} is valid date')
    else:
        print(f'{date_str} is not valid date')
