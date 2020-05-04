#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 05.05.2020
#  -> task 1: Создайте класс "животное". Наполните его данными и методами на свое усмотрение.
#  -> task 2: Опишите с помощью классов кухонную технику в виде диаграммы
#  (пример https://www.intuit.ru/EDI/23_04_17_1/1492899714-28128/tutorial/356/objects/2/files/02_05.gif).
#  Продумайте классы, их назначение и взаимосвязи. Реализовать с описанием свойств и методов.
# * Описать все то же с помощью питона.
######################################################################################################################


class Animal:
	"""Класс 'животное' направлен на примитивное взаимодействие
	 с конретно 'созданым' животним"""
	name = None
	kind = None
	voice = None

	def __init__(self, name=None, kind=None, voice=None):
		self.name = name if isinstance(name, str) else None
		self.kind = kind if isinstance(kind, str) else None
		self.voice = voice if isinstance(voice, str) else None

	def get_voice(self) -> None:
		"""Метод дает возможность узнать какой 'голос' у животного"""
		if self.voice is not None:
			print(f"Voice: {self.voice}!!")
		else:
			print("Error: voice is None type")

	def get_info(self) -> None:
		"""Метод печатает ту информацию что указал пользовеатель в конструкторе"""
		print("+" + "-" * 20 + "+")
		print(f"|My name is {self.name}")
		print(f"|My kind is {self.kind}")
		print(f"|My voice is {self.voice}")
		print("+" + "-" * 20 + "+")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ======================================================================================================================

def asking(string: str) -> bool:
	while True:
		buff = input(">>> " + string).lower()
		if buff == "y":
			return True
		elif buff == "n":
			return False
		else:
			print("Don`t understand. Try again)")


class HouseholdAppliances:
	"""Абстрактный класс, в котором указывается цель
	и устанаваливается выключеный режим(mode = False)"""
	target = None
	_mode = False

	def __init__(self, target=None):
		self._mode = False
		self.target = target if isinstance(target, str) else None

	def change_mode(self) -> None:
		"""Смена режима"""
		self._mode = not self._mode

	def use(self) -> None:
		pass


# ======================================================================================================================

class Iron(HouseholdAppliances):
	"""Класс утюг, в котором указыватся интенсивность пара и вес"""
	weight = None
	steam_level = 0

	def __init__(self, target=None, steam=0, weight=None):
		super().__init__(target)
		self.set_options(steam, weight)

	def set_options(self, steam_level, weight) -> bool:
		"""Метод устанавлиает все опции утюга.
			Если хоть один из параметров не удалось установить(None),
			то возвращветься False"""
		self.weight = weight if isinstance(weight, (int, float)) else None
		self.steam_level = steam_level if isinstance(steam_level, int) and 0 < steam_level < 3 else None
		if not (self.steam_level and self.weight):
			return False
		return True

	def use(self) -> None:
		"""Если один раз запустили этот метод, значит утюг работает,
			что бы использовать еще раз его нужно перезапсутить"""
		if not self._mode:
			print(f"Ironing {self.target} with steam level: {self.steam_level}")
			self.change_mode()
		else:
			self._mode = False if asking("Iron is on! Do you want to turn off it?(Y/N): ") else True


class WashingMachine(HouseholdAppliances):
	"""Класс стиральная машина, в котором устанавливаются размеры машины,
		температура и опция работы"""
	height = None
	width = None
	long = None
	temperature = None
	option = None

	def __init__(self, target=None, temp=None, option=None, height=None, width=None, long=None):
		super().__init__(target)
		self.set_size(height, width, long)
		self.set_options(option, temp)

	def set_size(self, height, width, long) -> bool:
		"""Метод устанавлиает все измерения стиральной машины.
			Если хоть один из параметров не удалось установить(None),
			то возвращветься False"""
		self.height = height if isinstance(height, (int, float)) and height > 0 else None
		self.width = width if isinstance(width, (int, float)) and width > 0 else None
		self.long = long if isinstance(long, (int, float)) and long > 0 else None
		if not(self.height and self.width and self.long):
			return False
		return True

	def set_options(self, option, temp) -> bool:
		"""Метод устанавлиает все опции стиральной машины.
			Если хоть один из параметров не удалось установить(None),
			то возвращветься False"""
		self.option = option if isinstance(option, str) else None
		self.temperature = temp if isinstance(temp, int) and temp > 0 else None
		if not (self.option or self.temperature):
			return False
		return True

	def use(self) -> None:
		"""Если один раз запустили этот метод, значит утюг работает,
			что бы использовать еще раз его нужно перезапсутить"""
		if not self._mode:
			print(f"Washing {self.target} with {self.option} option and temperature: {self.temperature}")
			self.change_mode()
		else:
			self._mode = False if asking("Washing machine is on! Do you want to turn off it?(Y/N): ") else True


