def seconds():
    message = 'Введите время в секундах:'
    time_seconds = int(input(message))
    hours, seconds = divmod(time_seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    print(f'Вы ввели {time_seconds}, это: {hours}:{minutes}:{seconds}')


if __name__ == "__main__":
    seconds()
