import json
import os
from interface import utils

def load_config() -> dict:
    """Function for opening config file"""
    with open("config.json", encoding="utf-8") as file:
        data = json.load(file)

    return data

def load_strings() -> dict:
    """Function for opening localization file"""
    with open("localization/locale.json", encoding="utf-8") as file:
        data = json.load(file)

    return data



LANGUAGE = load_config()["lang"]



strings = load_strings()

def get_string(key: str, lang: str = LANGUAGE) -> str:
    """Function for localization"""
    try:
        return strings[LANGUAGE][key]
    except KeyError:
        return utils.Format.Style.bold(utils.Format.Color.red("Unknown"))