class KitchenEquipment(HouseholdAppliances):
	"""Абстрактный класс для кухонной техники"""
	def __init__(self, target=None):
		super().__init__(target)


# ======================================================================================================================

class Bake(KitchenEquipment):
	"""Абстрактный класс для печей, в котором устанавливается температура
		время и поция приготовления"""
	temperature = None
	time = None
	option = None

	def __init__(self, target=None, temp=None, time=None, opt=None):
		super().__init__(target)
		self.set_options(temp, time, opt)

	def set_options(self, temp, time, opt) -> bool:
		"""Метод устанавлиает все опции печки.
			Если хоть один из параметров не удалось установить(None),
			то возвращветься False"""
		self.temperature = temp if isinstance(temp, int) and temp > 0 else None
		self.time = time if isinstance(time, int) and time > 0 else None
		self.option = opt if isinstance(opt, str) else None
		if not (self.temperature and self.option and self.time):
			return False
		return True


class Harvester(KitchenEquipment):
	"""Класс для комбайна, но не очень понимаю как он относиться к
		кухонной технике, поэтому так скудненько("""
	def __init__(self, target=None):
		super().__init__(target)

	def use(self) -> None:
		print(f"Mows {self.target}")


# ======================================================================================================================

class ElectricBake(Bake):
	"""Класс для электрической плиты, в котором указывается количество конфорок,
		температура, время и опции приготовления"""
	burner_amount = None

	def __init__(self, target=None, burner=None, temp=None, time=None, opt=None):
		super().__init__(target, temp, time, opt)
		self.burner_amount = burner if isinstance(burner, int) else None

	def use(self) -> None:
		"""Если один раз запустили этот метод, значит электрическая плита работает,
			что бы использовать еще раз его нужно перезапсутить"""
		if not self._mode:
			print(f"Baking {self.target} for {self.time} minutes with {self.option} option")
			self.change_mode()
		else:
			self._mode = False if asking("Electric bake is on! Do you want to turn off it?(Y/N): ") else True


class GasBake(Bake):
	"""Класс для газовой плиты, в котором указывается количество конфорок,
		температура, время и опции приготовления"""
	burner_amount = None

	def __init__(self, target=None, burner=None, temp=None, time=None, opt=None):
		super().__init__(target, temp, time, opt)
		self.burner_amount = burner if isinstance(burner, int) else None

	def use(self) -> None:
		"""Если один раз запустили этот метод, значит газовая плита работает,
			что бы использовать еще раз его нужно перезапсутить"""
		if not self._mode:
			print(f"Baking {self.target} for {self.time} minutes with {self.option} option")
			self.change_mode()
		else:
			self._mode = False if asking("Gas bake is on! Do you want to turn off it?(Y/N): ") else True


class MicrowaveOven(Bake):
	"""Класс для микроволновки, в котором указывается
			температура, время и опции приготовления"""

	def __init__(self, target=None, temp=None, time=None, opt=None):
		super().__init__(target, temp, time, opt)

	def use(self) -> None:
		"""Если один раз запустили этот метод, значит микроволновка работает,
			что бы использовать еще раз его нужно перезапсутить"""
		if not self._mode:
			print(f"Baking {self.target} for {self.time} minutes with {self.option} option")
			self.change_mode()
		else:
			self._mode = False if asking("Microwave oven is on! Do you want to turn off it?(Y/N): ") else True

# ======================================================================================================================


if __name__ == "__main__":

	print("-> task 1:")
	obj = Animal("Sharic", "dog", "gav")
	obj.get_voice()
	obj.get_info()

	print("\n-> task 2:")
	print("Object Iron:")
	obj = Iron("shirt", 1, 20.4)
	print("Weight:", obj.weight, "kg")
	obj.use()

	print("\nObject WashingMachine:")
	obj = WashingMachine("hat", 30, "wash", 1.60, 1, 1.60)
	obj.use()

	print("\nObject Harvester:")
	obj = Harvester("field")
	obj.use()

	print("\nObject ElectricBake:")
	obj = ElectricBake("bread", 4, 160, 40, "traditional")
	obj.use()

	print("\nObject GasBake:")
	obj = GasBake("chicken", 4, 200, 10, "traditional")
	obj.use()

	print("\nObject Microwave:")
	obj = MicrowaveOven("potato", 190, 30, "traditional")
	obj.use()
