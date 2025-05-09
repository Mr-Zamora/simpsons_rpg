"""
interfaces.py - Contains interface-like classes for the Simpsons RPG
"""

class CanSpeak:
    """
    Represents the ability to speak.
    A class inheriting from this should implement the 'speak' method.
    (Simpler version of the <<interface>> CanSpeak in UML)
    """
    def speak(self):
        """
        Placeholder method - subclasses should provide their own speaking behavior.
        """
        raise NotImplementedError("Subclass must implement abstract method")
