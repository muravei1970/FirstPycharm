# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):  # Въехать в дом
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat):  # Подобрать кота
        cat.house = self.house
        cprint('{} подобрал кота {}'.format(self.name, cat.name), color='cyan')

    def buy_food_cat(self):  # Купить коту еды
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.work()

    def clean_house(self):  # Уборка в доме
        cprint('{} делал уборку в доме'.format(self.name), color='magenta')
        self.house.dirt -= 100
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)  # Кубик со случайными числами от 1 до 6
        if self.house.cat_food < 10:
            self.buy_food_cat()
        elif self.fullness < 30:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirt > 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0  # Грязь

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды для кота осталось {}, грязи набралось {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50  # Сытость
        self.house = None

    def __str__(self):
        return 'Я - кот {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет кошачьего корма'.format(self.name), color='red')

    def sleep(self):
        cprint('Кот {} спал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def tear_up_wallpaper(self):  # Кот дерет обои
        cprint('Кот {} драл обои целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('Кот{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)  # Кубик со случайными числами от 1 до 6
        if self.fullness < 20:
            self.eat()
        elif dice == 1 | 2:
            self.sleep()
        else:
            self.tear_up_wallpaper()

bivis = Man(name='Бивис')
my_sweet_home = House()
murzik = Cat(name='Мурзик')


bivis.go_to_the_house(house=my_sweet_home)
bivis.pick_up_cat(murzik)


for day in range(1, 366):
    print('================ день {} =================='.format(day))
    bivis.act()
    murzik.act()
    print('--- в конце дня ---')
    print(bivis)
    print(murzik)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
