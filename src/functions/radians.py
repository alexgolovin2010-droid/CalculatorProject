import math
import interface
from localization import loc

def calc_radians() -> float:
    """TASK 4: Function for calculating sine/cosine from a radian"""

    interface.menu(["sin()", "cos()"])
    choice = interface.input(loc("action_input"), type=int, options=[1, 2])

    radian = interface.input(loc("radians_input"), type=int)
    angle = math.pi / 6

    match choice:
        case 1:
            return math.sin(angle)
        case 2:
            return math.cos(angle)

