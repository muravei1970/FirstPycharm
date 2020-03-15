# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

colors = ({"Красный": sd.COLOR_RED, "Оранжевый": sd.COLOR_ORANGE, "Желтый": sd.COLOR_YELLOW,
           "Зеленый": sd.COLOR_GREEN, "Голубой": sd.COLOR_CYAN, "Синий": sd.COLOR_BLUE, "Пурпурный": sd.COLOR_PURPLE})


def polygon(start_point, angle, length, number_of_angles, color):
    for _ in range(number_of_angles):
        vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        end_point = vector.end_point
        sd.line(start_point=start_point, end_point=end_point, color=color)
        start_point = end_point
        angle = angle - 360/number_of_angles


# Новая функция рисования треугольника


def triangle_new(start_point, angle, length, color):
    number_of_angles = 3
    polygon(start_point, angle, length, number_of_angles, color)


# Новая функция рисования четырехугольника


def quadrangle_new(start_point, angle, length, color):
    number_of_angles = 4
    polygon(start_point, angle, length, number_of_angles, color)


# Новая функция рисования пятиугольника


def pentagon_new(start_point, angle, length, color):
    number_of_angles = 5
    polygon(start_point, angle, length, number_of_angles, color)


# Новая функция рисования шестиугольника


def hexagon_new(start_point, angle, length, color):
    number_of_angles = 6
    polygon(start_point, angle, length, number_of_angles, color)


sd.resolution = (800, 400)


print("Возможные цвета: ")
for i, col in enumerate(colors, 1):
    print(str(i) + " : " + col)
while True:
    input_color = input("Введите желаемый цвет: ")
    if input_color == "1":
        color = colors["Красный"]
        break
    elif input_color == "2":
        color = colors["Оранжевый"]
        break
    elif input_color == "3":
        color = colors["Желтый"]
        break
    elif input_color == "4":
        color = colors["Зеленый"]
        break
    elif input_color == "5":
        color = colors["Голубой"]
        break
    elif input_color == "6":
        color = colors["Синий"]
        break
    elif input_color == "7":
        color = colors["Пурпурный"]
        break
    else:
        print("Вы ввели некорректный цвет")
        continue


triangle_new(start_point=sd.get_point(250, 40), angle=155, length=100, color=color)
quadrangle_new(start_point=sd.get_point(650, 40), angle=155, length=100, color=color)
pentagon_new(start_point=sd.get_point(250, 200), angle=155, length=100, color=color)
hexagon_new(start_point=sd.get_point(650, 200), angle=155, length=100, color=color)


sd.pause()
