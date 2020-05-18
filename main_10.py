#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 19.05.2020
#  -> task 1: Добавьте в класс Unit атрибут, отвечающий за шанс (в процентах) для юнита нанести двойной урон во
#  	время атаки. Измените метод вычисления урона так, чтобы данная величина учитывалась при выполнении атаки.
#  	Можно использовать итератор или генератор, который будет возвращать результат обработки шанса (например шанс 0.5
#  	или 50% и определяет, сработал шанс или нет)
#  -> task 2: Сделайте класс Stuff, который будет базовым для всех вещей, которые смогут использовать юниты.
#  	В классе должен быть атрибут(ы), определяющий(е) классы юнитов, которые могут им воспользоваться;
#  	атрибуты, отвечающие за модификацию параметров юнита, который пользуется этим Stuff-ом
#  	(атрибуты для health, damage, defence)
#  -> *task 3: Добавьте в класс Unit атрибут, отвечающий за шанс (в процентах) для юнита уклонится от атаки
#  	противника и метод получения результата (уклонился от атаки или нет) во время атаки. Измените метод вычисления
# 	учитывалась при выполнении атаки (при уклонении от атаки урон не наносится).
#  	Также можно использовать итератор\генератор
######################################################################################################################
from abc import ABC, abstractmethod
from random import randint


def check_type(*types):
    """Декоратор с параметрами, принимает типы данных в такой же последовательности
        как и параметры метода или функции"""

    # *Приметка: так как в методах класса первый параметр это "self", то вместо него
    #   в параметрах декоратора надо поставить True. Тогда этот параметр проверятся не будет
    def decor(func):
        def wrapper(*args):
            if types[0] is True:
                types_list = list(types[1:])
                args_list = list(args[1:])
            else:
                types_list = list(types[:])
                args_list = list(args[:])
            if len(types_list) != len(args_list):
                raise TypeError("Check decor parameters")
            mas = dict(map(lambda *x: x, types_list, args_list))
            for arg in mas.items():
                if not isinstance(arg[1], arg[0]):
                    raise TypeError
            return func(*args)

        return wrapper

    return decor


class Item:
    """Класс отвечает за вещь(усилитель), который можно будет
    сложить в обьект Pocket"""
    _name = None
    _base = None
    _attachment = None
    _check_att = {"Unit", "Mage", "Knight"}

    def __init__(self, name="unknown", attachment="Unit", defence=0, dmg=0):
        """Создает предмет, которй может повысить домаг и/или защиту"""
        if isinstance(name, str) and isinstance(defence, (int, float)) and isinstance(dmg, (int, float)) \
                and isinstance(attachment, str) and attachment in self._check_att:
            self._attachment = attachment
            self._name = name
            self._base = dict()
            self._base.update({
                "defence": int(defence),
                "dmg": int(dmg)
            })

    @property
    def name(self) -> str:
        """Возвращет имя предмета, что бы потом можно было его использовать как ключ"""
        return self._name

    @property
    def attach(self) -> str:
        """Метод, который возвращает пренадлежность предмета классу"""
        return self._attachment

    @property
    def base(self) -> dict:
        """Возвращает словарь из характеристик предмета"""
        return self._base

    def __str__(self):
        string = "+----------------------+\n"
        string += f"| name: {self._name}\n"
        string += f"| attachment: {self._attachment}\n"
        string += f"| defence: {self._base['defence']}\n"
        string += f"| dmg: {self._base['dmg']}\n"
        string += "+----------------------+\n"
        return string


class Pocket:
    """Класс строится из обьектов Item для удобства использования"""
    _loot = None

    def __init__(self):
        self._loot = dict()

    def __iter__(self):
        self.keys = self._loot.keys()
        self.dict_index = -1
        return iter(self._loot.values())

    def __next__(self):
        if len(self.keys) <= self.dict_index:
            raise StopIteration
        self.dict_index += 1
        return 0

    def keys(self):
        return iter(self._loot.keys())

    def values(self):
        return iter(self._loot.values())

    def items(self):
        return iter(self._loot.items())

    @check_type(True, Item)
    def push_item(self, item) -> None:
        """Добавляет предмет в карман"""
        self._loot.update({item.name: item.base})

    @check_type(True, str)
    def param_sum(self, param: str) -> int:
        """Вычесляет общюю суму по параметру(defence/dmg) в кармане"""
        if param in ("defence", "dmg"):
            res = 0
            for i in self._loot:
                res += self._loot[i][param]
            return res

    def __str__(self):
        string = ""
        for i in self._loot:
            string += f"{i}: {self._loot[i]}\n"
        return string


