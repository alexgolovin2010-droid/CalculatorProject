from .simple import calc_simple
from .extended import calc_extended
from .degrees import calc_degrees
from .radians import calc_radians
from .logic import calc_logic
from .number_systems import menu_number_systems
from .about import about
from localization import loc

def functions():
    """
    The function returns a dictionary with the function name and the function itself.
    Required to call functions from the main menu of the program
    """

    functions = {
            loc("calc_simple"): calc_simple,
            loc("calc_extended"): calc_extended,
            loc("calc_degrees"): calc_degrees,
            loc("calc_radians"): calc_radians,
            loc("calc_logic"): calc_logic,
            loc("menu_number_systems"): menu_number_systems,
            loc("about_page"): about
    }

    return functions
