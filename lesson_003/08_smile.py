# -*- coding: utf-8 -*-

# (определение функций)
from random import randrange

import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
sd.resolution = (800, 400)


def smile(x, y, color=sd.COLOR_YELLOW):

    # Эллипс - голова
    left_bottom_x = x
    right_top_x = x + 100
    left_bottom_y = y
    right_top_y = y + 70
    left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
    right_top = sd.get_point(right_top_x, right_top_y)
    sd.ellipse(left_bottom=left_bottom, right_top=right_top, color=color, width=3)

    # Глаза
    left_eye_y = right_eye_y = right_top_y - 30
    left_eye_x = left_bottom_x + 30
    right_eye_x = right_top_x - 30
    left_eye = sd.get_point(left_eye_x, left_eye_y)
    right_eye = sd.get_point(right_eye_x, right_eye_y)
    eye_radius = 7
    sd.circle(center_position=left_eye, color=color, radius=eye_radius)
    sd.circle(center_position=right_eye, color=color, radius=eye_radius)

    # Рот
    point_list_x = [left_bottom_x + 20, left_bottom_x + 40, right_top_x - 40, right_top_x - 20]
    point_list_y = [left_bottom_y + 25, left_bottom_y + 15, left_bottom_y + 15, left_bottom_y + 25]
    point_list = []
    for i in range(4):
        point_list.append(sd.get_point(point_list_x[i], point_list_y[i]))
    sd.lines(point_list=point_list, color=color)


for i in range(10):
    x = randrange(0, 700)
    y = randrange(0, 330)
    smile(x, y)

sd.pause()
