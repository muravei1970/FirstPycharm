# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sn


sd.resolution = (800, 400)
N = 20  # Количество снежинок


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#  создать_снежинки(count)
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
sn.create_snow(N)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    sd.start_drawing()
    sn.draw_snow_color(color=sd.background_color)
    #  сдвинуть_снежинки()
    sn.move_one_step()
    #  нарисовать_снежинки_цветом(color)
    sn.draw_snow_color()
    #  если есть номера_достигших_низа_экрана() то
    down = sn.numbers_snow_down()
    if down:
        #  удалить_снежинки(номера)
        sn.delete_snow_down(down)
        #  создать_снежинки(count)
        sn.create_snow_down(down)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
