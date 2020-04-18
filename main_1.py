###########################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 07.04.2020
# -> task 1: Дано два числа (a=10, b=30).
#   Вывести на экран результат математического взаимодействия (+, -, *, / ) этих чисел.
# -> task 2: Создать переменную и записать в нее результат сравнения (<, > , ==, !=) этих чисел
#   После этого вывести на экран значение полученную переменную.
# -> task 3: Создать переменную - результат конкатенации (сложения) строк str1="Hello " и str2="world".
#   Вывести на ее экран.
###########################################################################################################

#task 1:
a = 10
b = 30
print("task 1: a = 10, b = 30")
print("a + b =", a + b)
print("a - b =", a - b)
print("b - a =", b - a)
print("a * b =", a * b)
print("a / b =", a / b)
print("b / a =", b / a)

#task 3:
print("\ntask 2: a = 10, b = 30")
check = a > b
print("check(a > b) =", check)
check = b > a
print("check(b > a) =", check)
check = a < b
print("check(a < b) =", check)
check = b < a
print("check(b < a) =", check)
check = a == b
print("check(a == b) =", check)
check = b == a
print("check(b == a) =", check)
check = a != b
print("check(a != b) =", check)
check = b != a
print("check(b != a) =", check)

#task 3:
print("\ntask 3:")
str1 = "Hello "
str2 = "world"
str3 = str1 + str2
print(str3)