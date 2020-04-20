#####################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 20.04.2020
# -> task 1: Доделайте последнее задание из практики (Искусственный интеллект)
# -> task 2: Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44,]).
#   Написать программу, которая удалит из него все числа, которые меньше 18 и больше 81.
# -> *task 3:  Написать алгоритм перехода через улицу. Ваш робот стоит на одной стороне улицы и должен попасть
#   не другую сторону по пешеходному переходу. Робот может шагать вперед, смотреть по сторонам и вперед.
#   Можно описать как угодно, хоть блок-схемой, хоть текстом, главное понятно. Что такое блок-схема
#   https://uk.wikipedia.org/wiki/%D0%91%D0%BB%D0%BE%D0%BA-%D1%81%D1%85%D0%B5%D0%BC%D0%B0
# -> *task 4: Ввести из консоли строку. Найти в строке самое длинное слово, в котором присутствуют подряд
#   две согласные буквы. Если в строке присутствует слово с тремя согласными буквами подряд - завершить выполнение.
#####################################################################################################################

options = ["1", "2", "3", "4", "all", "quit"]
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
    task = input(">>> Введите режим работы: ")

    menu_cycle += 1

    if task == "quit":
        break

    check = True
    for i in options:
        if task == i:
            check = False
            break
    if check:
        print("\nНе понимаю о чем вы, попробойте еще раз)\n")
        continue

    if task == "1" or task == "all":

        # task 1:
        print("\n-> Задание 1:")
        st = input().split()
        for word in st:
            if word.startswith('+') and len(word) == 13 and word[1:].isdigit():
                # Если слово начинается с плюса, длинной в 13 элементов и после 0 элемента все цыфры,
                # то это номер телефона
                print('Это телефоный номер')
            elif '@' in word and "." in word:
                # Если в слове есть "@" и ".", то возможно это e-mail
                tmp = word.split('@')
                if len(tmp[0]) >= 3 and "." in tmp[1] and not tmp[1].endswith(".") \
                        and not tmp[1].startswith(".") and len((tmp[1].split("."))[1]) <= 3:
                    # Если слово до "@" имеет >= 3 элементов,
                    # "." находитьс во втором слове после "@",
                    # второе слово не начинается и не заканчивается на "."
                    # и если после "." <= 3 элементов, то это точно e-mail
                    print("Это e-mail")
            elif word[:1].isupper() and len(word) >= 2:
                # Если первая буква слова большая и если больше или равно 2
                # то это либо имя, либо фамимлия
                print("Либо имя, либо фамилия")
            else:
                print("Не понимаю что это")
        if task == "1":
            continue

    if task == "2" or task == "all":

        # task 2:
        print("\n-> Задание 2:")
        while True:                                                         # \
            try:                                                            # | Определение размера
                size = int(input(">>> Какого размера список будет?: "))     # | и создание пустого списка.
                break                                                       # | Если значение не int, то программа
            except ValueError:                                              # | переспрашивает до тех пор пока
                print("Тут что-то не так, попробуйте еще раз")              # | не введут int
        lst1 = []                                                           # /
        while True:
            print(" " * tab + "+--------------------------------+")
            print(" " * tab + "|  Авто-заполение       |  auto  |")
            print(" " * tab + "|  Ручной ввод          | manual |")
            print(" " * tab + "+--------------------------------+")
            option = input(">>> Хотите ввести цифру сами или что бы все сделал компьютер: ")
            if option == "manual":
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{РУЧНОЙ ВВОД}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                i = 0
                while i < size:
                    # Если введено не число, то программа будет переспрашивать
                    # до тех пора пока не будет введено значение int
                    try:
                        lst1.append(int(input(">>> Введите " + str(i) + " элемент: ")))
                        i += 1
                    except ValueError:
                        print("Тут что-то не так")
                break
            elif option == "auto":
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{АВТОМАТИЧЕСКЙ ВВОД}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                import random

                print("Если есть желание указать диапозон, то укажите ниже")
                print("Если желания нету, то просто нажмите на одном из вводов Enter")
                # Если введено что-то не int значения, то программа считает, что пользователь
                # желает что бы спиок был заполнен автоматически
                try:
                    x = int(input(">>> От: "))
                    y = int(input(">>> До: "))
                except ValueError:
                    print("Значения установлены автоматически")
                    x = None
                    y = None
                x = 18 - (81 - 18) if x is None else x
                y = 81 + (81 - 18) if y is None else y
                lst1 = [random.randint(x, y) for i in range(size)]
                break
            else:
                print("Не помнимаю о чем, попробуйте еще раз)")
                continue
        print("Before: ", lst1)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{ОБРАБОТКА ДАННЫХ В СПИСКЕ}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Пытался разобраться с тем удаляется ли лишняя память при реинициализации списка с попомощью
        # sys.getsizeof() и __sizeof__(), но получилось не очень) поэтому вот два варианта
        # lst1 = [i for i in lst1 if not 18 < i < 81]
        i = 0
        while i < len(lst1):
            if not 18 < lst1[i] < 81:
                lst1.pop(i)
            else:
                i += 1
        print("After: ", lst1)
        if task == "2":
            continue

    if task == "3" or task == "all":
        # task 3:
        print("\n-> Задание 3:")
        print("""Посмотреть """)
        if task == "3":
            continue

    if task == "4" or task == "all":

        # task 4:
        print("\n-> Задание 4:")
        flag = True
        while flag:
            str1 = input(">>> Введите предложение: ")
            str1 = str1.split()
            long = ""
            three_consonants = ""
            for i in str1:
                buff = i
                i.lower()
                if i.isalpha():
                    check = None
                    for j in i:
                        if not (j == "a" or j == "i" or j == "u" or j == "e" or j == "o" or j == "y"):
                            check += 1
                        else:
                            if check == 2 and len(i) > len(long):
                                long = buff
                            elif check == 3:
                                three_consonants = buff
                                flag = False
                            check = 0

            print("check(2) =", long if check == 0 else buff)
            print("check(3) =", three_consonants if check == 0 else buff)
