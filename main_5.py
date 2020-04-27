#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 26.04.2020
#  -> task 1: Написать функцию, принимающую один аргумент. Функция жолджна вывести на экран тип данных этого аргумента
#   (type).
#  -> task 2: Написать функцию, принимающую два аргумента.Если оба аргумента относятся к числовым типам - вернуть их
#   произведение, если к строкам - соединить в одну строку и вернуть, если первый строка, а второй нет - вернуть
#   словарь, в котором ключ - первый аргумент а значение - второй, в любом другом случае вернуть кортеж из аргументов
#  -> task 3: Дан словарь продавцов и цен на какой то товар у разных продавцов на hotline: { ‘citrus’: 47.999,
#   ‘istudio’ 42.999, ‘moyo’: 49.999, ‘royal-service’: 37.245, ‘buy.ua’: 38.324, ‘g-store’: 37.166, ‘ipartner’: 38.988,
#   ‘sota’: 37.720 }.  Написать функцию возвращающую список имен продавцов, чьи цены попадают в определенный диапазон.
#   Функция должна принимать словарь, начало и конец диапазона и возвращать список имен.
#  -> *task 4: Пользователь вводит строку произвольной длины. Написать функцию, которая должна вернуть словарь
#   следующего содержания: ключ - количество букв в слове, значение - список слов с таким количеством букв.
#   Отдельным ключом количество пробелов и знаки препинания
#   Например:
#   {
#   "0": количество пробелов в строке
#   "1": list слов из одной буквы
#   "2": list слов из двух букв
#   "3": list слов из трех букв
#   и т.д ...
#   "punctuation" : tuple уникальных знаков препинания
#   }
#######################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{ СДЕЛАННЫЕ ЗАДАНИЯ }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def tsk_1(val) -> None:
    """Функция принимает один аргумент.
    Анализирует значение и выводит тип этого значение"""
    val_type = type(val)
    if val_type is int:
        print("Тип данных: int")
    elif val_type is float:
        print("Тип данных: float")
    elif val_type is bool:
        print("Тип данных: bool")
    elif val_type is str:
        print("Тип данных: str")
    elif val_type is list:
        print("Тип данных: list")
    elif val_type is dict:
        print("Тип данных: dict")
    elif val_type is tuple:
        print("Тип данных: tuple")
    elif val_type is set:
        print("Тип данных: set")
    else:
        print("Не понимаю")
  

def tsk_2(val1, val2) -> "int, str, tuple":
    """Функция принимает два аргумента:
    - если оба аргумента относятся к числовым типам - вернуть их произведение
    - если к строкам - соединить в одну строку и вернуть
    - если первый строка, а второй нет - вернуть словарь, в котором ключ - первый аргумент а значение - второй
    - в любом другом случае вернуть кортеж из аргументов"""
    if (type(val1) == type(val2)) and isinstance(val1, (int, str)):
        return val1 * val2 if type(val1) == int else val1 + val2
    elif isinstance(val1, str) and not isinstance(val2, str):
        return {val1: val2}
    else:
        return val1, val2


def tsk_3(dct: dict, begin, end) -> "list, None":
    """Функция ищет цены что попадают в диапозон (begin:end),
    делает из ключей что соотвецтвуют этим значениям спиок и возвращает его.
    В случае если в таком диапазоне нету такого продавца, возращается None"""
    if isinstance(dct, dict) and isinstance(begin, (float, int)) and isinstance(end, (float, int)):
        shop_list = []
        for shop, price in dct.items():
            if begin <= price <= end:
                shop_list.append(shop)
        return shop_list
    else:
        return None


def tsk_4(string: str) -> dict:
    """Функция принимает строку произвольной длинны и возвращает словарь следующего содержания:
     - ключ - количество букв в слове
     - значение - список слов с таким количеством букв"""
    tmp = string.split()
    dct = {"0": len(tmp) - 1}
    punctuation = set()
    the_longest = len(max(tmp, key=len)) + 1
    for i in range(1, the_longest):
        # Находит слово с максимальным количеством букв и запускает цикл,
        # который проработат в это количество раз(заполняя списками каждую ячейку словаря)
        buff = list()
        for j in tmp:
            # Цикл проходит по словам из сторки и проверяет последний элемент
            # каждого слова на то знак препинания это или нет
            if len(j) - 1 == i and not (j[-1] in "1234567890qwertyuiopasdfghjklzxcvbnm"):
                # Если в большом цикле идет итерация для слов с i-шным количеством букв и в нем в качестве
                # полседенего элемента присуцтвует знак припинания, то нам сюда
                buff.append(j[:-1])
                punctuation.add(j[-1])
            elif len(j) == i and j[-1] in "1234567890qwertyuiopasdfghjklzxcvbnm":
                buff.append(j)
        dct[str(i)] = buff
    dct["punctuation"] = tuple(punctuation)
    return dct


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{ ФУНКЦИИ ДЛЯ УПРАВЛЕНИЯ ЦИКЛОМ }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def input_processing(string: str) -> "str, int, float, list, dict, tuple, set":
    """Функция принимает сторку и преобразовывает ее
    в тип соотвецтвенно указаниям полсе '|'
    <значение нужного типа>|<тип данных> """
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
        else:
            print("Something went wrong")
    else:
        return str1


options = {"1", "2", "3", "4", "all", "quit"}


def task_ctrl(opt):
    if opt in options:
        return opt
    else:
        print("Не понимаю о чем вы, попробуйте еще раз)")
        return None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{ ОСНОВНАЯ ПРОГРАММА }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
    if task is None:
        continue

    if task is "1" or task == "all":

        print("\n-> task 1")
        print("!!! Фукнкция корректированого ввода работает так: !!!")
        print("!!!      <значение нужного типа>|<тип данных>     !!!")
        buffer = input_processing(">>> Введите значение: ")
        tsk_1(buffer)
        if task == "1":
            continue

    if task is "2" or task == "all":

        print("\n-> task 2:")
        print("!!! Фукнкция корректированого ввода работает так: !!!")
        print("!!!      <значение нужного типа>|<тип данных>     !!!")
        var1 = input_processing(">>> Введите первое значение: ")
        var2 = input_processing(">>> Введите второе значение: ")
        ret = tsk_2(var1, var2)
        print(type(ret), ret)
        if task == "2":
            continue

    if task is "3" or task == "all":

        print("\n-> task 3:")
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
        print("!!! Фукнкция корректированого ввода работает так: !!!")
        print("!!!      <значение нужного типа>|<тип данных>     !!!")
        begin_ = input_processing(">>> Введите начало диапозона: ")
        end_ = input_processing(">>> Введите конец диапозона: ")
        print("Before:", HotLine)
        lst = tsk_3(HotLine, begin_, end_)
        print("After:", lst)
        if task == "3":
            continue

    if task is "4" or task == "all":

        print("\n-> task 4:")
        dct1 = tsk_4(input(">>> Введите строку для анализа: "))
        print("dct =", dct1)
