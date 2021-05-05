# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar и
# WorkCar переопределите метод show_speed. При значении скорости свыше 60 (
# TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, name):
        self.name = name

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        turn = {'left': 'лево', 'right': 'право'}
        print(f'{self.name} повернул на{turn[direction]}')

    def show_speed(self):
        print(f'У {self.name} скорость: {self.speed}')


class SpeedLimit(Car):
    speed_limit: int

    def show_speed(self):
        print(f'У {self.name} скорость: {self.speed}')
        if self.speed > self.speed_limit:
            print('Скорость превышена')


class TownCar(SpeedLimit):
    speed_limit = 60


class WorkCar(SpeedLimit):
    speed_limit = 40


class PoliceCar(Car):
    is_police = True


class SportCar(Car):
    pass


if __name__ == '__main__':
    town = TownCar('Luigi')
    town.go(50)
    town.show_speed()
    town.speed = 40
    town.turn('left')
    town.stop()
    print()
    police = PoliceCar('Sheriff')
    town.go(70)
    town.show_speed()
    town.speed = 30
    town.turn('right')
    town.stop()
    print()
    sport = SportCar('Lightning McQuen')
    sport.go(90)
    work = WorkCar('Mater')
    work.go(20)
