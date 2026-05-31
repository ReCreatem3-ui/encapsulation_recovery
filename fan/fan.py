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

    # ── Getters ──────────────────────────────────────────────
    def get_speed(self):
        return self.__speed
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    def is_on(self):
        return self.__on
    
    # ── Setters ──────────────────────────────────────────────
    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

    def __str__(self):
        status = "on" if self.__on else "off"
        return (f"Fan [speed={self.__speed}, radius={self.__radius}, "
                f"color={self.__color}, on={status}]")
