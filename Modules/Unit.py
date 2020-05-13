from abc import ABC, abstractmethod
from PyProjects.Modules.Pocket import Pocket


class Unit(ABC):
    _name = None
    _health = 100
    _dmg = 1
    _defence = 10
    _amplifiers = None

    @abstractmethod
    def attack(self, enemy) -> int:
        pass

    @abstractmethod
    def _get_dmg(self) -> int:
        pass

    @abstractmethod
    def _get_defence(self) -> int:
        pass

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
