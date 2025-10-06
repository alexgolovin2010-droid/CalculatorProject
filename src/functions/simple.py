import interface
import math
from localization import loc

def calc_simple() -> float:
    """Function for simple calculations"""

    a = interface.input(loc("first_num_input"), type=int)
    b = interface.input(loc("second_num_input"), type=int)
    operator = interface.input(loc("operator_input"), type=str, options=['+', '-', '*', '/'])

    res = float(eval(str(a) + operator + str(b)))

    return res
