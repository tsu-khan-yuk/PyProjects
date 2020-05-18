from PyProjects.Modules.Unit import Unit
from PyProjects.Modules.Checker import check_type
from PyProjects.Modules.Pocket import Pocket
from PyProjects.Modules.Item import Item


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
