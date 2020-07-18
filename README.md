# PyProjects_Intro
-> **main_1**:

    * task 1: Дано два числа (a=10, b=30). 
        Вывести на экран результат математического взаимодействия (+, -, *, / ) этих чисел.
    * task 2: Создать переменную и записать в нее результат сравнения (<, > , ==, !=) этих чисел.  
        После этого вывести на экран значение полученную переменную.
    * task 3: Создать переменную - результат конкатенации (сложения) строк str1="Hello " и str2="world".
        Вывести на ее экран.
    
-> **main_2**:

    * task 1: Используя переменные a и b сформировать строку "First variable is [тут знаение переменной a],  
        second variable is [тут знаение переменной b]. Their sum is [тут их сумма].
        Переменные получите с помощью input()
    * task 2: Попросить ввести из консоли возраст пользователя.  
        если пользователь ничего не ввел (ввел пустую строку) - вывести “не понимаю”
        если пользователю меньше 7 - вывести “где твои мама и папа?”
        если пользователю меньше 18 - вывести “мы не продаем сигареты несовершеннолетним”
        если пользователю больше 65 - вывести “вы в зоне риска”
        в любом другом случае - вывести “оденьте маску!”

-> **main_3**:

    * task 1: Есть list с данными lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', hw9, 0, 'Lorem Ipsum'],
        Нужно сформировать новый list (lst2), который содержит все строки, которые есть в lst1.
    * task 2: Ввести из консоли строку. Определить количество слов в этой строке,
        которые начинаются на "а" (учтите, что слова могут начинаться с большой буквы).
    * task 3: Вывести пользователю приветствие ('Hello!'). Спросить у пользователя, хочет ли он повторно его
        увидеть этот текст (Y/N)?. Повторять приветствие если пользователь введет Y, завершить выполнение если если
        пользователь введет N, если ответ не Y или N - переспрашивать, пока не введет Y или N.

-> **main_4**:

    * task 1: Доделайте последнее задание из практики (Искусственный интеллект)
    * task 2: Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44,]).
        Написать программу, которая удалит из него все числа, которые меньше 18 и больше 81.
    * task 3:  Написать алгоритм перехода через улицу. Ваш робот стоит на одной стороне улицы и должен попасть
        не другую сторону по пешеходному переходу. Робот может шагать вперед, смотреть по сторонам и вперед.
        Можно описать как угодно, хоть блок-схемой, хоть текстом, главное понятно. Что такое блок-схема
        https://uk.wikipedia.org/wiki/%D0%91%D0%BB%D0%BE%D0%BA-%D1%81%D1%85%D0%B5%D0%BC%D0%B0
    * task 4: Ввести из консоли строку. Найти в строке самое длинное слово, в котором присутствуют подряд
        две согласные буквы. Если в строке присутствует слово с тремя согласными буквами подряд - завершить выполнение.

-> **main_5**:

    * task 1: Написать функцию, принимающую один аргумент. Функция жолджна вывести на экран тип данных этого аргумента
        (type).
    * task 2: Написать функцию, принимающую два аргумента.Если оба аргумента относятся к числовым типам - вернуть их
        произведение, если к строкам - соединить в одну строку и вернуть, если первый строка, а второй нет - вернуть
        словарь, в котором ключ - первый аргумент а значение - второй, в любом другом случае вернуть кортеж из аргументов
    * task 3: Дан словарь продавцов и цен на какой то товар у разных продавцов на hotline: { ‘citrus’: 47.999,
       ‘istudio’ 42.999, ‘moyo’: 49.999, ‘royal-service’: 37.245, ‘buy.ua’: 38.324, ‘g-store’: 37.166, ‘ipartner’: 38.988,
       ‘sota’: 37.720 }.  Написать функцию возвращающую список имен продавцов, чьи цены попадают в определенный диапазон.
       Функция должна принимать словарь, начало и конец диапазона и возвращать список имен.
    * task 4: Пользователь вводит строку произвольной длины. Написать функцию, которая должна вернуть словарь
       следующего содержания: ключ - количество букв в слове, значение - список слов с таким количеством букв.
       Отдельным ключом количество пробелов и знаки препинания
       Например:
       {
       "0": количество пробелов в строке
       "1": list слов из одной буквы
       "2": list слов из двух букв
       "3": list слов из трех букв
       и т.д ...
       "punctuation" : tuple уникальных знаков препинания
       }

