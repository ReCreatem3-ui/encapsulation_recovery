import time
import sys

class Car:
    """Represents a car with encapsulated year model, make, and speed."""

    MAX_SPEED = 200   # km/h safety cap
    MIN_SPEED = 0
    ACCEL_STEP = 5
    BRAKE_STEP = 5

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # ── Getters ──────────────────────────────────────────────
    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    # ── Setters ──────────────────────────────────────────────
    def set_year_model(self, year):
        if not isinstance(year, int) or year < 1886 or year > 2026:
            raise ValueError("Invalid year model. Must be between 1886 to 2026")
        self.__year_model = year

    def set_make(self, make):
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Make must be a non-empty string.")
        self.__make = make.strip()

    # ── Behaviours ───────────────────────────────────────────
    def accelerate(self):
        if self.__speed < Car.MAX_SPEED:
            self.__speed = min(self.__speed + Car.ACCEL_STEP, Car.MAX_SPEED)
            return None
        else:
            return f"  ⚠  Already at maximum speed ({Car.MAX_SPEED} km/h)!"

    def brake(self):
        if self.__speed > Car.MIN_SPEED:
            self.__speed = max(self.__speed - Car.BRAKE_STEP, Car.MIN_SPEED)
            return None
        else:
            return "  ⚠  Car is already fully stopped!"

    def speedometer(self):
        """Animate a speedometer bar filling up to current speed."""
        total_blocks = 20
        target = int((self.__speed / Car.MAX_SPEED) * total_blocks)
        
        for i in range(target + 1):
            bar = '▄' * i + ' ' * (total_blocks - i)
            percent = int((i / total_blocks) * 100)
            sys.stdout.write(f'\r  [{bar}] {self.__speed} km/h ({percent}%)')
            sys.stdout.flush()
            time.sleep(0.05)
            print()

    def __str__(self):
        return (f"{self.__year_model} {self.__make}")
