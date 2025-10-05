import math
import interface

def calc_radians() -> float:
    """TASK 4: Function for calculating sine/cosine from a radian"""

    interface.menu(["sin()", "cos()"])
    choice = interface.input("Выберите действие: ", type=int, options=[1, 2])

    radian = interface.input("Введите угол в радианах: ", type=int)
    angle = math.pi / 6

    match choice:
        case 1:
            return math.sin(angle)
        case 2:
            return math.cos(angle)

