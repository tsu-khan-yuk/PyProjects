#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 21.05.2020
#  -> task 1: Интегрируйте Battle в свою игру:
# 		+- обеспечьте совместимость с вашими юнитами
# 		+- создайте обьекты юнитов, создайте обьект битвы, проведите битву
#  -> *task 2: Доработайте механику сражения и проверки состояния атакуемого юнита
######################################################################################################################
from random import shuffle
from PyProjects.Modules.Mage import Unit, Mage, check_type


class Battle:
    unit1 = None
    unit2 = None
    _loc = None
    _day_part = None
    _ind = None
    # todo: check struct for power up, can be used 'Item'
    _power_up = {
        "location": {
            "forest": {
                Mage: {
                    "defence": 50,
                    "dmg": 60
                }
            },
            "city": {
                "Mage": {
                    "defence": 80,
                    "dmg": 40
                }
            },
            "cornfield": {
                "Knight": {
                    "defence": 40,
                    "dmg": 70
                }
            }
        },
        "day_part": {
            "morning": {
                "Knight": {
                    "defence": 60,
                    "dmg": 50
                }
            },
            "noon": {
                "Mage": {
                    "defence": 40,
                    "dmg": 70
                }
            },
            "midday": {
                "Knight": {
                    "defence": 70,
                    "dmg": 50
                }
            }
        }
    }

    @check_type(True, Unit, Unit)
    def __init__(self, unit1, unit2):
        self.unit1 = unit1
        self.unit2 = unit2
        self._ind = 0

    @check_type(True, str, str)
    def set_mods_into_battle(self, location=None, day_part=None):
        self._loc = location
        self._day_part = day_part

    def _deploy_mods_into_unit(self, unit):
        # if self._loc is not None:
        # 	defence_up = self._power_up[self._loc][]
        return unit

    def _first_attack(self):
        unit1 = self._deploy_mods_into_unit(self.unit1)
        unit2 = self._deploy_mods_into_unit(self.unit2)
        return shuffle(unit1, unit2)

    def _index(self):
        while True:
            self._ind = 1 if self._ind is 0 else 0
            yield self._ind

    def battle(self):
        unit = self._first_attack()
        count = self._index()

        while True:
            unit[next(count)].attack(unit[next(count)])


mage1 = Mage("Vasya")
mage2 = Mage("Petya")
bat = Battle(mage1, mage2)

bat.battle()
