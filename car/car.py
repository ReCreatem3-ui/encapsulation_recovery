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

    def __str__(self):
        return f"{self.__year_model}{self.__make}"