import time 
import sys

class Car:
    """Represents a car wtih encapsulated year model, car name (make), and speed"""

    MAX_SPEED = 200  #km/h safety cap
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
        if not isinstance(year, int) or year < 1886:
            raise ValueError("Invalid year model. Cars were invented in 1886")
        self.__year_model = year

    def set_make(self, make):
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Please input a car model name as a non-empty string.")
        self.__make = make
    
    # ── Behaviours ───────────────────────────────────────────
    def accelerate(self):
        if self.__speed < Car.MAX_SPEED:
            self.__speed = min(self.__speed + Car.ACCEL_STEP, Car.MAX_SPEED)
        else:
            print(f"  ⚠  Already at maximum speed ({Car.MAX_SPEED} km/h)!")

    def brake(self):
        if self.__speed > Car.MIN_SPEED:
            self.__speed = max(self.__speed - Car.BRAKE_STEP, Car.MIN_SPEED)
        else:
            print("  ⚠  Car is already fully stopped!")

    def speedometer(self):
        """Animate a speedometer bar filling up to current speed."""
        bar_width = 30
        filled = self.__speed // 5
        bar = '▄' * filled + ' ' * (bar_width - filled)
        percent = int((self.__speed / Car.MAX_SPEED) * 100)
        print(f'  Speedometer: [{bar}] {self.__speed} km/h ({percent}%)')
    print()

    def __str__(self):
        return f"{self.__year_model}{self.__make}"