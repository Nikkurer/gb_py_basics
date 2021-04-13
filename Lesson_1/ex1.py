def hello():
    message = 'Привет!'
    print(message)
    name, age = input('Введите свои имя и возраст: ').split()
    print(f'{name.capitalize()}, вам {age} лет')


if __name__ == "__main__":
    hello()
