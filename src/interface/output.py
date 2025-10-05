from .utils import Format

def custom_output(text: str) -> None:
    """Custom output function for project"""
    print(Format.Style.bold(Format.Color.green("Результат: ")) + str(text))
