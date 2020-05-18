from PyProjects.Modules.Unit import Unit
from PyProjects.Modules.Checker import check_type
from PyProjects.Modules.Pocket import Pocket
from PyProjects.Modules.Item import Item


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

