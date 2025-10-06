from localization import loc
from interface import utils

def about() -> None:
    text = utils.Format.Style.bold(loc("about_page")) + '\n' + loc("text_about_page")
    
    print(text)

    return None

