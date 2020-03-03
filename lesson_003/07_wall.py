# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (800, 400)
size_brick = (100, 50)
left_bottom_y = -50
right_top_y = 0
wall_width = sd.resolution[0] // size_brick[0] + 1 # Ширина стены
wall_height = sd.resolution[1] // size_brick[1]  # Высота стены
row_counter = 0  # Счетчик рядов кирпичей
for _ in range(wall_height): # Переход на очередной ряд кирпичей
    row_counter += 1
    if row_counter % 2:  # Начать ряд с половинки кирпича
        left_bottom_x = -50
        right_top_x = 50
    else:  # Начать ряд с целого кирпича
        left_bottom_x = 0
        right_top_x = 100
    left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
    right_top = sd.get_point(right_top_x, right_top_y)
    left_bottom_y += 50
    right_top_y += 50
    for _ in range(wall_width): # Постройка ряда кирпичей
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top = sd.get_point(right_top_x, right_top_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2, color=sd.COLOR_DARK_ORANGE)
        left_bottom_x += 100
        right_top_x += 100


sd.pause()
