numbers = []
cycles = 3
message = 'Введите число:'
number = input(message)
for cycle in range(cycles):
    numbers.append(int(number*(cycle+1)))
print(sum(numbers))