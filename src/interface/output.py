from .utils import Format
from localization import loc

def custom_output(text: str) -> None:
    """Custom output function for project"""
    print(Format.Style.bold(Format.Color.green(loc("output_result"))) + str(text))
