from .simple import calc_simple
from .extended import calc_extended

def functions():
    """
    The function returns a dictionary with the function name and the function itself.
    Required to call functions from the main menu of the program
    """

    functions = {
            "Простые операции": calc_simple,
            "Расширенные операции": calc_extended
    }

    return functions
