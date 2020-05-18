from PyProjects.Modules.Item import Item
from PyProjects.Modules.Checker import check_type


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
