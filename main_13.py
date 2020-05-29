#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 30.05.2020
# -> task 1: Создайте репозиторий на GitLab или GitHub. Сохраните туда игру (далее любые изменения игры публикуйте
#   с помощью git). Сохраните отдельной веткой (пусть будет HW14) дз по регулярным выражениям
# -> task 2: Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB,
#   a12345BC) с помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является
#   номерным знаком. Если является номерным знаком - возвращает саму строку.
# -> *task 3: Напишите класс, который выбирает из произвольного текста номерные знаки и возвращает их в виде
#   пронумерованного списка
#######################################################################################################################
from re import *


class Parser:
    __string = None
    __tokens = None
    __base = [
        compile(r"[A-Z|А-Я]{2}[0-9]{4}[A-Z|А-Я]{2}"),
        compile(r"[1-9]{2}\s[0-9]{3}-[0-9]{2}[A-Z|А-Я]{2}"),
        compile(r"[a-z|а-я][0-9]{5}[A-Z|А-Я]{2}")
    ]

    def __init__(self, string: str):
        """Конструктор, в котором сохраняется введенная строка и парситься"""
        if not isinstance(string, str):
            raise TypeError
        self.__string = string
        self.__tokens = dict()
        if len(string) >= 11:
            self.__flag = True
            self.__whole_string_processing()
        else:
            self.__tokens["single"] = self.single_string_parser(string)

    def __whole_string_processing(self):
        """Метод, который находит все типы номерних знаков и записывает их в словарь"""
        self.__tokens["first"] = self.__base[0].findall(self.__string)
        self.__tokens["second"] = self.__base[1].findall(self.__string)
        self.__tokens["third"] = self.__base[2].findall(self.__string)

    @property
    def first_type_num(self):
        return self.__tokens["first"]

    @property
    def second_type_num(self):
        return self.__tokens["second"]

    @property
    def third_type_num(self):
        return self.__tokens["third"]

    @property
    def string(self):
        return self.__string

    @classmethod
    def single_string_parser(cls, string: str) -> "None, str":
        """Метод класса для поиска любого типа номерных знаков"""
        length = len(string)
        if length == 8:
            if string[1].isdigit():
                return cls.__base[2].search(string).string
            else:
                return cls.__base[0].search(string).string
        elif length == 11 and "-" in string and " " in string:
            return cls.__base[1].search(string).string
        raise Exception("Patern not found or punctuality in string")

    def __str__(self):
        tkn_set = self.__tokens.keys()
        output_str = "+------------------------+\n"
        output_str += f"| string: {self.__string}\n"
        if "single" not in tkn_set:
            for key in tkn_set:
                output_str += f"| {key} type:\n"
                for val in self.__tokens[key]:
                    output_str += f"|\t\t{val}\n"
        else:
            output_str += f"| result: {self.__tokens['single']}\n"
        output_str += f"+------------------------+\n"
        return output_str


if __name__ == "__main__":
    exmpl = Parser("AА1234BB12 123-45ABa12345BCAА1234BBAА1234BB12 123-45ABa12345BCAА1234BB")
    print(exmpl)

























