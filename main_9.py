#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 13.05.2020
#  -> task 1: Допишите класс Unit: добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было
#  установить < 0 (например у юнита осталось 5 здоровья а его ударили на 10)
#  -> task 2: Напишите класс Knight. Реализуйте расчет значения урона для атаки и значения заблокированного
#  урона для защиты. Добавьте в атаку рыцаря игнорирование половины защиты врага.
#  -> task 3: Реализуйте всем классам юнитов в атаке проверку состояния здоровья врага (нельзя атаковать врага,
#  у которого здоровье = 0)
#  -> *task 4: Для мага - продумайте механику использования заклинаний. Вероятнее всего заклинание - обьект
#  отдельного класса (ООП всетаки))))
######################################################################################################################
from abc import ABC, abstractmethod


class Item:
	"""Класс отвечает за вещь(усилитель), который можно будет
	сложить в обьект Pocket"""
	_name = None
	_base = None
	
	def __init__(self, name="unknown", defence=0, dmg=0):
		"""Создает предмет, которй может повысить домаг и/или защиту"""
		if isinstance(name, str) and isinstance(defence, (int, float)) and isinstance(dmg, (int, float)):
			self._name = name
			self._base = dict()
			self._base.update({
				"defence": int(defence),
				"dmg": int(dmg)
			})
	
	@property
	def name(self) -> str:
		"""Возвращет имя предмета, что бы потом можно было его использовать как ключ"""
		return self._name
	
	@property
	def base(self) -> dict:
		"""Возвращает словарь из характеристик предмета"""
		return self._base
	
	def __str__(self):
		string = "+----------------------+\n"
		string += f"| name: {self._name}\n"
		string += f"| defence: {self._base['defence']}\n"
		string += f"| dmg: {self._base['dmg']}\n"
		string += "+----------------------+\n"
		return string


class Pocket:
	"""Класс строится из обьектов Item для удобства использования"""
	# todo: сделать чтение из готового словаря
	_loot = None
	
	def __init__(self):
		self._loot = dict()
	
	def push_item(self, item) -> None:
		"""Добавляет предмет в карман"""
		if isinstance(item, Item):
			self._loot.update({ item.name: item.base })
	
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


class Mage(Unit):
	
	def __init__(self, name):
		if isinstance(name, str):
			self._amplifiers = Pocket()
			self._name = name
	
	def take_item(self, item):
		"""Подобрать предмет и положить в сумку"""
		if isinstance(item, Item):
			self._amplifiers.push_item(item)
			self._defence = self._get_defence()
			self._dmg = self._get_dmg()
	
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
		string += f"| name: {self._name}\n"
		string += f"| health: {self._health}\n"
		string += f"| defence: {self._defence} (loot: {self._amplifiers.param_sum('defence')})\n"
		string += f"| dmg: {self._dmg} (loot: {self._amplifiers.param_sum('dmg')})\n"
		string += "+------------------+"
		return string


class Knight(Unit):
	"""Напишите класс Knight. Реализуйте расчет значения урона
	для атаки и значения заблокированного урона для защиты.
	Добавьте в атаку рыцаря игнорирование половины защиты врага."""
	
	def __init__(self, name):
		if isinstance(name, str):
			self._amplifiers = Pocket()
			self._name = name
	
	def attack(self, enemy) -> None:
		# # Если правильно понял, то игнорируеться половина защиты врага.
		# # 	Если домаг больше защиты, то цепляет здоровье, но не защиту.
		# # 	Если домаг меньше защиты, то цепляет только защиту
		if not isinstance(enemy, Unit):
			raise Exception(f"{self._name} не может атаковать {type(enemy)}(")
		half_enemy_defence = enemy._defence // 2
		if self._dmg > half_enemy_defence:
			enemy._health -= self._dmg - half_enemy_defence
			enemy._defence = half_enemy_defence
		else:
			enemy._defence -= self._dmg
	
	def take_item(self, item):
		"""Подобрать предмет и положить в сумку"""
		if isinstance(item, Item):
			self._amplifiers.push_item(item)
			self._defence = self._get_defence()
			self._dmg = self._get_dmg()
	
	def _get_defence(self) -> int:
		return self._defence + self._amplifiers.param_sum("defence")
	
	def _get_dmg(self) -> int:
		return self._dmg + self._amplifiers.param_sum("dmg")
	
	def __str__(self):
		string = "+------------------+\n"
		string += f"| name: {self._name}\n"
		string += f"| health: {self._health}\n"
		string += f"| defence: {self._defence} (loot: {self._amplifiers.param_sum('defence')})\n"
		string += f"| dmg: {self._dmg} (loot: {self._amplifiers.param_sum('dmg')})\n"
		string += "+------------------+"
		return string


if __name__ == "__main__":
	mag = Mage("Python OOP")
	knight = Knight("Ivan")
	
	print(mag)
	print(knight)
	
	print("~" * 30 + "{After taking items}" + "~" * 30)
	knight.take_item(Item("Shield of knowledge", defence=50))
	mag.take_item(Item("Sword of complexity", dmg=60))
	
	print(mag)
	print(knight)
	
	print("~" * 30 + "{After attack}" + "~" * 30)
	
	mag.attack(knight)
	knight.attack(mag)
	
	print(mag)
	print(knight)






























