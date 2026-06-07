class Pet:
    """Represents a pet with encapsulated name, animal type, age, hunger, and happiness."""

    ANIMAL_TYPES = ["Cat", "Dog", "Bird", "Fish", "Rabbit", "Turtle"]

    MAX_HUNGER = 10
    MAX_HAPPINESS = 10

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        self.__hunger = 5  # 0 = full | 10 = starving
        self.__happiness = 5  # 0 = sad | 10 = happy

    # ── Getters ──────────────────────────────────────────────
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
    def get_hunger(self):
        return self.__hunger
    
    def get_happiness(self):
        return self.__happiness
    
    # ── Setters ──────────────────────────────────────────────
    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Please input a pet name")
        self.__name = name.strip().title()

    def set_animal_type(self, animal_type):
        if not isinstance(animal_type, str) or not animal_type.strip():
            raise ValueError("Invalid animal type. Please choose from: " + ", ".join(Pet.ANIMAL_TYPES))
        animal_type = animal_type.strip().title()
    
    def set_age(self, age):
        try:
            age = int(age)
        except (ValueError, TypeError):
            raise ValueError("Age must be a whole number.")
        if age < 0 or age > 100:
            raise ValueError("Age must be between 0 and 100.")
        self.__age = age
    
    def set_age(self, age):
        try:
            age = int(age)
        except (ValueError, TypeError):
            raise ValueError("Age must be a whole number.")
        if age < 0 or age > 100:
            raise ValueError("Age must be between 0 and 100.")
        self.__age = age

    # ── Behaviours ───────────────────────────────────────────
    def feed(self):
        """Decrease hunger by 2 (min 0). Returns a status message."""
        if self.__hunger == 0:
            return f"  {self.__name} is already full and turns away!"
        self.__hunger = max(0, self.__hunger - 2)
        if self.__hunger == 0:
            return f"  {self.__name} gobbled everything up. Tummy full! "
        return f"  {self.__name} munches happily. Hunger: {self.__hunger}/{self.MAX_HUNGER}"

    def play(self):
        """Increase happiness by 2 (max 10). Returns a status message."""
        if self.__happiness == self.MAX_HAPPINESS:
            return f"  {self.__name} is already bursting with joy!"
        self.__happiness = min(self.MAX_HAPPINESS, self.__happiness + 2)
        if self.__happiness == self.MAX_HAPPINESS:
            return f"  {self.__name} is having the time of their life! "
        return f"  {self.__name} plays eagerly. Happiness: {self.__happiness}/{self.MAX_HAPPINESS}"
    
    # ── Display helpers ───────────────────────────────────────
    def _stat_bar(self, value, max_val=10, width=10):
        """Generate a stat bar with filled and empty blocks."""
        filled = round((value / max_val) * width)
        return '█' * filled + '░' * (width - filled)
    
    def profile_card(self):
        """Return a simple formatted profile card for the pet."""
        name = self.get_name() or "Unknown"
        atype = self.get_animal_type() or "Unknown"
        age = f"{self.get_age()} year(s)" if self.get_age() is not None else "Unknown"

        fullness = Pet.MAX_HUNGER - self.get_hunger()
        happiness = self.get_happiness()

        hunger_bar = self._stat_bar(fullness)
        happiness_bar = self._stat_bar(happiness)

        return (
            f"\n{'=' * 50}\n"
            f"            PET PROFILE CARD\n"
            f"{'-' * 50}\n"
            f"  Name        : {name}\n"
            f"  Animal Type : {atype}\n"
            f"  Age         : {age}\n"
            f"{'-' * 50}\n"
            f"  Fullness    : [{hunger_bar}] {fullness}/10\n"
            f"  Happiness   : [{happiness_bar}] {happiness}/10\n"
            f"{'=' * 50}\n"
        )

    def __str__(self):
        return f"{self.__age} year old {self.__animal_type}: {self.__name}"

