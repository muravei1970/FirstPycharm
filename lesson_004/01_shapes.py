# -*- coding: utf-8 -*-

import simple_draw as sd
import math

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

sd.resolution = (800, 400)
start_point_x = 400
start_point_y = 150
start_point = sd.get_point(start_point_x, start_point_y) # Стартовая точка
number_of_angles = 4 # Количество углов
angle = 156 # Начальный угол
angle_offset = 360/number_of_angles # Смещение угла
length = 100

# Функция рисования треугольника

def triangle(start_point, angle, length):
    for _ in range(3):
        vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        end_point = vector.end_point
        sd.line(start_point=start_point, end_point=end_point)
        start_point = end_point
        angle = angle - 360/3


# triangle(start_point, angle, length)

# Функция рисования четырехугольника

def quadrangle(start_point, angle, length):
    for _ in range(4):
        vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        end_point = vector.end_point
        sd.line(start_point=start_point, end_point=end_point)
        start_point = end_point
        angle = angle - 360/4

# quadrangle(start_point, angle, length)

# Функция рисования пятиугольника

def pentagon(start_point, angle, length):
    for _ in range(5):
        vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        end_point = vector.end_point
        sd.line(start_point=start_point, end_point=end_point)
        start_point = end_point
        angle = angle - 360/5

# pentagon(start_point, angle, length)

# Функция рисования шестиугольника

def hexagon(start_point, angle, length):
    for _ in range(6):
        vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        end_point = vector.end_point
        sd.line(start_point=start_point, end_point=end_point)
        start_point = end_point
        angle = angle - 360/6

# hexagon(start_point, angle, length)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Функция многоугольник - общая функция

def polygon(start_point, angle, length, number_of_angles):
    for _ in range(number_of_angles):
        vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        end_point = vector.end_point
        sd.line(start_point=start_point, end_point=end_point)
        start_point = end_point
        angle = angle - 360/number_of_angles

# Новая функция рисования треугольника

def triangle_new(start_point, angle, length):
    number_of_angles = 3
    polygon(start_point, angle, length, number_of_angles)

# triangle_new(start_point, angle, length)

# Новая функция рисования четырехугольника

def quadrangle_new(start_point, angle, length):
    number_of_angles = 4
    polygon(start_point, angle, length, number_of_angles)

# quadrangle_new(start_point, angle, length)

# Новая функция рисования пятиугольника

def pentagon_new(start_point, angle, length):
    number_of_angles = 5
    polygon(start_point, angle, length, number_of_angles)

# pentagon_new(start_point, angle, length)

# Новая функция рисования шестиугольника

def hexagon_new(start_point, angle, length):
    number_of_angles = 6
    polygon(start_point, angle, length, number_of_angles)

# hexagon_new(start_point, angle, length)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