-> **main_7**:

    * task 1: Создайте класс "животное". Наполните его данными и методами на свое усмотрение.
    * task 2: Опишите с помощью классов кухонную технику в виде диаграммы
      (пример https://www.intuit.ru/EDI/23_04_17_1/1492899714-28128/tutorial/356/objects/2/files/02_05.gif).
      Продумайте классы, их назначение и взаимосвязи. Реализовать с описанием свойств и методов.
    * Описать все то же с помощью питона.

-> **main_8**:

     * task 1: Модифицируйте класс Dot следующим образом:
       - обеспечьте проверку значений координат (только числа)
       - добавьте метод __str__, который бы отдавал информацию о точке в фрмате "x: 10, y: 20"
     * task 2: Модифицируйте класс Line следующим образом:
       - обеспечьте проверку точек начала и конца (точки начала и конца отрезка не должны совпадать)
       - модифицируйте метод __str__ так чтобы он отдавал информацию в формате
           ("Line with points [информация о точке начала] [информация о точке конца] and length [длина]")
     * task 3: Напишите декоратор, замеряющий время выполнения функции
     * task 4: Модифицируйте декоратор таким образом, чтобы декоратор вместе с ответом функции возвращал строку,
       содержащую информацию о затраченном на выполнение времени. Формат возвращаемого времени
       - H-MM-SS-MS (часы-минуты-секунды-милисекунды)

-> **main_9**:

    * task 1: Допишите класс Unit: добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было
      установить < 0 (например у юнита осталось 5 здоровья а его ударили на 10)
    * task 2: Напишите класс Knight. Реализуйте расчет значения урона для атаки и значения заблокированного
      урона для защиты. Добавьте в атаку рыцаря игнорирование половины защиты врага.
    * task 3: Реализуйте всем классам юнитов в атаке проверку состояния здоровья врага (нельзя атаковать врага,
      у которого здоровье = 0)
    * task 4: Для мага - продумайте механику использования заклинаний. Вероятнее всего заклинание - обьект
      отдельного класса (ООП всетаки))))

-> **main_10**:

    * task 1: Добавьте в класс Unit атрибут, отвечающий за шанс (в процентах) для юнита нанести двойной урон во
        время атаки. Измените метод вычисления урона так, чтобы данная величина учитывалась при выполнении атаки.
        Можно использовать итератор или генератор, который будет возвращать результат обработки шанса (например шанс 0.5
        или 50% и определяет, сработал шанс или нет)
    * task 2: Сделайте класс Stuff, который будет базовым для всех вещей, которые смогут использовать юниты.
        В классе должен быть атрибут(ы), определяющий(е) классы юнитов, которые могут им воспользоваться;
        атрибуты, отвечающие за модификацию параметров юнита, который пользуется этим Stuff-ом
        (атрибуты для health, damage, defence)
    * task 3: Добавьте в класс Unit атрибут, отвечающий за шанс (в процентах) для юнита уклонится от атаки
        противника и метод получения результата (уклонился от атаки или нет) во время атаки. Измените метод вычисления
        учитывалась при выполнении атаки (при уклонении от атаки урон не наносится).
        Также можно использовать итератор\генератор

-> **main_11**:

    * task 1: Интегрируйте Battle в свою игру:
 		+- обеспечьте совместимость с вашими юнитами
 		+- создайте обьекты юнитов, создайте обьект битвы, проведите битву
    * task 2: Доработайте механику сражения и проверки состояния атакуемого юнита

-> **main_12**:

    * task 1: Подключитесь к API НБУ (описание API - https://old.bank.gov.ua/doccatalog/document?id=72819047) с помошью
        функции, получите текущий курс валют. Функция должна вернуть данные в таком виде:

           "дата создания запроса"
           1 - "название ввалюты1" -- "курс"
           2 - "название ввалюты2" -- "курс"
           3 - "название ввалюты3" -- "курс"
           ...
           так все валюты, которые придут

    * task 2: Запишите полученные данные в файл в таком же виде
    * task 3: Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны к этой
       валюте за указаную дату используя API НБУ. Если на такую дату курса нет - возвращает какойнибудь информативный
       ответ. Формат ввода пользователем данных - на ваше усмотрение. Реализовать с помощью ООП!

-> **main_13**:

    * task 1: Создайте репозиторий на GitLab или GitHub. Сохраните туда игру (далее любые изменения игры публикуйте
       с помощью git). Сохраните отдельной веткой (пусть будет HW14) дз по регулярным выражениям
    * task 2: Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB,
       a12345BC) с помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является
       номерным знаком. Если является номерным знаком - возвращает саму строку.
    * task 3: Напишите класс, который выбирает из произвольного текста номерные знаки и возвращает их в виде
       пронумерованного списка