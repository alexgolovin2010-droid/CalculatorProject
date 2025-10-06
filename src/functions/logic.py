import interface
from localization import loc

def calc_logic() -> bool:
    """TASK 5: Function for logical calculations"""
    interface.menu(["and", "or", "not"])
    choice = interface.input(loc("action_input"), type=int, options=[1, 2, 3])

    match choice:
        case 1:
            a = interface.input(loc("first_num_input"), type=bool)
            b = interface.input(loc("second_num_input"), type=bool)

            return (a and b)
        case 2:
            a = interface.input(loc("first_num_input"), type=bool)
            b = interface.input(loc("second_num_input"), type=bool)

            return (a or b)
        case 3:
            a = interface.input(loc("num_input"), type=bool)
            return (not a)


