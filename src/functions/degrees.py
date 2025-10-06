import math
import interface
from localization import loc

def calc_degrees() -> float:
    """TASK 3: Function for calculating sine/cosine from a degree angle"""

    interface.menu(["sin()", "cos()"])
    choice = interface.input(loc("action_input"), type=int, options=[1, 2])
    angle = interface.input(loc("degrees_input"), type=int)

    match choice:
        case 1:
            return math.sin(angle)
        case 2:
            return math.cos(angle)

