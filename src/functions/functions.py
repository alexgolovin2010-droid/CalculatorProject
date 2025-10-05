from .simple import calc_simple
from .extended import calc_extended
from .degrees import calc_degrees
from .radians import calc_radians

def functions():
    """
    The function returns a dictionary with the function name and the function itself.
    Required to call functions from the main menu of the program
    """

    functions = {
            "Простые операции": calc_simple,
            "Расширенные операции": calc_extended,
            "Тригонометрические действия с градусами": calc_degrees,
            "Тригонометрические действия с радианами": calc_radians
    }

    return functions
