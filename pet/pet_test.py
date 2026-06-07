from pet import Pet
import sys
import time
import os


class Spacer:
    """Utility class to print spacer lines."""

    @staticmethod
    def equal_spacer(count=69):
        return "=" * count

    @staticmethod
    def dash_spacer(count=69):
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