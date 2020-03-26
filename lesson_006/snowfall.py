# -*- coding: utf-8 -*-

import simple_draw as sd


sd.resolution = (600, 800)


# snow_N  # Количество снежинок
list_snow_coord_x = []  # Список текущих координат (x) снежинок
list_snow_coord_y = []  # Список текущих координат (y) снежинок
list_snow_length = []  # Список текущих размеров снежинок


def create_snow(N):
    """
        Создать N снежинок
    """
    # Создание списка текущих координат (x) снежинок
    global snow_N  # Глобальная переменная - кол-во снежинок
    snow_N = N
    for i in range(snow_N):
        x = sd.random_number(b=800)
        list_snow_coord_x.append(x)

    # Создание списка текущих координат (y) снежинок
    for i in range(snow_N):
        y = sd.random_number(a=200, b=400)
        list_snow_coord_y.append(y)

    # Создание списка размеров снежинок
    for i in range(snow_N):
        length = sd.random_number(a=10, b=40)
        list_snow_length.append(length)


def draw_snow_color(color=sd.COLOR_WHITE):
    """
        Отрисовать N снежинок (с координатами list_snow_coord_x, list_snow_coord_y, размерами list_snow_length)
        цветом color
    """
    for i in range(snow_N):
        point = sd.get_point(list_snow_coord_x[i], list_snow_coord_y[i])
        length = list_snow_length[i]
        sd.snowflake(center=point, length=length, color=color)


def move_one_step():
    """
        Сдвинуть N снежинок (с координатами list_snow_coord, размерами list_snow_length) на один шаг
    """
    for i in range(snow_N):
        list_snow_coord_x[i] += sd.random_number(a=-10, b=10)
        list_snow_coord_y[i] -= sd.random_number(a=0, b=10)


def numbers_snow_down():
    """
        Вернуть список номеров снежинок, которые вышли за границу экрана
        из N снежинок (с координатами list_snow_coord, размерами list_snow_length)
    """
    list_snow_down = []  # Список номеров снежинок, которые вышли за границу экрана
    for i in range(snow_N):
        if list_snow_coord_y[i] <= -list_snow_length[i]:
            list_snow_down.append(i)
    return list_snow_down


def delete_snow_down(list_snow_down):
    """
        Удалить снежинки из списка номеров снежинок, которые вышли за границу экрана
        из N снежинок (с координатами list_snow_coord, размерами list_snow_length)
    """
    for i in range(len(list_snow_down)):
        list_snow_coord_x[list_snow_down[i]] = 0
        list_snow_coord_y[list_snow_down[i]] = 0
        list_snow_length[list_snow_down[i]] = 0


def create_snow_down(list_snow_down):
    """
        Создать новые снежинки взамен удаленных из списка номеров снежинок,
         которые вышли за границу экрана
    """
    # Создание списка текущих координат и размеров снежинок
    for i in range(len(list_snow_down)):
        x = sd.random_number(b=800)
        list_snow_coord_x[list_snow_down[i]] = x
        y = sd.random_number(a=200, b=400)
        list_snow_coord_y[list_snow_down[i]] = y

    # Создание списка размеров снежинок
    for i in range(len(list_snow_down)):
        length = sd.random_number(a=10, b=40)
        list_snow_length[list_snow_down[i]] = length
