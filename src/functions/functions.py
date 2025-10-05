from .simple import calc_simple
from .extended import calc_extended
from .degrees import calc_degrees
from .radians import calc_radians
from .logic import calc_logic
from .number_systems import menu_number_systems

def functions():
    """
    The function returns a dictionary with the function name and the function itself.
    Required to call functions from the main menu of the program
    """

    functions = {
            "Простые операции": calc_simple,
            "Расширенные операции": calc_extended,
            "Тригонометрические действия с градусами": calc_degrees,
            "Тригонометрические действия с радианами": calc_radians,
            "Логические операции": calc_logic,
            "Перевод чисел в различные СС": menu_number_systems
    }

    return functions
