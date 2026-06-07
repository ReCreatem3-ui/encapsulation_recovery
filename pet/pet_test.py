from pet import Pet
import sys
import time
import os


class Spacer:
    """Utility class to print spacer lines."""

    @staticmethod
    def equal_spacer(count=175):
        return "=" * count

    @staticmethod
    def dash_spacer(count=175):
        return "-" * count

    @staticmethod
    def one_line_spacer():
        print()

    @staticmethod
    def small_spacer():
        for i in range(3):
            print()

    @staticmethod
    def screen_clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def low_bar_divider(count=86):
        return "  " + "▄" * count

    @staticmethod
    def high_bar_divider(count=86):
        return "  " + "▀" * count


class Effects:
    """Utility class to print various effects."""

    @staticmethod
    def slowtype(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

def title():
    return("""
                                                         ██████╗ ███████╗████████╗     ██████╗ █████╗ ██████╗ ███████╗
                                                         ██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝
                                                         ██████╔╝█████╗     ██║       ██║     ███████║██████╔╝█████╗  
                                                         ██╔═══╝ ██╔══╝     ██║       ██║     ██╔══██║██╔══██╗██╔══╝  
                                                         ██║     ███████╗   ██║       ╚██████╗██║  ██║██║  ██║███████╗
                                                         ╚═╝     ╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
""")

def ascii_pet(animal_type):
    """Return ASCII art based on pet type."""
    ascii_map = {
        "Cat": r"""
                                                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣷⣄⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⢀⣤⡤⣀⡀⠀⠀⠀⣀⢷⠊⢁⢻⣆⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠸⣤⡚⠃⢪⠓⠊⠉⠀⠀⠈⠀⠹⡿⡀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠈⡿⢴⡐⠁⠀⠀⠀⠀⠀⢀⣠⣄⡀⠑⣄⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⢹⢻⠀⢀⣤⣤⡀⠀⠀⠛⠿⠟⠀⠀⠈⢲⠄
                                                                            ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠻⠾⠟⠃⠰⣶⣀⠴⠀⠀⠀⠀⣨⠃
                                                                            ⠀⠀⠀⠀⠀⠀⢜⡀⠀⠀⠀⠀⠀⠘⠯⠼⠀⠀⢀⡠⢺⣅⠀
                                                                            ⠀⠀⠀⠀⠀⠀⠈⢳⣤⠄⡀⠀⢀⣀⠀⠀⠀⠞⠁⠀⠀⢳⠀
                                                                            ⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁
                                                                            ⠀⣠⠔⠚⢉⠝⡝⠉⠀⠀⠇⠠⡀⠀⠀⠀⠀⠀⠀⠀⣰⢫⠀
                                                                            ⢰⠁⠀⢀⠃⢔⠁⠀⠀⠀⠇⠀⠈⢦⡀⠀⠀⠀⢀⠔⠁⢸⠀
                                                                            ⡗⠀⠀⠈⠀⡈⠀⠀⠀⠀⠀⢀⠀⠀⠑⢄⠀⡠⠂⠀⡆⡘⠀
                                                                            ⢹⡀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⢂⠀⠀⠀⢋⠀⠀⠸⠀⡇⠀
                                                                            ⠀⠙⠦⢤⣄⠀⢂⠀⠀⠀⠀⠀⠈⠆⠀⠀⢸⠀⠀⡸⠋⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠉⠁⠙⠦⢴⠄⣀⡀⢴⣐⣀⠦⠤⠤⠋⠀⠀⠀
""",
        "Dog": r"""
                                                                          ⠀⠀⠀⠀⢀⣠⡤⣀⣀⣠⠤⠤⠤⠤⠤⢤⡠⠐⠛⠒⠲⣄⠀⠀⠀⠀⠀⠀
                                                                          ⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⡀⠀⠀⠀
                                                                          ⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡆⠀⠀
                                                                          ⢸⡀⠀⣀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⢄⠉⢿⠒⠋⠀⠀⠀
                                                                          ⠀⠉⠉⣱⢱⠀⠀⢰⣾⣦⠀⠀⠀⡀⢰⣿⣿⡆⠀⠀⠈⢣⣄⣑⡢⠀⠀⠀
                                                                          ⠀⠀⠸⠥⡇⠀⠀⠈⠛⠋⠸⡚⢒⡇⠀⠉⠉⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠜⠁⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠀⢩⠓⡆⠀⢠⠀⠀⠀⠀⠀⠀⣞⠀⢀⣹⠓⡄⠀⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠀⡳⠤⣙⣖⢸⠀⠀⠀⠀⠀⠀⣿⡥⣝⣡⠤⡞⠀⠀⠀⠀⣠⡀
                                                                          ⠀⠀⠀⠀⡰⠀⠀⠀⢹⣈⡆⠀⠀⠀⠀⢰⢯⣤⠇⠀⠀⠘⡄⢀⡶⡴⠁⢷
                                                                          ⠀⠀⠀⠀⡇⠀⠀⡔⠀⠉⡇⠀⠀⠀⠀⢸⠀⠀⠀⡆⠀⠀⢷⠞⠀⠀⠀⣸
                                                                          ⠀⠀⠀⠠⣇⣀⡤⠃⠀⢀⠃⠀⠀⠀⠀⢸⠀⠀⠀⠸⢄⢀⣸⠀⠀⠀⣰⠃
                                                                          ⠀⠀⠀⠀⣸⣍⠀⠀⠀⢸⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠈⣹⣧⡤⠔⠋⠁⠀
                                                                          ⠀⠀⠀⠀⠛⠺⡽⣯⣶⡇⢀⣀⣀⣀⣀⣀⣳⣶⣉⣿⣽⠷⠛⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠀⠀⣇⡄⡀⣰⠉⠀⠀⠀⠀⠀⠹⡀⠀⣄⡏⠀⠀⠀⠀⠀⠀⠀
                                                                          ⠀⠀⠀⠀⠀⠀⠈⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
""",
        "Bird": r"""
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠶⠶⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢟⣹⡮⡦⢀⣀⢡⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠕⠒⠀⠉⠒⠢⣍⡲⢄⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡃⠀⠀⢀⠀⢰⣷⠈⡎⡶⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠁⠈⠉⠉⢏⠀⠀⠀⠀⡏⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣍⠀⠀⠀⠀⠀⣀⡠⠜⠃⠀⠀⣰⠧⠤⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⢳⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⣀⠴⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠁⠀⠀⠀⠀⠀⠙⠦⣄⠀⠀⠀⣠⠞⠁⠀⣼⣥⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠒⢷⡒⠢⡜⢁⣴⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⢠⣇⢀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡗⢢⠤⠤⠤⠤⢤⠤⡤⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢡⠃⠀⠀⠀⢀⡞⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣔⣊⣁⡎⠀⠀⣤⣔⣊⣀⡧⠀⠀⠀⠀⠀⠀
""",
        "Fish": r"""
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⢻⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⡄⠀⢠⡞⠁⠀⢼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⠹⣶⠏⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣯⠁⠉⠀⠀⠀⠀⢾⠗⠛⣛⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠴⠿⠛⣦⣤⣀⣀⠀⠀⠀⠀⣴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⢀⡤⠶⠋⠁⠀⠀⠀⠀⠀⢹⣆⣰⣽⡗⢲⣬⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⢀⣴⠋⠀⠀⣠⡴⠶⠶⣄⠀⠀⠈⣯⠉⢳⡀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⢀⣴⣿⣤⡀⠀⣸⡇⠀⢲⠀⠘⣧⠀⠀⢽⡆⢀⡟⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⡄
                                                                        ⠀⠙⢻⣷⣿⠀⠸⣧⡀⠀⠀⣰⠇⢀⣤⣾⣿⡿⣦⣤⣤⣶⣦⣾⣿⣧⠀⠀⢀⣠⣶⡿⣿⡿⠿⢿⡏⠁
                                                                        ⠀⠀⠘⣿⢻⡧⣿⢮⡍⠙⠋⣡⣴⡿⢟⣉⣍⣭⣭⣿⣯⣭⠟⢻⡇⠹⣦⠖⣫⠟⠙⣏⢀⡀⣄⣼⠁⠀
                                                                        ⠀⢠⣾⣿⣿⠇⠈⠳⣽⣆⢸⣿⣿⣗⡋⠉⠀⠀⠀⣰⠟⠁⠀⣼⠀⠀⢿⣾⠷⠚⠛⠉⠉⠉⣹⠃⠀⠀
                                                                        ⠀⣿⡿⢿⡿⣄⠀⠀⢻⣿⡆⠈⠛⢯⣙⠛⠲⠄⣼⠃⠀⠀⢰⡏⠀⢀⡿⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀
                                                                        ⠀⢻⣿⠈⠳⣌⡳⢦⣼⣿⣧⠀⠀⢀⡞⢻⣦⣄⣿⠀⠀⢠⡾⢀⣴⢿⠿⡆⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀
                                                                        ⠀⠈⢿⣇⠀⠀⠙⠻⣽⣿⣗⣶⣴⣏⣠⠾⠂⣈⠙⣂⣤⡾⠗⠋⢸⣾⡇⠙⣄⠀⠀⣻⡇⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠈⢿⣆⠀⠀⠀⠀⣿⣿⠉⠉⠙⠛⠛⠛⢯⣉⠉⠀⠀⠀⠀⠘⣿⣷⡀⠈⠳⣄⣽⠃⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠈⢿⣆⠀⠀⢠⣿⣿⡇⠀⡀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠈⢯⣧⡀⢀⡾⠃⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⢘⣿⡄⠀⠛⠋⢿⣿⡶⠛⣆⠀⢠⡦⣤⣀⣳⣄⠀⠀⠀⠀⠈⠳⣷⡟⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⢨⣿⡗⠀⠀⠀⠈⢻⣿⣄⠈⠻⡾⠀⠀⠀⠉⠋⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⣼⡟⠁⠀⠀⠀⠀⠀⠘⢯⡷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
        "Turtle": r"""
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠤⠤⠴⠶⠖⠒⠲⠶⠤⢤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠋⠉⠈⣡⠀⠒⠒⠂⠒⠀⠹⡁⠀⠀⠀⠈⠉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⢹⢛⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠥⠤⠤⠶⠤⢤⣘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣰⠤⠤⡀⣀⣼⡈⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⣠⠔⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠈⠓⢄⠀⠀⠹⣄⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠤⠤⠤⢀⡀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⡤⡄⣘⣦⠀⠀⠀⠀
                                                                ⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠈⠦⡀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠹⣇⠀⠀⠀
                                                                ⠀⡼⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠀⠙⢂⡤⠤⠤⠤⠤⢼⠃⠀⠀⠀⠀⠻⡄⠀⠀
                                                                ⢨⡇⢺⣿⣯⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢿⣇⡀⠀⠀⠀⠀⣧⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⣿⠀⠀
                                                                ⢸⡇⠈⠛⠛⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠘⢿⣾⠟⠁⠀⠀⠀⠀⣱⠤⠦⠀⢀⣏⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⣀⠠⠔⠻⣆⡀
                                                                ⠈⣇⠀⠀⠀⠀⠀⠀⠉⠒⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢐⣆⣀⠀⠀⣼⠉⠐⠒⠒⠒⡒⠒⠊⣁⣀⣤⣵⣄⣈⡷
                                                                ⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠾⠋⠁⠀⠈⠉⠑⠣⡀⠀⠀⠀⠀⣧⡠⠞⠉⠀⠀⠀⣆⠀⠀
                                                                ⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⢴⡏⠀⠀⠀⠀⠀⠀⣸⣠⣌⡷⠲⠶⠿⢿⠶⠒⠁⠀⠀⠀⢿⠀⠀
                                                                ⠀⠀⠀⠀⣾⠀⠉⠉⠒⠒⠒⢲⠖⠒⠒⠒⠓⠋⠉⠁⠀⢰⡇⠀⠀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⢾⡂⠀⠀⠀⠀⠀⣼⠀⠀
                                                                ⠀⠀⠀⠀⠈⠳⠤⠤⣀⣠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣅⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠈⠓⠤⠤⠤⠴⠚⠁⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠂⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
        "Rabbit": r"""
                                                                        ⢠⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⢰⠀⠀⠑⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠸⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                        ⠀⢇⠀⠀⠀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠶⡀⠀⠀
                                                                        ⠀⠈⡄⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠱⠀⠀
                                                                        ⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⡇⠀
                                                                        ⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⢳⠀
                                                                        ⠀⠀⠀⠀⠀⠳⣄⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⣼⠀
                                                                        ⠀⠀⠀⠀⠀⠀⢀⠵⠞⠁⠀⠀⠀⠈⢉⠦⠤⠄⣀⠀⠀⠀⠀⠀⠀⢀⠏⠀
                                                                        ⠀⠀⠀⠀⠀⢰⣏⣽⢳⢇⣀⣀⠤⠒⣁⡀⠀⠀⠀⠉⠒⠺⡒⠢⢤⠎⠀⠀
                                                                        ⠀⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠈⠲⡀⠈⡆⠀
                                                                        ⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠛⢟⠛⠈⢖⢓⡤
                                                                        ⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠉⠁⠀⡆⠀⠈⠣⠀⠈⣦⠇
                                                                        ⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠒⢄⠀⡇⠀⠀⠀⠀⠀⢹⠀
                                                                        ⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠈⣤⠁⠀⠀⠀⠀⠀⢸⠀
                                                                        ⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠀⠒⠁⠀⠀⠀⠀⠀⠀⠇⠀
                                                                        ⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠈⠑⠢⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠔⠋⠀⠀⠀
                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠒⠀⠀⠀⠒⠒⠉⠁⠀⠀⠀⠀⠀⠀
"""
    }
    return ascii_map.get(animal_type)

def manual_center(text, width=175):
    if len(text) >= width:
        return text
    padding = (width - len(text)) // 2
    return ' ' * padding + text

def separator(title_text="", total_width=175):
    """Return a centered separator line with optional title."""
    line_width = 70  # Width of the separator itself
    if title_text:
        pad = (line_width - len(title_text) - 2) // 2
        sep_line = f"{'═' * pad} {title_text} {'═' * pad}"
    else:
        sep_line = "─" * line_width
    
    # Center the entire separator line within total_width
    padding = (total_width - len(sep_line)) // 2
    return f"\n{' ' * padding}{sep_line}"

def animate_stat(label, from_val, to_val, max_val=10, bar_width=10, step_delay=0.3):
    """Animate a stat bar filling or draining."""
    direction = 1 if to_val >= from_val else -1
    for val in range(from_val, to_val + direction, direction):
        filled = round((val / max_val) * bar_width)
        bar = '█' * filled + '░' * (bar_width - filled)
        sys.stdout.write(f'\r  {label}  [{bar}] {val:>2}/{max_val}')
        sys.stdout.flush()
        time.sleep(step_delay)
    print()

class App():
    
    @staticmethod
    def main():
        Spacer.screen_clear()
        print(title())
        time.sleep(0.4)
        input(manual_center("Press Enter to proceed..."))

        # ── Pet Input ─────────────────────────────────────────────
        name = None
        animal_type = None
        age = None

        Spacer.screen_clear()
        print(title())
        Effects.slowtype(separator("Register Your Pet"), delay=0.01)
        Spacer.one_line_spacer()

        # ── Name Input ────────────────────────────────────────────
        while name is None:
            try:
                name_input = input(' ' * 62 + "Pet's Name      : ").strip()
                if not name_input:
                    raise ValueError("Name cannot be empty.")
                name = name_input
            except ValueError as e:
                print(manual_center(f"      {e}"))
                time.sleep(1.5)
                Spacer.screen_clear()
                print(title())
                print(separator("Register Your Pet")) 
                Spacer.one_line_spacer()

        # ── Animal Type Input ─────────────────────────────────────
        while animal_type is None:
            Spacer.screen_clear()
            print(title())
            print(separator("Register Your Pet"))
            Spacer.one_line_spacer()
            print(' ' * 62 + f"Pet's Name      : {name}")
            
            try:
                atype_input = input(' ' * 62 + "Animal Type     : ").strip()
                if not atype_input:
                    raise ValueError("Animal type cannot be empty.")
                atype_input = atype_input.title()
                if atype_input not in Pet.ANIMAL_TYPES:
                    raise ValueError(f"Animal type must be one of: {', '.join(Pet.ANIMAL_TYPES)}")
                animal_type = atype_input
            except ValueError as e:
                print(manual_center(f"      {e}"))
                time.sleep(1.5)

        # ── Age Input ─────────────────────────────────────────────
        while age is None:
            Spacer.screen_clear()
            print(title())
            print(separator("Register Your Pet"))
            Spacer.one_line_spacer()
            print(' ' * 62 + f"Pet's Name      : {name}")
            print(' ' * 62 + f"Animal Type     : {animal_type}")
            
            try:
                age_input = input(' ' * 62 + "Age (years)     : ").strip()
                if not age_input:
                    raise ValueError("Age cannot be empty.")
                try:
                    age_value = int(age_input)
                except ValueError:
                    raise ValueError("Age must be a whole number (e.g., 3, 5, 10).")
                if age_value < 0 or age_value > 100:
                    raise ValueError("Age must be between 0 and 100.")
                age = age_value
            except ValueError as e:
                print(manual_center(f"      {e}"))
                time.sleep(1.5)

        my_pet = Pet(name, animal_type, age)
        print(separator())
        time.sleep(0.005)

        # ── Profile Screen ────────────────────────────────────────
        Spacer.screen_clear()
        print(title())
        Effects.slowtype(ascii_pet(my_pet.get_animal_type()), delay=0.001)
        Effects.slowtype(manual_center(f"{my_pet}"), delay=0.01)
        Spacer.one_line_spacer()
        print(manual_center(my_pet.profile_card()))
        Spacer.one_line_spacer()
        time.sleep(1.2)


if __name__ == "__main__":
    App.main()

