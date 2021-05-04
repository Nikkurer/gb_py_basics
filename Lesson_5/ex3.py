# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
import random

a = 123
result = ''
salary_min = 20000
salary_sum = 0

with open('ex3.txt', mode='rt', encoding='utf-8') as input_file:
    employees = tuple(input_file)
    employee_number = random.randint(10, 20)
    # employee_number = len(employees)
    print('Сотрудники с окладом менее 20000:')
    for employee_raw in random.sample(employees, employee_number):
        employee, salary = employee_raw.split()
        salary = int(salary)
        salary_sum += salary
        if salary < salary_min:
            print(employee)
    print(f'Средний доход сотрудника: {salary_sum / employee_number:.2f}')
