import os
import time
from fan import Fan

class Spacer:
    """Utility class to print a spacer line."""
    
    @staticmethod
    def equal_spacer(count = 60):
        return "=" * count

    @staticmethod
    def dash_spacer(count = 60):
        return "-" * count

    @staticmethod
    def one_line_spacer():
        print()
    
    @staticmethod
    def small_spacer():
        for i in range(3):
            print()

    @staticmethod
    def medium_spacer():
        for i in range(5):
            print()

    @staticmethod
    def large_spacer():
        for i in range(10):
            print()

    @staticmethod
    def big_spacer():
        for i in range(20):
            print()

    @staticmethod
    def screen_clear():
        os.system('cls' if os.name == 'nt' else 'clear')

class Effects:
    """Utility class to print various effects"""
    
    @staticmethod
    def slowtype(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

class TestFan:
    """Test program for the Fan class."""
    
    @staticmethod
    def main():
        Spacer.screen_clear()
        Effects.slowtype(Spacer.equal_spacer(), delay=0.005)
        Effects.slowtype("                  THE FAN CLASS — TestFan", delay = 0.02)
        Effects.slowtype(Spacer.equal_spacer(), delay=0.005)

        # ── Fan 1: max speed, radius 10, yellow, ON ──────────────
        Spacer.one_line_spacer()
        Effects.slowtype("Fan 1 (Speed: FAST, Radius: 10, Color: Yellow, On: True)", delay=0.02)
        fan1 = Fan()
        fan1.set_speed(Fan.FAST)
        fan1.set_radius(10)
        fan1.set_color("Yellow")
        fan1.set_on(True)

        Effects.slowtype(f"  Speed  : {fan1.get_speed()}", delay = 0.02), time.sleep(0.67)
        Effects.slowtype(f"  Radius : {fan1.get_radius()}", delay = 0.02), time.sleep(0.67)
        Effects.slowtype(f"  Color  : {fan1.get_color()}", delay = 0.02), time.sleep(0.67)
        Effects.slowtype(f"  On     : {fan1.is_on()}\n", delay = 0.02), time.sleep(2),

        # ── Fan 2: medium speed, radius 5, blue, OFF ─────────────
        Effects.slowtype(Spacer.dash_spacer(), delay=0.005)
        Spacer.one_line_spacer()
        Effects.slowtype("Fan 2 (Speed: MEDIUM, Radius: 5, Color: Blue, On: False)", delay=0.02)
        fan2 = Fan()
        fan2.set_speed(Fan.MEDIUM)
        fan2.set_radius(5)
        fan2.set_color("Blue")
        fan2.set_on(False)

        Effects.slowtype(f"  Speed  : {fan2.get_speed()}", delay = 0.02), time.sleep(0.67)
        Effects.slowtype(f"  Radius : {fan2.get_radius()}", delay = 0.02), time.sleep(0.67)
        Effects.slowtype(f"  Color  : {fan2.get_color()}", delay = 0.02), time.sleep(0.67)
        Effects.slowtype(f"  On     : {fan2.is_on()}\n", delay = 0.02), time.sleep(0.67)
        Effects.slowtype(Spacer.equal_spacer(), delay=0.005)


TestFan.main()