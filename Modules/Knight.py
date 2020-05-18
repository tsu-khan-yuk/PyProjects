from PyProjects.Modules.Unit import Unit, check_type
from PyProjects.Modules.Pocket import Pocket
from PyProjects.Modules.Item import Item


class Knight(Unit):
    """Напишите класс Knight. Реализуйте расчет значения урона
    для атаки и значения заблокированного урона для защиты.
    Добавьте в атаку рыцаря игнорирование половины защиты врага."""

    def __init__(self, name):
        if isinstance(name, str):
            self._amplifiers = Pocket()
            self._name = name

    @check_type(True, Unit)
    def attack(self, enemy) -> None:
        # # Если правильно понял, то игнорируеться половина защиты врага.
        # # 	Если домаг больше половины защиты, то цепляет здоровье, но не защиту.
        # # 	Если домаг меньше половины защиты, то цепляет только защиту
        # if not isinstance(enemy, Unit):
        #     raise Exception(f"{self._name} не может атаковать {type(enemy)}(")
        half_enemy_defence = enemy._defence // 2
        # todo: add "power_up" instead self._dmg
        if self._dmg > half_enemy_defence:
            enemy._health -= self._dmg - half_enemy_defence
            enemy._defence = half_enemy_defence
        else:
            enemy._defence -= self._dmg

    @check_type()
    def take_item(self, item) -> None:
        """Подобрать предмет и положить в сумку"""
        if isinstance(item, Item):
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
