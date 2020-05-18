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
