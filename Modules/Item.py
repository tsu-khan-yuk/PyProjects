from PyProjects.Modules.Checker import check_type


class Item:
	"""Класс отвечает за вещь(усилитель), который можно будет
	сложить в обьект Pocket"""
	_name = None
	_base = None
	_attachment = None
	_check_att = {"Unit", "Mage", "Knight"}

	def __init__(self, name="unknown", attachment="Unit", defence=0, dmg=0):
		"""Создает предмет, которй может повысить домаг и/или защиту"""
		if isinstance(name, str) and isinstance(defence, (int, float)) and isinstance(dmg, (int, float)) \
					and isinstance(attachment, str) and attachment in self._check_att:
			self._attachment = attachment
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
	def attach(self) -> str:
		return self._attachment
	
	@property
	def base(self) -> dict:
		"""Возвращает словарь из характеристик предмета"""
		return self._base
	
	def __str__(self):
		string = "+----------------------+\n"
		string += f"| name: {self._name}\n"
		string += f"| attachment: {self._attachment}\n"
		string += f"| defence: {self._base['defence']}\n"
		string += f"| dmg: {self._base['dmg']}\n"
		string += "+----------------------+\n"
		return string
