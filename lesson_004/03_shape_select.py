# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def polygon(start_point, number_of_angles, angle=155, length=100, color=sd.COLOR_YELLOW):
    for _ in range(number_of_angles):
        vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        end_point = vector.end_point
        sd.line(start_point=start_point, end_point=end_point, color=color)
        start_point = end_point
        angle = angle - 360/number_of_angles


# Новая функция рисования треугольника


def triangle_new(start_point, angle=155, length=100, color=sd.COLOR_YELLOW):
    number_of_angles = 3
    polygon(start_point=start_point, angle=angle, length=length, number_of_angles=number_of_angles, color=color)


# Новая функция рисования четырехугольника


def quadrangle_new(start_point, angle=155, length=100, color=sd.COLOR_YELLOW):
    number_of_angles = 4
    polygon(start_point=start_point, angle=angle, length=length, number_of_angles=number_of_angles, color=color)


# Новая функция рисования пятиугольника


def pentagon_new(start_point, angle=155, length=100, color=sd.COLOR_YELLOW):
    number_of_angles = 5
    polygon(start_point=start_point, angle=angle, length=length, number_of_angles=number_of_angles, color=color)


# Новая функция рисования шестиугольника


def hexagon_new(start_point, angle=155, length=100, color=sd.COLOR_YELLOW):
    number_of_angles = 6
    polygon(start_point=start_point, angle=angle, length=length, number_of_angles=number_of_angles, color=color)


sd.resolution = (800, 400)

shapes = ["треугольник", "квадрат", "пятиугольник", "шестиугольник"]
start_point = sd.get_point(400, 170)


print("Возможные фигуры: ")
for i, sh in enumerate(shapes, 1):
    print(str(i) + " : " + sh)

while True:
    input_shape = input("Введите желаемую фигуру: ")
    if input_shape == "1":
        triangle_new(start_point)
        break
    elif input_shape == "2":
        quadrangle_new(start_point)
        break
    elif input_shape == "3":
        pentagon_new(start_point)
        break
    elif input_shape == "4":
        hexagon_new(start_point)
        break
    else:
        print("Вы ввели некорректный номер!")
        continue



sd.pause()
