#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 24.05.2020
#  -> task 1: Подключитесь к API НБУ (описание API - https://old.bank.gov.ua/doccatalog/document?id=72819047) с помошью
#   функции, получите текущий курс валют. Функция должна вернуть данные в таком виде:
#
#       "дата создания запроса"
#       1 - "название ввалюты1" -- "курс"
#       2 - "название ввалюты2" -- "курс"
#       3 - "название ввалюты3" -- "курс"
#       ...
#       так все валюты, которые придут
#
# -> *task 2: Запишите полученные данные в файл в таком же виде
# -> **task 3: Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны к этой
#   валюте за указаную дату используя API НБУ. Если на такую дату курса нет - возвращает какойнибудь информативный
#   ответ. Формат ввода пользователем данных - на ваше усмотрение. Реализовать с помощью ООП!
######################################################################################################################
import requests
import json


class Currancy:
    _name = None
    _rate = None
    _date = None
    _cc = None

    def __init__(self, name: str, cc: str, rate: float, date: str):
        if not (isinstance(name, str) and isinstance(cc, str) and
                isinstance(rate, float) and isinstance(date, str)):
            raise TypeError
        self._name = name
        self._rate = rate
        self._date = date
        self._cc = cc

    @property
    def name(self) -> str:
        return self._name

    @property
    def rate(self) -> float:
        return self._rate

    @property
    def date(self) -> str:
        return self._date

    @property
    def cc(self) -> str:
        return self._cc

    def __str__(self):
        string = "+---------------------------+\n"
        string += f"| {self._name}({self._cc})\n"
        string += f"| rate: {self._rate}\n"
        string += f"| date: {self._date}\n"
        string += "+---------------------------+"
        return string


class DataOperating:
    json_filename = None
    txt_filename = None
    _json_data = None
    _cur_list = None
    _data = None

    def __init__(self, json_f: str, txt_f: str, date=None):
        """Конструктор класса, в котором записываються имена файлов для зариси и чтения,
            так же указываеться дата данных с которыми будет проходить работа"""
        if not (isinstance(json_f, str) and isinstance(txt_f, str)):
            raise TypeError
        self.json_filename = json_f
        self.txt_filename = txt_f
        self._loading_json_data(date)                       # загрузка информации с сайта
        self._json_data = self.load_json_as_list()          # создание списка из словарей с данными о валюте
        self._cur_list = self.load_json_as_obj_list()       # создание списка из обьектов с данными о валюте

    def _loading_json_data(self, date) -> None:
        """Функция в которой происходить загрузка информации с сайта и запись
            в файл json_filename"""
        string = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
        if date is not None:
            string += "&date=" + date
        self._data = requests.request("GET", string)
        if self._data.status_code != 200:
            raise Exception("loading failed")
        self.writing_into(self.json_filename, self._data.text)

    def load_json_as_list(self) -> list:
        """Функция, в которой создаеться список из словарей с данными о валюте.
            Загрузка происходит из файла json_filenmae"""
        with open(self.json_filename, "r") as f:
            json_data = json.load(f)
        return json_data

    def load_json_as_obj_list(self) -> list:
        """Функция, в которой создаеться спиок из обьектов тип Currancy"""
        buff_list = []
        for val in self._json_data:
            buff_list.append(Currancy(val["txt"], val["cc"], val["rate"], val["exchangedate"]))
        return buff_list

    def search(self, name) -> Currancy:
        """Функция для поиска подходящего по имени обьекта с валютой"""
        if not isinstance(name, str):
            raise TypeError
        for val in self._cur_list:
            if val.name == name or val.cc == name:
                return val
        raise Exception(f"{name} not found")

    @staticmethod
    def writing_into(filename, info) -> None:
        """Функция для записи в файл"""
        with open(filename, "w") as f:
            f.write(info)

    def __str__(self):
        count = 0
        buff = ""
        for val in self._json_data:
            count += 1
            buff += f"{count} - {val['txt']} -- {val['rate']}\n"
        return buff


def input_processing() -> list:
    name = input(">>> Введите название валюты(либо на укр, либо сокращенно на англ): ")
    date = input(">>> Введите дату(ДД.ММ.ГГГГ): ")
    if "." in date :
        date = date.split(".")
        if len(date) == 3:
            date = date[2] + date[1] + date[0]
            return [date, name]
    raise TypeError("Date is not correct")


def task_1() -> None:
    """ Подключитесь к API НБУ (описание API - https://old.bank.gov.ua/doccatalog/document?id=72819047) с помошью
       функции, получите текущий курс валют"""
    print(" -> task 1:")
    exmpl1 = DataOperating("Files/nbu_content.json", "Files/nbu_curs.txt")
    print(exmpl1)


def task_2() -> None:
    """Запишите полученные данные в файл в таком же виде"""
    exmpl2 = DataOperating("Files/nbu_content.json", "Files/nbu_curs.txt")
    exmpl2.writing_into("Files/nbu_content.json", str(exmpl2))


def task_3() -> None:
    """Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны к этой
       валюте за указаную дату используя API НБУ. Если на такую дату курса нет - возвращает какойнибудь информативный
       ответ. Формат ввода пользователем данных - на ваше усмотрение. Реализовать с помощью ООП!"""
    print(" -> task 3:")
    lst = input_processing()
    exmpl3 = DataOperating("Files/nbu_content.json", "Files/nbu_curs.txt", lst[0])
    check_list = exmpl3.load_json_as_list()
    if len(check_list) == 0:
        raise Exception(f"No information for such date({lst[0]})")
    var = exmpl3.search(lst[1])
    print("\n" + str(var))


task_1()
task_2()
task_3()

