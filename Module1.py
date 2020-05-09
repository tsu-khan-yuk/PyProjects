from abc import ABC, abstractmethod


class Unit(ABC):
    """Допишите класс Unit: добавьте проверку на здоровье
        таким образом, чтобы здоровье нельзя было установить < 0"""
    _name = None
    _health = 100
    _dmg = 1
    _defence = 10

    @abstractmethod
    def attack(self, enemy):
        pass

    @abstractmethod
    def _get_dmg(self):
        pass

    @abstractmethod
    def _get_defence(self):
        pass

    def __setattr__(self, key, value):
        # todo: проверить наличие видеолекции и проверить то ли это!!!
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
        # modify self._dmg here
        return self._dmg

    def _get_defence(self):
        # modify self._defence here
        return self._defence

    def set_name(self, val):
        print(self._name)
        self._name = val
        print(self._name)

    def attack(self, enemy):
        if not isinstance(enemy, Unit):
            raise Exception  # todo: do informative exception !

        _dmg = self._get_dmg()
        _defence = enemy._get_defence()

        enemy._health -= _defence - _dmg


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




