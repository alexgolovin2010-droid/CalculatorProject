class Format:
    """Class with helper functions for formating text"""

    class Style:
        """Class with functions for changing style"""

        @staticmethod
        def bold(text: str) -> str:
            """Function for create bold text"""
            res = "\033[1m{}\033[0m".format(text)
            return res

        @staticmethod
        def italic(text: str) -> str:
            """Function for create italic text"""
            res = "\033[3m{}\033[0m".format(text)
            return res

        @staticmethod
        def underline(text: str) -> str:
            """Function for create underlined text"""
            res = "\033[4m{}\033[0m".format(text)
            return res      
    
    class Color:
        @staticmethod
        def black(text: str) -> str:
            """Function for create black text"""
            res = "\033[30m{}\033[0m".format(text)
            return res

        @staticmethod
        def red(text: str) -> str:
            """Function for create red text"""
            res = "\033[31m{}\033[0m".format(text)
            return res

        @staticmethod
        def green(text: str) -> str:
            """Function for create green text"""
            res = "\033[32m{}\033[0m".format(text)
            return res

        @staticmethod
        def yellow(text: str) -> str:
            """Function for create yellow text"""
            res = "\033[33m{}\033[0m".format(text)
            return res

        @staticmethod
        def blue(text: str) -> str:
            """Function for create blue text"""
            res = "\033[34m{}\033[0m".format(text)
            return res

        @staticmethod
        def purple(text: str) -> str:
            """Function for create purple text"""
            res = "\033[35m{}\033[0m".format(text)
            return res

        @staticmethod
        def aqua(text: str) -> str:
            """Function for create aqua text"""
            res = "\033[36m{}\033[0m".format(text)
            return res

        @staticmethod
        def white(text: str) -> str:
            """Function for create white text"""
            res = "\033[37m{}\033[0m".format(text)
            return res

    class Background:
        @staticmethod
        def black(text: str) -> str:
            """Function for create black background"""
            res = "\033[40m{}\033[0m".format(text)
            return res

        @staticmethod
        def red(text: str) -> str:
            """Function for create red background"""
            res = f"\033[41m{text}\033[0m"
            return res

        @staticmethod
        def green(text: str) -> str:
            """Function for create green background"""
            res = "\033[42m{}\033[0m".format(text)
            return res

        @staticmethod
        def yellow(text: str) -> str:
            """Function for create yellow background"""
            res = "\033[43m{}\033[0m".format(text)
            return res

        @staticmethod
        def blue(text: str) -> str:
            """Function for create blue background"""
            res = "\033[44m{}\033[0m".format(text)
            return res

        @staticmethod
        def purple(text: str) -> str:
            """Function for create purple background"""
            res = "\033[45m{}\033[0m".format(text)
            return res

        @staticmethod
        def aqua(text: str) -> str:
            """Function for create aqua background"""
            res = "\033[46m{}\033[0m".format(text)
            return res

        @staticmethod
        def white(text: str) -> str:
            """Function for create white background"""
            res = "\033[47m{}\033[0m".format(text)
            return res
