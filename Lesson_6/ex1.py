# Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В
# рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав
# экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    __color: str
    _colors = ('red', 'yellow', 'green')
    _modes = {_colors[0]: 7, _colors[1]: 2, _colors[2]: 8}

    def __init__(self):
        self.__color = self._colors[0]

    def running(self, color):
        print(f'Текущий цвет: {self.__color}')
        current_color_index = self._colors.index(self.__color)
        next_color_index = self._colors.index(color)
        if next_color_index - current_color_index == 1:
            self.__color = color
            print(f'Текущий цвет: {self.__color}\n')
            time.sleep(self._modes[color])
        else:
            raise Exception


if __name__ == '__main__':
    first = TrafficLight()
    first.running('yellow')
    first.running('green')
    first.running('red')
