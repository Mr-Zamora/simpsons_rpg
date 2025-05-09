"""
simpson_characters.py - Contains the specific Simpson character classes
"""

from simpsons_rpg.base_characters import Simpson

# --- Subclasses (Inheritance) ---
# Represents the "is-a" relationship (e.g., Homer is a Simpson)
class Homer(Simpson):
    """
    Represents Homer Simpson, inheriting from Simpson.
    Corresponds to the Homer class in the UML diagram.
    """
    def __init__(self, name, age, secret):
        """Initializes Homer Simpson."""
        # Inheritance: Call the parent class (Simpson) constructor
        super().__init__(name, age, secret)
        # Association: Homer drinks 0..* DuffBeer
        # This is implemented by holding a list of DuffBeer objects.
        self.drunk_beers = []
        # Association: Homer drives 0 or 1 HomersCar
        # This is implemented by holding a reference to a HomersCar object, or None.
        self.car = None # None indicates 0 (Optional)

    # Overriding the speak method with Homer's unique sound
    # +speak() (Public method, overrides parent)
    def speak(self):
        """Homer's unique speak sound."""
        return "D'oh!"

    # +eat_donuts() (Public method)
    def eat_donuts(self):
        """Homer eats donuts."""
        print(f"{self.name} eats some donuts. Mmm... donuts!")

    # +go_to_work() (Public method)
    # Dependency: This method depends on (uses) a NuclearPlant object.
    # Abstraction: This public method hides the complex internal steps of going to work.
    def go_to_work(self, plant): # Depends on 'plant' object
        """Initiates Homer's work routine, demonstrating abstraction and dependency."""
        print(f"\n{self.name} groans. Time for work at the {plant.name}!")
        # Calling internal/private methods that are part of the abstraction
        self._get_dressed() # Calling a 'private' internal method
        self._drive(self.car) # Calling an internal method that depends on self.car
        self._enter_building(plant) # Calling an internal method that depends on 'plant'
        self._clock_in() # Calling another internal method

    # -_get_dressed() (Private method - internal implementation detail)
    def _get_dressed(self):
        """Internal step: Homer gets dressed."""
        print(f"{self.name} puts on his white shirt and pants.")

    # -_drive(car) (Private method with dependency on car)
    def _drive(self, car):
        """Internal step: Homer drives the car."""
        if car:
            print(f"{self.name} drives the {car} to work.")
        else:
            print(f"{self.name} realizes he has no car and walks instead.")

    def _enter_building(self, building):
        """Internal step: Homer enters a building."""
        print(f"{self.name} enters the {building}.")

    def _clock_in(self):
        """Internal step: Homer clocks in."""
        print(f"{self.name} clocks in for work.")

    # +drink(beer) (Public method with dependency on beer)
    def drink(self, beer):
        """Homer drinks a Duff Beer."""
        self.drunk_beers.append(beer) # Add to the list of drunk beers
        print(f"{self.name} drinks a {beer}. 'Mmmm... {beer.brand}!'")

    # +pay_for_item(item, plant) (Public method with multiple dependencies)
    # Demonstrates dependency chain: Homer depends on plant for money to pay for item
    def pay_for_item(self, item, plant):
        """Homer uses earnings (from plant) to pay for an item."""
        # This method depends on both 'item' and 'plant' objects
        print(f"{self.name} uses money from working at {plant.name} to pay for {item}.")


class Marge(Simpson):
    """
    Represents Marge Simpson, inheriting from Simpson.
    Corresponds to the Marge class in the UML diagram.
    """
    # Overriding the speak method with Marge's unique sound
    def speak(self):
        """Marge's unique speak sound."""
        return "Hmmmm..."


class Bart(Simpson):
    """
    Represents Bart Simpson, inheriting from Simpson.
    Corresponds to the Bart class in the UML diagram.
    """
    def __init__(self, name, age, secret):
        """Initializes Bart Simpson."""
        # Inheritance: Call the parent class constructor
        super().__init__(name, age, secret)
        # Aggregation: Bart owns 0..1 Skateboard
        # This is implemented by holding a reference to a Skateboard object, or None.
        self.skateboard = None # None indicates 0 (Optional)

    # Overriding the speak method with Bart's unique sound
    def speak(self):
        """Bart's unique speak sound."""
        return "Eat my shorts!"

    # +set_skateboard(skateboard) (Public method)
    def set_skateboard(self, skateboard):
        """Sets or removes Bart's skateboard."""
        # This method demonstrates aggregation - Bart "has-a" skateboard
        self.skateboard = skateboard
        if skateboard:
            print(f"{self.name} now has a {skateboard} skateboard!")
        else:
            print(f"{self.name} no longer has a skateboard.")


class Lisa(Simpson):
    """
    Represents Lisa Simpson, inheriting from Simpson.
    Corresponds to the Lisa class in the UML diagram.
    """
    # Overriding the speak method with Lisa's unique sound
    def speak(self):
        """Lisa's unique speak sound."""
        return "I'm going to become President someday!"

    # +play(instrument) (Public method with dependency on instrument)
    def play(self, instrument):
        """Lisa plays an instrument."""
        # This method depends on an 'instrument' object
        print(f"{self.name} plays her {instrument} beautifully.")


class Maggie(Simpson):
    """
    Represents Maggie Simpson, inheriting from Simpson.
    Corresponds to the Maggie class in the UML diagram.
    """
    # Overriding the speak method with Maggie's unique sound
    def speak(self):
        """Maggie's unique speak sound."""
        return "*Pacifier sound*"
