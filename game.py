"""
game.py - Main game file for the Simpsons RPG
Contains the game logic and interactive elements
"""

import time
from simpsons_rpg.simpson_characters import Homer, Marge, Bart, Lisa, Maggie
from simpsons_rpg.items import DuffBeer, Skateboard, NuclearPlant, Saxophone
from simpsons_rpg.vehicles import HomersCar
from simpsons_rpg.family import Family

# --- Helper Function for RPG Interaction ---
def wait_for_player(message="Press Enter to continue..."):
    """Pauses the game and waits for the player to press Enter."""
    input(message)

# --- Main Game Function ---
def run_game():
    """Runs the main Simpsons RPG game."""
    print("--- The Simpsons: A Simple RPG Day in Springfield ---")
    print("Based on the UML Class Diagram")

    wait_for_player("Press Enter to start...")

    # --- 1. Object Creation ---
    print("\n--- Creating Characters and Objects ---")
    
    # Create Simpson characters (instances of the subclasses)
    homer = Homer("Homer", 39, "I love donuts more than Marge")
    marge = Marge("Marge", 36, "I once almost had an affair")
    bart = Bart("Bart", 10, "I'm actually a good student but hide it")
    lisa = Lisa("Lisa", 8, "I sometimes wish I wasn't so smart")
    maggie = Maggie("Maggie", 1, "I shot Mr. Burns")
    
    # Create other objects
    plant = NuclearPlant("Springfield Nuclear Power Plant")
    duff = DuffBeer("Regular")
    skate = Skateboard("Thrashmaster 3000")
    sax = Saxophone("Baritone")
    h_car = HomersCar("Sedan", "Pink")
    
    # Create the family object
    simpsons_family = Family("Simpson")
    
    print("Characters and objects created!")
    wait_for_player()
    
    # --- 2. Establishing Relationships ---
    print("\n--- Establishing Relationships ---")
    
    # Family Aggregation: Adding members to the Family object
    simpsons_family.add_member(homer)
    simpsons_family.add_member(marge)
    simpsons_family.add_member(bart)
    simpsons_family.add_member(lisa)
    simpsons_family.add_member(maggie)
    
    # Bart's Skateboard Aggregation: Setting the skateboard object for Bart
    bart.set_skateboard(skate)
    
    # Homer's Car Association: Setting the car for Homer
    homer.car = h_car
    h_car.set_driver(homer)
    
    print("\n--- Morning in Springfield ---")

    # Characters Speak (Inheritance, Realization)
    print(f"{homer.name}: {homer.speak()}")
    print(f"{lisa.name}: {lisa.speak()}")
    print(f"{bart.name}: {bart.speak()}")
    print(f"{marge.name}: {marge.speak()}")
    print(f"{maggie.name}: {maggie.speak()}")

    wait_for_player()

    # Homer goes to work (Dependency on Plant, Abstraction)
    print(f"\nTime for work!")
    homer.go_to_work(plant) # This method call includes driving the car and entering the plant

    wait_for_player()

    # Lisa plays (Dependency on Saxophone)
    print(f"\nLisa feels musical.")
    lisa.play(sax) # Depends on 'sax' object

    wait_for_player()

    # Homer pays for items (Dependency chain: Item -> Homer -> Plant)
    # This method call demonstrates dependencies on 'item' and 'plant'
    print(f"\nUh oh, bills are due!")
    homer.pay_for_item(bart.skateboard, plant) # Skateboard depends on Homer, Homer depends on Plant
    homer.pay_for_item(sax, plant)             # Saxophone depends on Homer, Homer depends on Plant

    wait_for_player()

    # --- Evening Actions with a Choice ---
    print(f"\n--- Evening ---")

    # Simple Choice 1: What does Homer do after work? (Relates to Homer's methods/associations)
    print("Homer is home from work. What does he do?")
    print("1. Drink a Duff Beer")
    print("2. Eat some donuts")

    choice1 = input("Enter choice (1 or 2): ")

    if choice1 == '1':
        homer.drink(duff) # Calls the drink method (Association with DuffBeer)
    elif choice1 == '2':
        homer.eat_donuts() # Calls the eat_donuts method
    else:
        print("Homer just sighs and sits on the couch.") # Default action

    wait_for_player()

    # --- Family Car Ride ---
    print("\nTime for a family outing!")
    # Homer is already linked to the car as the driver via association established earlier.

    # Aggregation (Carries Occupants), Multiplicity 1..5 with a simple choice
    print(f"{homer.name} is in the car.")
    remaining_family = [marge, bart, lisa, maggie]
    available_seats = 5 - 1 # 5 total, Homer is one

    print(f"There are {available_seats} spots left. Who gets in first?")
    for i, member in enumerate(remaining_family):
        print(f"{i + 1}. {member.name}")

    # Simple Choice 2: Choose one other family member to get in first
    chosen_index = input(f"Enter choice (1 to {len(remaining_family)}): ")

    try:
        chosen_index = int(chosen_index) - 1
        if 0 <= chosen_index < len(remaining_family):
            chosen_member = remaining_family.pop(chosen_index) # Remove chosen from remaining list
            h_car.add_occupant(homer) # Add Homer first (driver) - enforce multiplicity logic
            h_car.add_occupant(chosen_member) # Add the player's choice
            # Add the rest of the family (up to the limit)
            print("Adding the rest of the family...")
            for member in remaining_family:
                if len(h_car.occupants) < 5: # Check limit before adding
                     h_car.add_occupant(member)
                else:
                     print("Car is full!")
                     break # Stop adding if car is full

        else:
            print("Invalid choice. The family just piles in.")
            h_car.add_occupant(homer)
            h_car.add_occupant(marge)
            h_car.add_occupant(bart)
            h_car.add_occupant(lisa)
            h_car.add_occupant(maggie)

    except ValueError:
        print("Invalid input. The family just piles in.")
        h_car.add_occupant(homer)
        h_car.add_occupant(marge)
        h_car.add_occupant(bart)
        h_car.add_occupant(lisa)
        h_car.add_occupant(maggie)

    print(f"\nCurrent occupants in the car: {[o.name for o in h_car.occupants]}")
    print(f"Car status: {h_car}") # Shows composed parts (Engine, Wheels) and occupants

    wait_for_player()

    print("\n--- End of Day ---")
    print("Thanks for playing!")

# Run the game if this file is executed directly
if __name__ == "__main__":
    run_game()
