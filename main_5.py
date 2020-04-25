#####################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 21.04.2020
#  -> Написать функцию, принимающую один аргумент. Функция жолджна вывести на экран тип данных этого аргумента (type).
#  -> Написать функцию, принимающую два аргумента.Если оба аргумента относятся к числовым типам - вернуть их
#   произведение, если к строкам - соединить в одну строку и вернуть, если первый строка, а второй нет - вернуть
#   словарь, в котором ключ - первый аргумент а значение - второй, в любом другом случае вернуть кортеж из аргументов
#  -> Дан словарь продавцов и цен на какой то товар у разных продавцов на hotline: { ‘citrus’: 47.999, ‘istudio’ 42.999,
#   ‘moyo’: 49.999, ‘royal-service’: 37.245, ‘buy.ua’: 38.324, ‘g-store’: 37.166, ‘ipartner’: 38.988, ‘sota’: 37.720 }.
#   Написать функцию возвращающую список имен продавцов, чьи цены попадают в определенный диапазон. Функция должна
#   принимать словарь, начало и конец диапазона и возвращать список имен.
#  -> * Пользователь вводит строку произвольной длины. Написать функцию, которая должна вернуть словарь следующего
#   содержания: ключ - количество букв в слове, значение - список слов с таким количеством букв. Отдельным ключом
#   количество пробелов и знаки препинания
#  Например:
#  {
#  "0": количество пробелов в строке
#  "1": list слов из одной буквы
#  "2": list слов из двух букв
#  "3": list слов из трех букв
#  и т.д ...
#  "punctuation" : tuple уникальных знаков препинания
#  }
#####################################################################################################################


def tsk_1(tmp):
    try:
        int(tmp)
        print("Тип значения: int")
    except ValueError:
        try:
            float(tmp)
            print("Тип значения: float")
        except ValueError:
            if tmp.startswith("(") and ("," in tmp) and tmp.endswith(")"):
                print("Тип значения: tuple")
            elif tmp.startswith("{") and tmp.endswith("}"):
                tmp = tmp.split(",")
                count = 0
                for i in tmp:
                    if ":" in tmp:
                        count += 1
                if count == len(tmp):
                    print("Тип значения: dictionary\n")
                else:
                    print("Тип значения: set\n")
            elif tmp.startswith("[") and tmp.endswith("]"):
                print("agv")
            else:
                print("Тип значения: string\n")


def tsk_2(val1, val2):
    # Написать функцию, принимающую два аргумента.Если оба аргумента относятся к числовым типам - вернуть их
    #  произведение, если к строкам - соединить в одну строку и вернуть, если первый строка, а второй нет - вернуть
    #  словарь, в котором ключ - первый аргумент а значение - второй, в любом другом случае вернуть кортеж из аргументов
    if (type(val1) == type(val2)) and isinstance(val1, (int, str)):
        return val1 * val2 if type(val1) == int else val1 + val2
    elif isinstance(val1, str) and not isinstance(val2, str):
        return {val1: val2}
    else:
        return val1, val2


def tsk_3(dct: dict, begin, end):
    # -> Дан словарь продавцов и цен на какой то товар у разных продавцов на hotline: { ‘citrus’: 47.999,
    # ‘istudio’ 42.999, ‘moyo’: 49.999, ‘royal-service’: 37.245, ‘buy.ua’: 38.324, ‘g-store’: 37.166, ‘ipartner’:
    # 38.988, ‘sota’: 37.720 }. Написать функцию возвращающую список имен продавцов, чьи цены попадают в определенный
    # диапазон. Функция должна принимать словарь, начало и конец диапазона и возвращать список имен.
    if isinstance(dct, dict) and isinstance(begin, (float, int)) and isinstance(end, (float, int)):
        shop_list = []
        for shop, price in dct.items():
            if begin <= price <= end:
                shop_list.append(shop)
        return shop_list
    else:
        return None


def tsk_4():
    print("-> task 4")


def input_processing(string):
    str1 = input(string)
    if "|" in str1:
        tmp = str1.split("|")
        if tmp[1] == "int":
            try:
                tmp = int(tmp[0])
            except ValueError:
                print("Something went wrong")
            return tmp
        elif tmp[1] == "float":
            try:
                tmp = float(tmp[0])
            except ValueError:
                print("Something went wrong")
            return tmp
        elif tmp[1] == "str":
            return tmp[0]
        elif tmp[1] == "list":
            tmp = list(tmp[0])
            return tmp
        elif tmp[1] == "dict":
            tmp1 = tmp[0].split(", ")
            dct = dict()
            for i in tmp1:
                i = i.split(":")
                dct[i[0]] = i[1]
            return dct
        elif tmp[1] == "tuple":
            tmp = tuple(tmp[0])
            return tmp
        elif tmp[1] == "set":
            tmp = set(tmp[0])
            return tmp


options = {"1", "2", "3", "4", "all", "quit"}


def task_ctrl(opt):
    if opt in options:
        return opt
    else:
        print("Не понимаю о чем вы, попробуйте еще раз)")
        return None


tab = 20
menu_cycle = 1
while True:
    print("~" * 30 + "{Итерация № %d}" % menu_cycle + "~" * 30)
    print(" " * tab + "+--------------------------------+")
    print(" " * tab + "|  Первое задание       |  1     |")
    print(" " * tab + "|  Второе задание       |  2     |")
    print(" " * tab + "|  Третье задание       |  3     |")
    print(" " * tab + "|  Четвертое задание    |  4     |")
    print(" " * tab + "|  Все по очереди       |  all   |")
    print(" " * tab + "|  Завершение программы |  quit  |")
    print(" " * tab + "+--------------------------------+")
    task = task_ctrl(input(">>> Введите режим работы: "))
    menu_cycle += 1

    if task == "quit":
        break
    elif task is None:
        continue
    elif task == "all":

        print("gav")

    elif task is "1":

        print("\n-> task 1")
        tsk_1(input(">>> Введите значение: "))

    elif task is "2":

        print("-> task 2:")
        print("{\nФукнкция корректированого ввода работает так:")
        print("<значение нужного типа>|<тип данных>\n}")
        var1 = input_processing(">>> Введите первое значение: ")
        var2 = input_processing(">>> Введите второе значение: ")
        ret = tsk_2(var1, var2)
        print(type(ret), ret)

    elif task is "3":

        print("-> task 3:")
        HotLine = {
            "citrus": 47.999,
            "istudio": 42.999,
            "moyo": 49.999,
            "royal-service": 37.245,
            "buy.ua": 38.324,
            "g-store": 37.166,
            "ipartner": 38.988,
            "sota": 37.720
        }
        begin_ = input_processing(">>> Введите начало диапозона: ")
        end_ = input_processing(">>> Введите конец диапозона: ")
        print("Before:", HotLine)
        lst = tsk_3(HotLine, begin_, end_)
        print("After:", lst)

    elif task is "4":

        print("-> task 4:")
        tsk_4()
