from .utils import Format

def custom_input(prompt: str, type=None, options=[]):
    """Custom input function for project"""

    while True:
        value = input(prompt)
        
        if type != None:
            try:
                value = type(value)
            except ValueError:
                print(Format.Style.bold(Format.Color.red("ОШИБКА: ")) + "Неверный формат ввода")
                continue
    
        if options != []:
            if value not in options:
                print(Format.Style.bold(Format.Color.red("ОШИБКА: ")) + "Выберите один из допустимых вариантов: " + str(*options))
                continue
        
        return value

