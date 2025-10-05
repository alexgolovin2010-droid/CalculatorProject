import math
import interface

def calc_degrees() -> float:
    """TASK 3: Function for calculating sine/cosine from a degree angle"""

    interface.menu(["sin()", "cos()"])
    choice = interface.input("Выберите действие: ", type=int, options=[1, 2])
    angle = interface.input("Введите угол в градусах: ", type=int)

    match choice:
        case 1:
            return math.sin(angle)
        case 2:
            return math.cos(angle)

