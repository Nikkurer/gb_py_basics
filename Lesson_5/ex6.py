# Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести
# словарь на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
def sum_hours(data: tuple):
    result = 0
    for lesson_type in data:
        if lesson_type != '—':
            hours = lesson_type.split('(')[0]
            result += int(hours)
    return result


catalog = {}
with open('ex6.txt', 'rt', encoding='utf-8') as input_file:
    for line in input_file:
        subject_raw = tuple(line.split())
        subject_name = subject_raw[0]
        subject_hours_raw = subject_raw[1:]
        catalog[subject_name] = sum_hours(subject_hours_raw)
print(catalog)
