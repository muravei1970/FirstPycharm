# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

for current_good in goods:
    current_good_name = current_good  # Наименование текущего (в цикле) товара
    current_good_code = goods[current_good]  # Код текущего (в цикле) товара
    current_total_quantity = 0  # Общее количество текущего товара
    current_total_price = 0  # Общая стоимость текущего товара

    list_current_good_in_store = store[current_good_code]  # Список текущего товара на складе

    #  Цикл вычисления общего количества текущего товарв на складе
    #  current_type_of_good_in_store - Количество текущего вида одноименного товара (различающегося по цене)

    for current_type_of_good_in_store in list_current_good_in_store:
        current_total_quantity += current_type_of_good_in_store['quantity']

    #  Цикл вычисления общей цены текущего товарв на складе
    #  current_type_of_good_in_store - Цена текущего вида одноименного товара (различающегося по цене)

    for current_type_of_good_in_store in list_current_good_in_store:
        current_total_price += current_type_of_good_in_store['price'] * current_type_of_good_in_store['quantity']
    print(current_good_name + ' - ' + str(current_total_quantity) + " шт, стоимость " + \
          str(current_total_price) + " руб")
