# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (600, 800)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
#------------------------------------------------------------------------------------------------------------------

# sd.resolution = (800, 400)

# Создание списка текущих координат снежинок

# list_snow_current = []
# for i in range(N):
#     x = sd.random_number(b=800)
#     y = sd.random_number(a=200, b=400)
#     list_snow_current.append([x, y])
#
#
# # Создание списка размеров снежинок
# list_snow_length = []
# for i in range(N):
#     x = sd.random_number(a=10, b=40)
#     list_snow_length.append(x)
#
#
# # Функция отрисовки N снежинок
# def snow_n(list_coord_n, list_length_n, color=sd.COLOR_WHITE):
#     for i in range(N):
#         tuple_temp = (list_coord_n[i][0], list_coord_n[i][1])
#         point = sd.get_point(tuple_temp[0], tuple_temp[1])
#         temp_length = list_length_n[i]
#         sd.snowflake(center=point, length=temp_length, color=color)
#
#
# snow_n(list_coord_n=list_snow_current, list_length_n=list_snow_length) # Первая отрисовка 20-ти снежинок (вне цикла)
# while True:
#     sd.start_drawing()
#     # Затереть предыдущую отрисовку
#     snow_n(list_coord_n=list_snow_current, list_length_n=list_snow_length, color=sd.background_color)
#
#     for i in range(N): # Цикл проверки текущего нахождения снежинок
#         # Если снежинка не упала  - изменить ее координаты (продолжить падение)
#         if list_snow_current[i][1] > list_snow_length[i]:
#             list_snow_current[i][1] -= sd.random_number(a=0, b=10)
#             list_snow_current[i][0] += sd.random_number(a=-10, b=10)
#
#     # Очередная отрисовка 20-ти снежинок
#     snow_n(list_coord_n=list_snow_current, list_length_n=list_snow_length)
#     sd.finish_drawing()
#     sd.sleep(0.1)
#
#     if sd.user_want_exit():
#         break
#
# sd.pause()
#---------------------------------------------------------------------------------------------------------------

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку

#-------------------------------------------------------------------------------------------------------

sd.resolution = (800, 400)

# Создание списка текущих координат снежинок

list_snow_current = []
for i in range(N):
    x = sd.random_number(b=800)
    y = sd.random_number(a=200, b=400)
    list_snow_current.append([x, y])

# Создание списка размеров снежинок
list_snow_length = []
for i in range(N):
    x = sd.random_number(a=10, b=40)
    list_snow_length.append(x)

# Список упавших снежинок
list_snow_down = []


# Функция отрисовки n снежинок
def snow_n(list_coord_n, list_length_n, color=sd.COLOR_WHITE):
    for i in range(N):
        tuple_temp = (list_coord_n[i][0], list_coord_n[i][1])
        point = sd.get_point(tuple_temp[0], tuple_temp[1])
        temp_length = list_length_n[i]
        sd.snowflake(center=point, length=temp_length, color=color)


snow_n(list_coord_n=list_snow_current, list_length_n=list_snow_length)  # Первая отрисовка 20-ти снежинок (вне цикла)
while True:
    sd.start_drawing()
    # Затереть предыдущую отрисовку
    snow_n(list_coord_n=list_snow_current, list_length_n=list_snow_length, color=sd.background_color)

    for i in range(N):  # Цикл проверки текущего нахождения снежинок
        if list_snow_current[i][1] < list_snow_length[i]:  # Если снежинка упала
            if i in list_snow_down:  # Если она уже в списке упавших
                continue  # не проверять ее дальше
            else:  # Если она только что упала
                list_snow_down.append(i)  # добавить ее в список упавших снежинок

                # Создать новую снежинку взамен упавшей
                x = sd.random_number(b=800)
                y = sd.random_number(a=200, b=400)
                list_snow_current.append([x, y])
                x = sd.random_number(a=10, b=40)
                list_snow_length.append(x)
                N += 1

        else:  # Если снежинка не упала - изменить ее координаты (продолжить падение)
            list_snow_current[i][1] -= sd.random_number(a=0, b=10)
            list_snow_current[i][0] += sd.random_number(a=-10, b=10)

    # Очередная отрисовка 20-ти снежинок
    snow_n(list_coord_n=list_snow_current, list_length_n=list_snow_length)
    sd.finish_drawing()
    sd.sleep(0.1)

    if sd.user_want_exit():
        break

sd.pause()
#------------------------------------------------------------------------------------------------------------
# Результат решения см https://youtu.be/XBx0JtxHiLg


