from PyProjects.Modules.Item import Item


class Pocket:
    """Класс строится из обьектов Item для удобства использования"""
    # todo 1: сделать чтение из готового словаря
    # todo 2: сделать его итерируемым
    # todo 3: сдлеать различия для мага и для рыцаря
    _loot = None

    def __init__(self):
        self._loot = dict()

    def push_item(self, item) -> None:
        """Добавляет предмет в карман"""
        if isinstance(item, Item):
            self._loot.update({item.name: item.base})

    def param_sum(self, param: str) -> int:
        """Вычесляет общюю суму по параметру(defence/dmg) в кармане"""
        if isinstance(param, str) and param in ("defence", "dmg"):
            res = 0
            for i in self._loot:
                res += self._loot[i][param]
            return res

    def __str__(self):
        string = ""
        for i in self._loot:
            string += f"{i}: {self._loot[i]}\n"
        return string
