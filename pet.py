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

