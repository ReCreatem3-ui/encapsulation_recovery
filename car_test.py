from car import Car
import sys
import time
import os

try:
    import keyboard
    KEYBOARD_AVAILABLE = True
except ImportError:
    KEYBOARD_AVAILABLE = False

class Spacer:
    """Utility class to print spacer lines."""

    @staticmethod
    def equal_spacer(count=69):
        return "=" * count

    def dash_spacer(count=69):
        return "-" * count

    def one_line_spacer():
        print()

    def small_spacer():
        for i in range(3):
            print()

    def screen_clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def low_bar_divider(count=86):
        return "  " + "▄" * count

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

class Elements:
    """Utility class to print various elements."""

    def title():
        print(Spacer.equal_spacer())
        print("""       _____           _______               ______        __ 
        / ___/__ _____  / ___/ /__ ____ ___   /_  __/__ ___ / /_
        / /__/ _ `/ __/ / /__/ / _ `(_-<(_-<    / / / -_|_-</ __/
        \___/\_,_/_/    \___/_/\_,_/___/___/   /_/  \__/___/\__/ 
    """)
        print(Spacer.equal_spacer())

    def animated_title():
        Effects.slowtype("""       _____           _______               ______        __ 
        / ___/__ _____  / ___/ /__ ____ ___   /_  __/__ ___ / /_
        / /__/ _ `/ __/ / /__/ / _ `(_-<(_-<    / / / -_|_-</ __/
        \___/\_,_/_/    \___/_/\_,_/___/___/   /_/  \__/___/\__/ 
    """, delay=0.0067)

    def ascii_car():
        return ("""
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣀⣤⣴⣖⣈⣉⣁⠀⠀⠀⠀⠀⠀⣀⡉⢩⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⣠⣤⡴⠞⠋⠉⠀⣼⣿⠋⠘⠛⠽⣿⣦⠛⠛⠈⠉⠁⠸⢄⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⢸⠡⡛⠦⢤⣀⡀⡼⣿⠃⠀⠀⠀⠀⠘⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢍⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣸⡲⣧⢀⡀⠈⠙⡙⠷⢤⡄⣀⠀⠀⠀⠘⡿⣷⡀⠀⠀⠀⠀⢀⣤⣤⣶⡾⠿⠛⠫⢅⡒⠠⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠱⡙⣿⠒⢌⢦⢀⡷⠿⣦⣤⡉⡚⢷⣛⣋⣟⡯⢿⣄⡀⣤⡞⠿⠿⢍⣀⠀⠀⠀⠀⠀⠀⠉⠒⠤⡈⠐⠦⣀⠀⠀⠀⠀⠀
                ⠀⠈⣿⣿⣿⢎⠰⣯⣅⡛⠭⣃⠷⢼⣧⣀⡈⠉⡌⠀⠁⠒⠤⡀⠀⠀⠈⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⠉⠂⢄⣉⣲⠶⠥⡝
                ⠀⠀⠸⣿⣿⣿⢦⣡⠈⠉⠃⠶⣩⢐⡊⠍⣋⠀⡇⠀⠀⠀⠀⠀⠁⠂⠄⡀⠀⠀⠈⠓⠦⣄⠀⠀⠀⠀⠀⠀⣼⠛⣦⣷⣇
                ⠀⠀⠀⠙⢟⣻⠨⠗⠫⢒⡤⣀⠀⠈⠛⠳⢆⡭⣗⠢⠤⠄⠀⠤⢀⡀⠀⠈⠑⠢⣀⠀⠀⠈⠙⣦⠔⠋⡲⢀⣼⣿⣿⠟⣴
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠮⢐⠠⢀⠀⠀⠏⢊⣴⠟⠛⢔⠤⡈⠢⡀⠀⠀⠀⠉⠢⢴⣿⡉⢲⢈⣿⡿⡫⠟⣡⣾⠇
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠨⣐⠢⢿⣿⣾⢿⣆⢢⠈⠲⡼⣤⣄⣀⣀⣒⡠⠭⢾⣶⢯⡿⠊⣠⢞⡿⠟⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠚⠸⣿⣻⣯⡆⠆⠀⢹⡔⢛⡹⠿⢬⡿⣿⣻⡕⣁⢔⢝⣵⠟⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡿⣣⢰⠀⢸⢷⡆⠠⠭⢒⡂⠭⠁⠩⣺⢕⠟⠁⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⠇⡘⢀⡼⠈⠙⠓⠶⣤⣄⣉⢀⣿⠿⠊⠀⠀⠀⠀⠀⠀
    """)

    def manual_center(text, width=70):
        if len(text) >= width:
            return text
        padding = (width - len(text)) // 2
        return ' ' * padding + text

    def animate_speed(label, from_speed, to_speed, max_speed=200, step_delay=1.0):
        """Animate a single bar from from_speed to to_speed, 5 km/h per second."""
        bar_width = 30
        direction = 1 if to_speed >= from_speed else -1

        for spd in range(from_speed, to_speed + direction, direction * 5):
            filled = spd // 5
            bar = '▄' * filled + ' ' * (bar_width - filled)
            percent = int((spd / max_speed) * 100)
            sys.stdout.write(f'\r  {label}  [{bar}] {spd:>3} km/h')
            sys.stdout.flush()
            time.sleep(step_delay)
        print()


    def separator(title=""):
        width = 70
        if title:
            pad = (width - len(title) - 2) // 2
            return f"\n{'═' * pad} {title} {'═' * pad}"
        else:
            return "─" * width


    def draw_bar(spd, max_speed=200, label=" ", bar_width=40):
        filled = min(spd // 5, bar_width)
        bar = '▄' * filled + ' ' * (bar_width - filled)
        percent = int((spd / max_speed) * 100)
        line = f'  {label}  [{bar}] {spd:>3} km/h)'
        sys.stdout.write(f'\r{line:<70}') 
        sys.stdout.flush()

def interactive_drive(car):
    """Interactive drive mode — hold W to accelerate, S to brake, Q to quit."""
    if not KEYBOARD_AVAILABLE:
        print(Elements.manual_center("\nKeyboard module not installed.", width=70))
        print(Elements.manual_center("  Run: pip install keyboard", width=70))
        print(Elements.manual_center("  Note: may require admin/root privileges.", width=70))
        return

    Effects.slowtype(Elements.separator("Interactive Drive"), delay=0.01)
    Spacer.one_line_spacer()
    Effects.slowtype(Elements.manual_center("Hold W to accelerate, S to brake, Q to quit", width=70), delay=0.01)
    Spacer.one_line_spacer()

    # Reset speed for interactive session
    while car.get_speed() > 0:
        car.brake()

    try:
        while True:
            if keyboard.is_pressed('q'):
                print(Elements.manual_center("\n\n  Engine off", width=70), end='', flush=True)
                Effects.slowtype("...", delay=0.05)
                time.sleep(1.6)
                break
            elif keyboard.is_pressed('w'):
                warning = car.accelerate()
                if warning:
                    sys.stdout.write(f'\r{warning:<80}')
                    sys.stdout.flush()
                else:
                    Elements.draw_bar(car.get_speed(), label="  Drive")
            elif keyboard.is_pressed('s'):
                warning = car.brake()
                if warning:
                    sys.stdout.write(f'\r{warning:<80}')
                    sys.stdout.flush()
                else:
                    Elements.draw_bar(car.get_speed(), label="  Brake")
            else:
                Elements.draw_bar(car.get_speed(), label="  Drive")

            time.sleep(1.0)
    except KeyboardInterrupt:
        print(Elements.manual_center("Interrupted."))