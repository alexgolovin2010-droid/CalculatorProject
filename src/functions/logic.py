import interface

def calc_logic() -> bool:
    """TASK 5: Function for logical calculations"""
    interface.menu(["and", "or", "not"])
    choice = interface.input("Выберите действие: ", type=int, options=[1, 2, 3])

    match choice:
        case 1:
            a = interface.input("Введите первое число: ", type=bool)
            b = interface.input("Введите второе число: ", type=bool)

            return (a and b)
        case 2:
            a = interface.input("Введите первое число: ", type=bool)
            b = interface.input("Введите второе число: ", type=bool)

            return (a or b)
        case 3:
            a = interface.input("Введите число: ", type=bool)
            return (not a)


