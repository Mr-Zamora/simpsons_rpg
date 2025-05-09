"""
vehicles.py - Contains classes for vehicles and their components in the Simpsons RPG
"""

# Composition Class (Whole)
# Depicted by HomersCar *-- Engine and HomersCar *-- Wheel
class HomersCar:
    """
    Represents Homer's Car.
    Corresponds to the HomersCar class in the UML diagram.
    Composed of Engine and Wheels (the parts).
    """
    def __init__(self, model, color):
        """Initializes Homer's Car."""
        # Attributes: model, color (Public)
        self.model = model
        self.color = color
        
        # Composition: Car has exactly 1 Engine (created here)
        # This is implemented by creating the Engine object within the Car constructor.
        self.engine = Engine("V8") # Create the Engine part
        
        # Composition: Car has exactly 4 Wheels (created here)
        # This is implemented by creating the Wheel objects within the Car constructor.
        self.wheels = [Wheel(16) for _ in range(4)] # Create 4 Wheel parts
        
        # Aggregation: Car has 0..5 occupants
        # This is implemented by holding a list of Simpson objects.
        self.occupants = [] # Start with an empty list
        
        # Association: Car has 0 or 1 driver
        # This is implemented by holding a reference to a Simpson object, or None.
        self.driver = None # None indicates no driver (0)

    # +set_driver(driver) (Public method)
    def set_driver(self, driver):
        """Sets or removes the driver of the car."""
        # This method demonstrates association - Car "has-a" driver
        self.driver = driver
        if driver:
            print(f"{driver.name} is now driving the {self.color} {self.model}.")
        else:
            print(f"The {self.color} {self.model} has no driver.")

    # +add_occupant(occupant) (Public method)
    def add_occupant(self, occupant):
        """Adds an occupant to the car."""
        # This method demonstrates aggregation - Car "has" occupants
        if len(self.occupants) < 5: # Check multiplicity constraint (0..5)
            self.occupants.append(occupant)
            print(f"{occupant.name} gets in the {self.color} {self.model}.")
        else:
            print(f"The {self.color} {self.model} is full! {occupant.name} can't get in.")

    # +remove_occupant(occupant) (Public method)
    def remove_occupant(self, occupant):
        """Removes an occupant from the car."""
        # This method demonstrates aggregation - Car "has" occupants
        if occupant in self.occupants:
            self.occupants.remove(occupant)
            print(f"{occupant.name} gets out of the {self.color} {self.model}.")
        else:
            print(f"{occupant.name} is not in the {self.color} {self.model}.")

    def __str__(self):
        """String representation of the Car, including composed parts."""
        # This method demonstrates composition - Car "is made of" Engine and Wheels
        return (f"{self.color} {self.model} with {self.engine} and "
                f"{len(self.wheels)} {self.wheels[0]}")


# Composition Class (Part in HomersCar composition)
class Engine:
    """
    Represents a Car Engine.
    Corresponds to the Engine class in the UML diagram.
    Part of HomersCar composition.
    """
    def __init__(self, type):
        """Initializes an Engine."""
        # Attribute: type (Public)
        self.type = type
        # No back-reference to Car usually in Composition part - highlights dependency on the whole

    def __str__(self):
        """String representation of Engine."""
        return f"{self.type} Engine"


# Composition Class (Part in HomersCar composition)
class Wheel:
    """
    Represents a Car Wheel.
    Corresponds to the Wheel class in the UML diagram.
    Part of HomersCar composition.
    """
    def __init__(self, size):
        """Initializes a Wheel."""
        # Attribute: size (Public)
        self.size = size
        # No back-reference to Car usually in Composition part - highlights dependency on the whole

    def __str__(self):
        """String representation of Wheel."""
        return f"{self.size}-inch Wheels"
