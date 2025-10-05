from .utils import Format

def custom_output(text: str) -> None:
    print(Format.Style.bold(Format.Color.green("Результат: ")) + str(text))
