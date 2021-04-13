def profit():
    message = 'Введите выручку и издержки фирмы: '
    revenue, costs = map(int, input(message).split())
    if revenue > costs:
        profitability = revenue - costs
        revenue_profitability = revenue / costs
        print(f'Компания прибыльна. Рентабельность выручки: '
              f'{revenue_profitability:.3f}')
        message = 'Введите количество сотрудников: '
        employes = int(input(message))
        profit_per_employe = profitability / employes
        print(f'Доход на сотрудника: {profit_per_employe:.3f}')
    else:
        print('Компания убыточна')


if __name__ == "__main__":
    profit()
