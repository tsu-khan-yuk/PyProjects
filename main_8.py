#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 09.05.2020
#  -> task 1: Модифицируйте класс Dot следующим образом:
#   - обеспечьте проверку значений координат (только числа)
#   - добавьте метод __str__, который бы отдавал информацию о точке в фрмате "x: 10, y: 20"
# -> task 2: Модифицируйте класс Line следующим образом:
#   - обеспечьте проверку точек начала и конца (точки начала и конца отрезка не должны совпадать)
#   - модифицируйте метод __str__ так чтобы он отдавал информацию в формате
#       ("Line with points [информация о точке начала] [информация о точке конца] and length [длина]")
# -> task 3: Напишите декоратор, замеряющий время выполнения функции
# -> *task 4: Модифицируйте декоратор таким образом, чтобы декоратор вместе с ответом функции возвращал строку,
#   содержащую информацию о затраченном на выполнение времени. Формат возвращаемого времени
#   - H-MM-SS-MS (часы-минуты-секунды-милисекунды)
######################################################################################################################
from datetime import datetime
import time


class Dot:
    _x = None
    _y = None

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self._x = x
            self._y = y
        else:
            raise Exception("Expected float or int type arguments")

    @property
    def x(self) -> "int, float":
        return self._x

    @property
    def y(self) -> "int, float":
        return self._y

    @property
    def coord(self) -> tuple:
        return self._x, self._y

    def __str__(self):
        return f"(x: {self._x}, y: {self._y})"


class Line:
    begin_dot = None
    end_dot = None

    def __init__(self, begin, end):
        if isinstance(begin, Dot) and isinstance(begin, Dot):
            if begin.coord != end.coord:
                self.begin_dot = begin
                self.end_dot = end
            else:
                raise Exception("Expected non-simular dots")
        else:
            raise Exception("Expected Dot type arguments")

    @property
    def begin(self) -> Dot:
        return self.begin_dot

    @property
    def end(self) -> Dot:
        return self.end_dot

    @property
    def length(self) -> float:
        return ((self.begin_dot.x - self.end_dot.x) ** 2 + (self.begin_dot.y - self.end_dot.y) ** 2) ** 0.5

    def __str__(self):
        return f'Line with points {self.begin_dot} {self.end_dot} and length {self.length}'


def time_decor(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        val = func(*args, **kwargs)
        return str(datetime.now() - start_time), val

    return wrapper


@time_decor
def func_(sec) -> int:
    """Функция принимает один аргумент в качестве секунд,
        что примерно должна проработать. Возвращает этот же аргумент"""
    print("\t\tbefore sleep")
    for i in range(0, sec):
        time.sleep(1)
        print(f"\t\twait for {sec - i} secs")
    print("\t\tend of sleep")
    return sec


if __name__ == "__main__":
    print(f"\n -> task 1: Возвращаемая строка обьектом Dot: {Dot(10, 20)}")
    print(f" -> task 2: Возвращаемая строка обьектом Line: {Line(Dot(10, 20), Dot(20, 10))}")
    print(" -> task 3 and 4:\n\tfunction outut {")
    tpl = func_(5)
    print("\t}")
    print(f"Возвращаемое значаение {tpl[1]}, время работы функции {tpl[0]}")
    dot3 = Dot()
