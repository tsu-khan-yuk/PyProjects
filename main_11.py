#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 21.05.2020
#  -> task 1: Интегрируйте Battle в свою игру:
# 		+- обеспечьте совместимость с вашими юнитами
# 		+- создайте обьекты юнитов, создайте обьект битвы, проведите битву
#  -> *task 2: Доработайте механику сражения и проверки состояния атакуемого юнита
######################################################################################################################
from random import shuffle
from PyProjects.Modules.Mage import Mage


class Battle:
	unit1 = None
	unit2 = None
	_ind = None
	# todo: check struct for power up, can be used 'Item'
	_power_up = {
		"Mage": {
			"defence": 50,
			"dmg": 20
		},
		"Knight": {
			"defence": 100,
			"dmg": 60
		}
	}
	
	# check_type(True, Unit, Unit)
	def __init__(self, unit1, unit2):
		self.unit1 = unit1
		self.unit2 = unit2
		self._ind = 0
	
	# check_type(True, str, str)
	def set_mods_into_battle(self, location=None, day_part=None):
		pass
	
	def _deploy_mods_into_unit(self, unit):
		return unit
	
	@staticmethod
	def _first_attack():
		return shuffle(0, 1)
	
	def _index(self):
		while True:
			self._ind = 1 if self._ind is 1 else 0
			yield self._ind
	
	def battle(self):
		# todo: solve problem with index in 'unit' list
		unit = [self._deploy_mods_into_unit(self.unit1), self._deploy_mods_into_unit(self.unit2)]
		count = self._index()
		while True:
			# todo: refresh methods according to raises in 'Unit'
			val = next(count)
			self.unit[val].attack(self.unit2)


mage1 = Mage("Vasya")
mage2 = Mage("Petya")
bat = Battle(mage1, mage2)
