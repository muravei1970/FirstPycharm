# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

sd.resolution = (800, 400)
root_point = sd.get_point(300, 30)

# def draw_bunches(start_point, angle=90, length=100, delta=30):
#     v1 = sd.get_vector(start_point=root_point, angle=angle - delta, length=length, width=3)
#     v1.draw()
#     next_point_1 = v1.end_point
#     v2 = sd.get_vector(start_point=root_point, angle=angle + delta, length=length, width=3)
#     v2.draw()
#     next_point_2 = v2.end_point
#
# draw_bunches(start_point=root_point)
#---------------------------------------------------------------------------------------

# delta = 30
# next_point = root_point # Начальные условия
# next_angle = 90 # Начальные условия
# next_length = 100 # Начальные условия
#
#
# def draw_bunches(next_point, next_angle=90, next_length=100, delta=30):
#     if next_length < 10:
#         return
#     v1 = sd.get_vector(start_point=next_point, angle=next_angle - delta, length=next_length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=next_point, angle=next_angle + delta, length=next_length, width=3)
#     v2.draw()
#     next_length *= .75
#     next_point = v1.end_point
#     next_angle = v1.angle
#     draw_bunches(next_point=next_point, next_angle=next_angle, next_length=next_length)
#     next_point = v2.end_point
#     next_angle = v2.angle
#     draw_bunches(next_point=next_point, next_angle=next_angle, next_length=next_length)
#
# draw_bunches(next_point=root_point)
#-------------------------------------------------------------------------------------------------


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


delta = 30 # Начальные условия
next_point = root_point # Начальные условия
next_angle = 90 # Начальные условия
next_length = 100 # Начальные условия

def delta_var(delta=30): # Рандомное отклонение ветвей
    return delta * (1 + sd.random_number(a=-4, b=4) / 10)


def draw_bunches(next_point, next_angle=90, next_length=100, delta=30):
    if next_length < 10:
        return
    v1 = sd.get_vector(start_point=next_point, angle=next_angle - delta, length=next_length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=next_point, angle=next_angle + delta, length=next_length, width=3)
    v2.draw()
    next_length *= .75 * (1 + sd.random_number(a=-2, b=2) / 10)
    next_point = v1.end_point
    next_angle = v1.angle
    draw_bunches(next_point=next_point, next_angle=next_angle, next_length=next_length, delta=delta_var())
    next_point = v2.end_point
    next_angle = v2.angle
    draw_bunches(next_point=next_point, next_angle=next_angle, next_length=next_length, delta=delta_var())

draw_bunches(next_point=root_point, delta=delta_var())


sd.pause()


