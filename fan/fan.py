class Fan:
    """Represents an electric fan with encapsulated attributes."""
    # Class constants for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=None, radius=5.0, color="blue", on=False):
        if speed is None:
            speed = Fan.SLOW
            self.__speed = speed
            self.__radius = radius
            self.__color = color
            self.__on = on

