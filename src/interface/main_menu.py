from .utils import Format

from .menu import menu

from .input import custom_input
from .output import custom_output

import functions


def main_menu():
    """Function for displaying the main menu of the program"""
    
    print(Format.Style.bold("CalculatorProject"))

    print("Функции:")
    functions_list = functions.functions()

    menu(functions_list, numbered=True, start=1)

    choice = custom_input("Введите номер функции: ", type=int, options=[1])
    functions_list = list(functions_list.items())
    func = functions_list[choice - 1][1]

    res = func()
    custom_output(res)



