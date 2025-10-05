import interface
import math

def calc_simple() -> float:
    """Function for simple calculations"""

    a = interface.input("Введите первое число: ", type=int)
    b = interface.input("Введите второе число: ", type=int)
    operator = interface.input("Введите оператор: ", type=str, options=['+', '-', '*', '/'])

    res = float(eval(str(a) + operator + str(b)))

    return res
