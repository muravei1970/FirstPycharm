# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (800, 470)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# start_x = 50
# stop_x = 350
# for i in range(7):
#     start_point = sd.get_point(start_x, 50)
#     stop_point = sd.get_point(stop_x, 450)
#     sd.line(start_point, stop_point, width=4, color=rainbow_colors[i])
#     start_x += 5
#     stop_x += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(510, -310)
radius = 620
for i in range(7):
    sd.circle(center_position=point, radius=radius, width=4, color=rainbow_colors[i])
    radius += 5

sd.pause()
