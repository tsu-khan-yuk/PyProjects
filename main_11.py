#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 22.05.2020
#  -> task 1: Интегрируйте Battle в свою игру:
# 		+- обеспечьте совместимость с вашими юнитами
# 		+- создайте обьекты юнитов, создайте обьект битвы, проведите битву
#  -> *task 2: Доработайте механику сражения и проверки состояния атакуемого юнита
######################################################################################################################
from random import sample
from abc import ABC, abstractmethod
from random import randint


def check_type(*types):
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

    def __eq__(self, other):
        """Метод для сравнения героев"""
        if not isinstance(other, Unit):
            return False
        if other._name == self._name and other._health == self._health and \
                other._dmg == self._dmg and other._defence and self._defence:
            return True
        else:
            return False

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


class Battle:
    unit1 = None
    unit2 = None
    _loc = None
    _day_part = None
    _ind = None
    _power_up = {
        "location": {
            "forest": {
                Mage: {
                    "defence": 50,
                    "dmg": 60
                }
            },
            "city": {
                Mage: {
                    "defence": 80,
                    "dmg": 40
                }
            },
            "cornfield": {
                Knight: {
                    "defence": 40,
                    "dmg": 70
                }
            }
        },
        "day_part": {
            "morning": {
                Knight: {
                    "defence": 60,
                    "dmg": 50
                }
            },
            "noon": {
                Mage: {
                    "defence": 40,
                    "dmg": 70
                }
            },
            "midday": {
                Knight: {
                    "defence": 70,
                    "dmg": 50
                }
            }
        }
    }

    @check_type(True, Unit, Unit)
    def __init__(self, unit1, unit2):
        if unit1 == unit2:
            raise Exception("Self harm isn`t ok!!!")
        self.unit1 = unit1
        self.unit2 = unit2
        self._ind = 0

    def set_mods_into_battle(self, location=None, day_part=None):
        """Метод, с помощью которой можно установки параметры боя"""
        if not (isinstance(location, str) and isinstance(day_part, str)):
            raise TypeError
        # can renew the _power_up dict for memory optimization
        if location is not None and location in self._power_up["location"].keys():
            self._loc = self._power_up["location"][location]
        if day_part is not None and day_part in self._power_up["day_part"].keys():
            self._day_part = self._power_up["day_part"][day_part]

    def _deploy_mods_into_unit(self, unit):
        """Метод для усиления героев"""
        unit_type = type(unit)
        if self._loc is not None and unit_type in self._loc.keys():
            unit._defence += self._loc[unit_type]["defence"]
            unit._dmg += self._loc[unit_type]["dmg"]
        if self._day_part is not None and unit_type in self._day_part.keys():
            unit._defence += self._day_part[unit_type]["defence"]
            unit._dmg += self._day_part[unit_type]["dmg"]
        return unit

    def _first_attack(self):
        """Метод для решения, кто сделает первый удар"""
        unit1 = self._deploy_mods_into_unit(self.unit1)
        unit2 = self._deploy_mods_into_unit(self.unit2)
        return sample([unit1, unit2], 2)

    def _index(self):
        """Генератор который возвращает 0 и 1 поочередно"""
        while True:
            self._ind = 1 if self._ind is 0 else 0
            yield self._ind

    def battle(self):
        """Метод для проведения боя"""
        unit = self._first_attack()
        count = self._index()

        while True:
            unit[next(count)].attack(unit[next(count)])


if __name__ == "__main__":
    mage = Mage("Vasya")
    print(mage)
    knight = Knight("Petya")
    print(knight)

    bat = Battle(mage, knight)
    bat.set_mods_into_battle("forest", "morning")

    bat.battle()
