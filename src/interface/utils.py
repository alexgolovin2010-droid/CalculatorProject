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
            res = "\033[30{}\033[0m".format(text)
            return res

        @staticmethod
        def red(text: str) -> str:
            """Function for create red text"""
            res = "\033[32{}\033[0m".format(text)
            return res

        @staticmethod
        def green(text: str) -> str:
            """Function for create green text"""
            res = "\033[32{}\033[0m".format(text)
            return res

        @staticmethod
        def yellow(text: str) -> str:
            """Function for create yellow text"""
            res = "\033[33{}\033[0m".format(text)
            return res

        @staticmethod
        def blue(text: str) -> str:
            """Function for create blue text"""
            res = "\033[34{}\033[0m".format(text)
            return res

        @staticmethod
        def purple(text: str) -> str:
            """Function for create purple text"""
            res = "\033[35{}\033[0m".format(text)
            return res

        @staticmethod
        def aqua(text: str) -> str:
            """Function for create aqua text"""
            res = "\033[36{}\033[0m".format(text)
            return res

        @staticmethod
        def white(text: str) -> str:
            """Function for create white text"""
            res = "\033[37{}\033[0m".format(text)
            return res

    class Background:
        @staticmethod
        def black(text: str) -> str:
            """Function for create black background"""
            res = "\033[40{}\033[0m".format(text)
            return res

        @staticmethod
        def red(text: str) -> str:
            """Function for create red background"""
            res = "\033[41{}\033[0m".format(text)
            return res

        @staticmethod
        def green(text: str) -> str:
            """Function for create green background"""
            res = "\033[42{}\033[0m".format(text)
            return res

        @staticmethod
        def yellow(text: str) -> str:
            """Function for create yellow background"""
            res = "\033[43{}\033[0m".format(text)
            return res

        @staticmethod
        def blue(text: str) -> str:
            """Function for create blue background"""
            res = "\033[44{}\033[0m".format(text)
            return res

        @staticmethod
        def purple(text: str) -> str:
            """Function for create purple background"""
            res = "\033[45{}\033[0m".format(text)
            return res

        @staticmethod
        def aqua(text: str) -> str:
            """Function for create aqua background"""
            res = "\033[46{}\033[0m".format(text)
            return res

        @staticmethod
        def white(text: str) -> str:
            """Function for create white background"""
            res = "\033[47{}\033[0m".format(text)
            return res
