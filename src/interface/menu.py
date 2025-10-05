from .utils import Format

def menu(options=[], numbered=True, start=1) -> None:
    """Function for drawing the menu"""

    if numbered:
        for i, option in enumerate(options, start=start):
            print(Format.Style.bold(i), option, sep=". ")         
    else:
        for option in options:
            print(option)


