import interface
from localization import loc

def menu_number_systems():
    """Menu for selecting actions with calculus siestas"""

    interface.menu([loc("action_dec_to_bin"), loc("action_dec_to_hex"), loc("action_dec_to_oct")])
    choice = interface.input(loc("action_input"), type=int, options=[1, 2, 3])

    match choice:
        case 1:
            value = calc_10_2()
        case 2:
            value = calc_10_16()
        case 3:
            value = calc_10_8()

    return value[2:]


def calc_10_2():
    """Conversion from base 10 to base 2"""
    a = interface.input(loc("num_input"), type=int)

    return bin(a)

def calc_10_16():
    """Conversion from base 10 to base 16"""
    a = interface.input(loc("num_input"), type=int)

    return hex(a)

def calc_10_8():
    """Conversion from base 10 to base 8"""
    a = interface.input(loc("num_input"), type=int)

    return oct(a)
