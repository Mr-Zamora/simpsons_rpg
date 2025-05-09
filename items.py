"""
items.py - Contains classes for various items and objects in the Simpsons RPG
"""

# Association Class (Target of Homer's drinks association)
class DuffBeer:
    """
    Represents a Duff Beer.
    Corresponds to the DuffBeer class in the UML diagram.
    """
    def __init__(self, brand):
        """Initializes a Duff Beer."""
        # Attribute: brand (Public)
        self.brand = brand

    def __str__(self):
        """String representation of Duff Beer."""
        return f"Duff {self.brand} Beer"


# Aggregation Class (Part in Bart's owns aggregation)
class Skateboard:
    """
    Represents a Skateboard.
    Corresponds to the Skateboard class in the UML diagram.
    Part in Bart's aggregation.
    """
    def __init__(self, model):
        """Initializes a Skateboard."""
        # Attribute: model (Public)
        self.model = model

    def __str__(self):
        """String representation of Skateboard."""
        return f"{self.model} Skateboard"


# Dependency Class (Homer depends on this for income context)
# Depicted by Homer ..> NuclearPlant in UML
class NuclearPlant:
    """
    Represents the Nuclear Plant.
    Corresponds to the NuclearPlant class in the UML diagram.
    Homer depends on this (uses it for work).
    """
    def __init__(self, name):
        """Initializes the Nuclear Plant."""
        # Attribute: name (Public)
        self.name = name

    def __str__(self):
        """String representation of the Nuclear Plant."""
        return self.name


# Dependency Class (Lisa depends on this to play)
# Depicted by Lisa ..> Saxophone in UML
class Saxophone:
    """
    Represents a Saxophone.
    Corresponds to the Saxophone class in the UML diagram.
    Lisa depends on this (uses it to play).
    """
    def __init__(self, type):
        """Initializes a Saxophone."""
        # Attribute: type (Public)
        self.type = type

    def __str__(self):
        """String representation of Saxophone."""
        return f"{self.type} Saxophone"
