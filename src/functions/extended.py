import math
import interface

def calc_extended() -> float:
    """TASK 2: Function for extended calculations"""

    interface.menu(["Возведение в степень", "Остаток от деления", "Нахождение корня"])
    choice = interface.input("Введите номер действия: ", type=int, options=[1, 2, 3])

    match choice:
        case 1:
            a = interface.input("Введите число: ", type=int)
            b = interface.input("Введите степень: ", type=int)
            
            return a ** b
        case 2:
            a = interface.input("Введите делимое число: ", type=int)
            b = interface.input("Введите делитель: ", type=int, not_equal=0)

            return a % b
        case 3:
            a = interface.input("Введите число: ", type=int)

            return math.sqrt(a)

