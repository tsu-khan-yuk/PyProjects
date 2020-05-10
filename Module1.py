from abc import ABC, abstractmethod


class Item:
    """Класс отвечает за вещь(усилитель), который можно будет
        сложить в обьект Pocket"""
    _name = None
    _item_base = dict()

    def __init__(self, name="unknown", health=0.0, defence=0.0, dmg=0.0):
        if isinstance(name, str) and isinstance(health, (int, float)) and \
                isinstance(defence, (int, float)) and isinstance(dmg, (int, float)):
            self._name = name
            self._item_base.update({
                "health": float(health),
                "defence": float(defence),
                "dmg": float(dmg)
            })

    @property
    def name(self) -> str:
        return self._name

    @property
    def base(self) -> dict:
        return self._item_base


class Pocket:
    """Класс строится из обьектов Item для удобства использования"""
    # todo: сделать чтение из готового словаря
    # todo: делать ли обновлениве по параметрам, что находяться в словаре?
    _boost_dictionary = dict()

    def push_item(self, item) -> None:
        if isinstance(item, Item):
            self._boost_dictionary.update({item.name: item.base})

    def param_sum(self, param: str):
        if isinstance(param, str) and param in ("health", "defence", "dmg"):
            res = 0.0
            for i in self._boost_dictionary:
                res += i[param]
            return res

    def __str__(self):
        string = ""
        for i in self._boost_dictionary:
            string += f"{i}: {self._boost_dictionary[i]}\n"
        return string


class Unit(ABC):
    """Допишите класс Unit: добавьте проверку на здоровье
        таким образом, чтобы здоровье нельзя было установить < 0"""
    _name = None
    _health = 100
    _dmg = 1
    _defence = 10
    _amplifiers = Pocket()

    @abstractmethod
    def attack(self, enemy):
        # todo: нужно посчтать весь дмг в кармане и приплюсовавть к собстевнной силе
        pass

    @abstractmethod
    def _get_dmg(self):
        pass

    @abstractmethod
    def _get_defence(self):
        pass

    def __setattr__(self, key, value):
        # todo: проверить наличие видеолекции и проверить то ли это!!!
        # todo: надо доработать взаимодействие с пользоветелем
        if key == "_health" and (self._health - value) >= 0:
            self.__dict__[key] = value
        elif key == "_dmg" and value > 0:
            self.__dict__[key] = value
        elif key == "_defence" and value >= 0:
            self.__dict__[key] = value
        elif key == "_name" and isinstance(value, str):
            self.__dict__[key] = value


class Mage(Unit):

    def __init__(self, name, dmg, defence):
        self._name = name
        self._dmg = dmg
        self._defence = defence

    def _get_dmg(self):
        # todo: нужно посчитать весь дмг в кармане
        # modify self._dmg here

    def take_item(self, item):
        if isinstance(item, Item):
            self._amplifiers.push_item(item)

    def _get_defence(self):
        # modify self._defence here
        return self._defence

    def set_name(self, val):
        print(self._name)
        self._name = val
        print(self._name)

    def attack(self, enemy):
        if not isinstance(enemy, Unit):
            raise Exception("Undefined type of warrior!")  # todo: do informative exception !

        _dmg = self._get_dmg()
        _defence = enemy._get_defence()

        enemy._health -= _defence - _dmg

    def __str__(self):
        string = "+------------------+\n"
        string += f"| name: {self._name}\n"
        string += f"| healt: {self._health}\n"
        string += f"| defence: {self._defence}\n"
        string += f"| dmg: {self._dmg}\n"
        string += "+------------------+"
        return string


class Knight(Unit):
    """Напишите класс Knight. Реализуйте расчет значения урона
        для атаки и значения заблокированного урона для защиты.
        Добавьте в атаку рыцаря игнорирование половины защиты врага."""

    def __init__(self, name, dmg, defence):
        self._name = name
        self._dmg = dmg
        self._defence = defence

    def attack(self, enemy):
        pass

    def _get_defence(self):
        pass

    def _get_dmg(self):
        pass
