def greetings() -> "True, False":
	"""Функция спрашивает пользователя хочет ли он продолженя
	повторения кода или его завершения"""
	while True:
		string = input(">>> Позволите сработать программе еще раз(Y/N)?: ").lower()
		if string == "y":
			return True
		elif string == "n":
			return False
		else:
			print("Не понимаю о чем вы( Повторите, пожплуйста")
			continue