class Unit(ABC):
    _name = None
    _health = 100
    _dmg = 1
    _defence = 10
    _amplifiers = None

    @abstractmethod
    def attack(self, enemy) -> None:
        pass

    @abstractmethod
    def _get_dmg(self) -> int:
        pass

    @abstractmethod
    def _get_defence(self) -> int:
        pass

    @staticmethod
    def luck_generator() -> int:
        """Генератор, который возвращает процент вероятности от 0 до 100"""
        while True:
            yield randint(0, 100)

    @staticmethod
    @check_type(int)
    def power_up(dmg: int) -> int:
        """Функция, которая возвращает либо 0(если генератор вернул <75),
            или полное значение(если генератор вернул >75)"""
        func = Unit.luck_generator()
        if next(func) > 75:
            return 2 * dmg
        else:
            return dmg

    def __setattr__(self, key, value):
        if key == "_health":
            if not (self._health - value) < 0 and value > 0:
                self.__dict__[key] = value
            else:
                raise Exception(f"{self._name} is dead(")
        elif key == "_dmg" and value > 0:
            self.__dict__[key] = value
        elif key == "_defence" and value >= 0:
            self.__dict__[key] = value
        elif key == "_name" and isinstance(value, str):
            self.__dict__[key] = value
        elif key == "_amplifiers" and type(value) == Pocket:
            self.__dict__[key] = Pocket()


class Mage(Unit):

    @check_type(True, str)
    def __init__(self, name):
        self._amplifiers = Pocket()
        self._name = name

    @check_type(True, Item)
    def take_item(self, item) -> None:
        """Подобрать предмет и положить в сумку"""
        if item.attach in {"Mage", "Unit"}:
            self._amplifiers.push_item(item)
            self._defence = self._get_defence()
            self._dmg = self._get_dmg()
        else:
            raise Exception(f"{self._name} can`t take {item.name}")

    def _get_dmg(self) -> int:
        return self._dmg + self._amplifiers.param_sum("dmg")

    def _get_defence(self) -> int:
        return self._defence + self._amplifiers.param_sum("defence")

    @check_type(True, Unit)
    def attack(self, enemy) -> None:
        real_vitality = enemy._defence + enemy._health
        real_vitality -= Unit.power_up(self._dmg)

        if real_vitality < enemy._health:
            enemy._health = real_vitality
            enemy._defence = 0
        else:
            enemy._defence = real_vitality - enemy._health

    def __str__(self):
        string = "+------------------+\n"
        string += f"| name: {self._name}(Mage)\n"
        string += f"| health: {self._health}\n"
        string += f"| defence: {self._defence} (loot: {self._amplifiers.param_sum('defence')})\n"
        string += f"| dmg: {self._dmg} (loot: {self._amplifiers.param_sum('dmg')})\n"
        string += "+------------------+"
        return string


class Knight(Unit):
    """Напишите класс Knight. Реализуйте расчет значения урона
    для атаки и значения заблокированного урона для защиты.
    Добавьте в атаку рыцаря игнорирование половины защиты врага."""

    @check_type(True, str)
    def __init__(self, name):
        self._amplifiers = Pocket()
        self._name = name

    @check_type(True, Unit)
    def attack(self, enemy) -> None:
        half_enemy_defence = enemy._defence // 2
        real_dmg = Unit.power_up(self._dmg)
        if real_dmg > half_enemy_defence:
            enemy._health -= real_dmg - half_enemy_defence
            enemy._defence = half_enemy_defence
        else:
            enemy._defence -= real_dmg

    @check_type(True, Item)
    def take_item(self, item) -> None:
        """Подобрать предмет и положить в сумку"""
        if item.attach in {"Knight", "Unit"}:
            self._amplifiers.push_item(item)
            self._defence = self._get_defence()
            self._dmg = self._get_dmg()
        else:
            raise Exception(f"{self._name} can`t take {item.name}")

    def _get_defence(self) -> int:
        return self._defence + self._amplifiers.param_sum("defence")

    def _get_dmg(self) -> int:
        return self._dmg + self._amplifiers.param_sum("dmg")

    def __str__(self):
        string = "+------------------+\n"
        string += f"| name: {self._name}(Knight)\n"
        string += f"| health: {self._health}\n"
        string += f"| defence: {self._defence} (loot: {self._amplifiers.param_sum('defence')})\n"
        string += f"| dmg: {self._dmg} (loot: {self._amplifiers.param_sum('dmg')})\n"
        string += "+------------------+"
        return string


if __name__ == "__main__":

    mag = Mage("Python OOP")
    knight = Knight("Ivan")

    print(mag)
    print(knight)

    print("~" * 30 + "{After taking items}" + "~" * 30)
    it1 = Item("Shield of knowledge", attachment="Knight", defence=50)
    it2 = Item("Stick of complexity", attachment="Mage", dmg=60)
    print(it1)
    print(it2)
    knight.take_item(it1)
    mag.take_item(it2)

    print(mag)
    print(knight)

    print("~" * 30 + "{After attack}" + "~" * 30)

    mag.attack(knight)
    knight.attack(mag)

    print(mag)
    print(knight)
