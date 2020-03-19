# -*- coding: utf-8 -*-


import simple_draw as sd

sd.resolution = (800, 400)

# Создание списка начальных координат снежинок
N = 20
list_snow = []
y = 500

for i in range(N):
    x = sd.random_number(b=800)
    list_snow.append([x, y])


# Процесс падения снежинок

while True:
    sd.clear_screen()
    for i in range(N):
        for i in range(N):
            tuple_temp = (list_snow[i][0], list_snow[i][1])
            point = sd.get_point(tuple_temp[0], tuple_temp[1])
            sd.snowflake(center=point, length=50)
    if list_snow[i][1] < 50:
        list_snow[i].append(True)
        if all(list_snow[2]):
            break
        continue
    else:
        list_snow[i][1] -= 10
        list_snow[i][0] += 10

    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()
