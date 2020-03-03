# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 400)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# point = sd.get_point(100, 100)
# radius = 50

# Запуск цикла рисования пузырька
# for _ in range(3):
#     sd.circle(center_position=point, radius=radius, width=2)
#     radius += 5

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step, color):
    radius = 20
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2, color=color)
        radius += step


# Запуск функции рисования пузырька
# point = sd.get_point(300, 300)
# bubble(point=point, step=10, color=sd.COLOR_YELLOW)

# Нарисовать 10 пузырьков в ряд

# for x in range(30, 571, 60):
#     point = sd.get_point(x, 100)
#     bubble(point = point, step=5, color=sd.COLOR_YELLOW)


# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 221, 60):
#     for x in range(30, 571, 60):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5, color=sd.COLOR_YELLOW)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    bubble(point, 5, color)

sd.pause()
