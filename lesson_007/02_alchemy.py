# -*- coding: utf-8 -*-


# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self, name='water'):
        self.name = name

    def __add__(self, other):
        if other.name == 'air':
            return Storm()
        elif other.name == 'fire':
            return Steam()
        elif other.name == 'earth':
            return Dirt()
        else:
            return None

    def __str__(self):
        return 'Вода'


class Air:

    def __init__(self, name='air'):
        self.name = name

    def __add__(self, other):
        if other.name == 'water':
            return Storm()
        elif other.name == 'fire':
            return Thunder()
        elif other.name == 'earth':
            return Dust()
        else:
            return None

    def __str__(self):
        return 'Воздух'


class Fire:

    def __init__(self, name='fire'):
        self.name = name

    def __add__(self, other):
        if other.name == 'water':
            return Steam()
        elif other.name == 'air':
            return Thunder()
        elif other.name == 'earth':
            return Lava()
        else:
            return None

    def __str__(self):
        return 'Огонь'


class Earth:

    def __init__(self, name='earth'):
        self.name = name

    def __str__(self):
        return 'Земля'


class Storm:
    def __init__(self, name='storm'):
        self.name = name

    def __str__(self):
        return 'Шторм'


class Steam:
    def __init__(self, name='steam'):
        self.name = name

    def __str__(self):
        return 'Пар'


class Dirt:
    def __init__(self, name='dirt'):
        self.name = name

    def __str__(self):
        return 'Грязь'


class Thunder:
    def __init__(self, name='thunder'):
        self.name = name

    def __str__(self):
        return 'Молния'


class Dust:
    def __init__(self, name='dust'):
        self.name = name

    def __str__(self):
        return 'Пыль'


class Lava:
    def __init__(self, name='lava'):
        self.name = name

    def __str__(self):
        return 'Лава'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
