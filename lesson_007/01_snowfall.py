# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 400)
N = 20
flakes = []  # Список снежинок


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x = sd.random_number(b=800)
        self.y = sd.random_number(a=200, b=400)
        self.length = sd.random_number(a=10, b=40)
        self.point = sd.get_point(self.x, self.y)

    def draw(self, color=sd.COLOR_WHITE):
        sd.snowflake(center=self.point, length=self.length, color=color)

    def move(self):
        self.x += sd.random_number(a=-10, b=10)
        self.y -= sd.random_number(a=0, b=10)
        self.point = sd.get_point(self.x, self.y)

    def can_fall(self):
        """Если еще не упала - возврат True"""
        if self.y > -self.length:
            return True
        else:
            return False

    def clear_previous_picture(self):
        """Стереть предыдущую отрсовку"""
        sd.snowflake(center=self.point, length=self.length, color=sd.background_color)


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:


def get_flakes(count=N):
    """Создать count снежинок"""
    for _ in range(count):
        flakes.append(Snowflake())


def get_fallen_flakes(flakes=flakes):
    """Подсчитать сколько снежинок уже упало и удалить упавшие из списка снежинок"""
    count = 0
    for flake in flakes:
        if not flake.can_fall():
            i = flakes.index(flake)
            flakes.pop(i)
            count += 1
    return count


def append_flakes(count):
    for i in range(count):
        flakes.append(Snowflake())


get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes)  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
