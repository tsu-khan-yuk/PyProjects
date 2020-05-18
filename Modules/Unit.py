from abc import ABC, abstractmethod
from PyProjects.Modules.Pocket import Pocket
from random import randint


# todo: добваить метод который будет вычилсять веротность
#  атаки с двойным уроном  //
# todo: Дописать везде декоратор для проверки типов

def check_type(*types):
	def decor(func):
		def wrapper(*args):
			if types[0] is True:
				types_list = list(types[1:])
				args_list = list(args[1:])
			else:
				types_list = list(types[:])
				args_list = list(args[:])
			if len(types_list) != len(args_list):
				raise TypeError("Check decor parameters")
			mas = dict(map(lambda *x: x, types_list, args_list))
			for arg in mas.items():
				if not isinstance(arg[1], arg[0]):
					raise TypeError
			return func(*args)
		return wrapper
	return decor


class Unit(ABC):
	_name = None
	_health = 100
	_dmg = 1
	_defence = 10
	_amplifiers = None
	
	@abstractmethod
	def attack(self, enemy) -> None:
		pass
	
	@abstractmethod
	def _get_dmg(self) -> int:
		pass
	
	@abstractmethod
	def _get_defence(self) -> int:
		pass
	
	@staticmethod
	def luck_generator() -> int:
		"""Генератор, который возвращает процент вероятности от 0 до 100"""
		while True:
			yield randint(0, 100)
	
	@staticmethod
	@check_type(int)
	def power_up(dmg: int) -> int:
		"""Функция, которая возвращает либо 0(если генератор вернул <75),
			или полное значение(если генератор вернул >75)"""
		func = Unit.luck_generator()
		if next(func) > 75:
			return dmg
		else:
			return 0
	
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
