from PyProjects.Modules.Unit import Unit
from PyProjects.Modules.Pocket import Pocket
from PyProjects.Modules.Item import Item


class Mage(Unit):

    def __init__(self, name):
        if isinstance(name, str):
            self._amplifiers = Pocket()
            self._name = name

    def take_item(self, item):
        """Подобрать предмет и положить в сумку"""
        if isinstance(item, Item):
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

    def attack(self, enemy) -> None:
        if not isinstance(enemy, Unit):
            raise Exception(f"{self._name} не может атаковать {type(enemy)}(")
        real_vitality = enemy._defence + enemy._health
        real_vitality -= self._dmg

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

