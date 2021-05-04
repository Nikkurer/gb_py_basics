# Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

with open('ex7.txt', 'r', encoding='utf-8') as input_file:
    balance_sum = 0
    companies_dict = {}
    for line in input_file:
        company_raw = line.split()
        company_name = company_raw[0]
        company_proceed = int(company_raw[2])
        company_costs = int(company_raw[3])
        balance = company_proceed - company_costs
        if balance > 0:
            balance_sum += balance
        companies_dict[company_name] = balance
average_profit = {"average_profit": balance_sum / len(companies_dict)}
companies_list = [companies_dict, average_profit]
with open('ex7_out.txt', 'wt', encoding='utf-8') as output_file:
    output_file.write(json.dumps(companies_list, ensure_ascii=False, indent=4))
