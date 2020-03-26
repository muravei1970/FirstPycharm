# -*- coding: utf-8 -*-
from random import randint


def make_number():
    """
        Функция генерации 4-значного числа
    """
    number_list = []
    random_number = randint(1, 9)  # Генерация первой цифры - от 1 до 9
    number_list.append(str(random_number))
    while len(number_list) < 4:  # Пока не сгенерировано 4 цифры
        random_number = randint(0, 9)  # Генерация второй, третьей и четвертой цифр - от 0 до 9
        for j in range(len(number_list)):  # Цикл исключения повторяемых цифр из числа
            label_repeat = False  # Метка повтора
            if str(random_number) == number_list[j]:
                label = True
                break
        if label:
            continue
        number_list.append(str(random_number))
    return number_list


def check_number(import_check_number, import_maked_number):
    """
        Функция проверки
        import_check_number - Число, введенное пользователем
        import_maked_number - Загаданное число
    """
    bools = 0  # Счетчик быков
    cows = 0  # Счетчик коров
    for i in range(4):  # С каждой цифрой загаданного числа
        for j in range(4):  # Сравнитоь каждую цифру числа, введенного пользователем
            if import_check_number[i] == import_maked_number[j] and i == j:  # Если это бык
                bools += 1
                break
            if import_check_number[i] == import_maked_number[j] and i != j:  # Если это корова
                cows += 1
                break
    coincidence_dict = {"bools": bools, "cows": cows}  # Результат сравнения
    return coincidence_dict


