#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 24.05.2020
# -> task 1: Создайте репозиторий на GitLab или GitHub. Сохраните туда игру (далее любые изменения игры публикуйте
#   с помощью git). Сохраните отдельной веткой (пусть будет HW14) дз по регулярным выражениям
# -> task 2: Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB,
#   a12345BC) с помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является
#   номерным знаком. Если является номерным знаком - возвращает саму строку.
# -> *task 3: Напишите класс, который выбирает из произвольного текста номерные знаки и возвращает их в виде
#   пронумерованного списка
#######################################################################################################################
from re import *


# AА1234BB, 12 123-45AB, a12345BC
# r"[A-Z]{2}[0-9]{4}[A-Z]{2}", r"[1-9]{2}\s[0-9]{3}-[0-9]{2}[A-Z]{2}", r"[a-z][0-9]{5}[A-Z]{2}"
base = [
    compile(r"[A-Z|А-Я]{2}[0-9]{4}[A-Z|А-Я]{2}"),               # AА1234BB
    compile(r"[1-9]{2}\s[0-9]{3}-[0-9]{2}[A-Z|А-Я]{2}"),    # 12 123-45AB
    compile(r"[a-z|а-я][0-9]{5}[A-Z|А-Я]{2}")                   # a12345BC
]


def parser(string: str) -> "None, str":
    global base
    length = len(string)
    if not isinstance(string, str) or len(string) > 12:
        raise Exception("length or type error")
    if length == 8:
        if string[1].isdigit():
            return base[2].search(string)
        else:
            return base[0].search(string)
    elif length == 11 and "-" in string and " " in string:
        return base[1].search(string)
    raise Exception("Not found")


# print(parser("AА1234BB"))
# print(parser("12 123-45AB"))
# print(parser("a12345BC"))

class Parser:
    _string = None
    _tokens = None
    _tpl = r"[0-9]{3}-[0-9]{2}[A-Z]{2}"

    def __init__(self, string: str):
        if not isinstance(string, str):
            raise TypeError
        self._string = string
        self._tokens = string.split()
        self._string_processing()

    def _string_processing(self):
        buff = ""
        for word in self._tokens:
            word = self._deleting_punctuality(word)
            if "-" in word and len(word) is 8 and search(self._tpl, word):
                tmp = buff + word
            buff = word

    def _deleting_punctuality(self, word):
        print(word)
        word = sub(r"^\W.{6}\W$", "", word)
        print(word)
        print()
        return word


obj = Parser(",AА1234BB, 12 123-45AB, a12345BC")

