import math
import interface
from localization import loc

def calc_extended() -> float:
    """TASK 2: Function for extended calculations"""

    interface.menu([loc("action_exponentiation"), loc("action_modulo"), loc("action_sqrt")])
    choice = interface.input(loc("action_input"), type=int, options=[1, 2, 3])

    match choice:
        case 1:
            a = interface.input(loc("num_input"), type=int)
            b = interface.input(loc("pow_input"), type=int)
            
            return a ** b
        case 2:
            a = interface.input(loc("input_devisible_num"), type=int)
            b = interface.input(loc("input_divider"), type=int, not_equal=0)

            return a % b
        case 3:
            a = interface.input(loc("num_input"), type=int)

            return math.sqrt(a)

