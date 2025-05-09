"""
base_characters.py - Contains the base Simpson character class
"""

from simpsons_rpg.interfaces import CanSpeak

class Simpson(CanSpeak):
    """
    Base class for Simpson characters.
    Corresponds to the Simpson class in the UML diagram.
    Inherits from CanSpeak (like 'realizing' the interface).
    """
    def __init__(self, name, age, secret):
        """Initializes a Simpson character with basic attributes."""
        # Attributes: Data that describes an object
        # +String name (Public convention - no special prefix)
        self.name = name
        # +int age (Public convention)
        self.age = age
        # -String _secret (Private convention - using single underscore _ )
        # In Python, a single underscore is a convention meaning "internal use only".
        self._secret = secret # Changed from __secret for simplicity

    # Implementation of the 'speak' method from CanSpeak
    def speak(self):
        """Generic speak method - intended to be overridden."""
        # This method is primarily here to satisfy the interface for the base class.
        # The specific character speaks are in the subclasses.
        return f"Hello from {self.name} (base Simpson)!"

    # Public method to access the "private" attribute
    # +get_secret() (Public method)
    def get_secret(self):
        """Returns the character's secret (accessing a 'private' attribute)."""
        return self._secret # Accessing the _secret attribute

    def __str__(self):
        """Provides a user-friendly string representation of the object."""
        return self.name # Simpler representation for the RPG
