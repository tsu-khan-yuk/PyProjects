#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 26.04.2020
#  -> task 1: Создайте класс "животное". Наполните его данными и методами на свое усмотрение.
#  -> task 2: Опишите с помощью классов кухонную технику в виде диаграммы
#  (пример https://www.intuit.ru/EDI/23_04_17_1/1492899714-28128/tutorial/356/objects/2/files/02_05.gif).
#  Продумайте классы, их назначение и взаимосвязи. Реализовать с описанием свойств и методов.
# * Описать все то же с помощью питона.
######################################################################################################################


class Animal:
	name = None
	kind = None
	voice = None

	def __init__(self, name=None, kind=None, voice=None):
		self.name = name if isinstance(name, str) else None
		self.kind = kind if isinstance(kind, str) else None
		self.voice = voice if isinstance(voice, str) else None

	def get_voice(self) -> None:
		if self.voice is not None:
			print(f"{self.voice}!!")
		else:
			print("Error: voice is None type")

	def get_info(self) -> None:
		print("+" + "-" * 20 + "+")
		print(f"|My name is {self.name}")
		print(f"|My kind is {self.kind}")
		print(f"|My voice is {self.voice}")
		print("+" + "-" * 20 + "+")


obj = Animal("Sharic", "dog", "gav")
obj.get_info()
obj.get_voice()


class Рousehold_appliances
