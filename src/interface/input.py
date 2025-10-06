from .utils import Format
from localization import loc

def custom_input(prompt: str, type=None, options=[], not_equal=None):
    """Custom input function for project"""

    while True:
        value = input(prompt)
        
        if type != None:
            try:
                value = type(value)
            except ValueError:
                print(Format.Style.bold(Format.Color.red(loc("error")) + loc("invalid_format")))
                continue
    
        if options != []:
            if value not in options:
                print((Format.Style.bold(Format.Color.red(loc("error"))) + loc("invalid_option") + ' '.join(map(str, options))))
                continue
        
        if value == not_equal:
            print((Format.Style.bold(Format.Color.red(loc("error"))) + loc("invalid_choice")))
            continue

        return value

