import interface

def menu_number_systems():
    """Menu for selecting actions with calculus siestas"""

    interface.menu(["10CИ -> 2CИ", "10CИ -> 16CИ", "10CИ -> 8CИ"])
    choice = interface.input("Выберите действие: ", type=int, options=[1, 2, 3])

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
    a = interface.input("Введите число: ", type=int)

    return bin(a)

def calc_10_16():
    """Conversion from base 10 to base 16"""
    a = interface.input("Введите число: ", type=int)

    return hex(a)

def calc_10_8():
    """Conversion from base 10 to base 8"""
    a = interface.input("Введите число: ", type=int)

    return oct(a)
