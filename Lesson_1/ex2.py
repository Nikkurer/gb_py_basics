message = 'Введите время в секундах:'
time_seconds = int(input(message))
hours, time_seconds = divmod(time_seconds, 3600)
minutes, seconds = divmod(time_seconds, 60)
print(f'Вы ввели {time_seconds}, это: {hours}:{minutes}:{seconds}')