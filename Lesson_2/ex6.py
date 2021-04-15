def ask_next():
    message = 'Ещё один товар? (д/н) '
    answer = input(message)
    print('\033[K', end='\r')
    if answer in 'дДyY':
        return True
    else:
        return False


def get_product():
    product = {}
    print('Введите характеристики товара:')
    for feature in analytics.keys():
        value = input(f'{feature}: ')
        if value == '':
            print('ОШИБКА! Повторите ввод товара!')
            return 0
        if feature in ('цена', 'количество'):
            value = int(value)
        product[feature] = value
        analytics[feature].append(value)
    return product


def get_products():
    products = []
    get_next = True
    index = 0
    while get_next:
        index += 1
        product = get_product()
        if product:
            products.append((index, product))
        get_next = ask_next()
    return products


def make_db():
    for product in get_products():
        print(product)
    print('Аналитика:')
    for feature in analytics:
        print(f'{feature}: {analytics[feature]}')


analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
if __name__ == '__main__':
    make_db()
