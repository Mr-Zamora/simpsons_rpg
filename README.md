# Simpsons RPG

A simple text-based RPG game featuring The Simpsons characters, designed to demonstrate Object-Oriented Programming (OOP) concepts in Python.

## Project Structure

The project has been organized into multiple files following OOP best practices:

- **interfaces.py**: Contains the `CanSpeak` interface that defines the speaking behavior
- **base_characters.py**: Contains the base `Simpson` class that all characters inherit from
- **simpson_characters.py**: Contains the specific Simpson character classes (Homer, Marge, Bart, Lisa, Maggie)
- **items.py**: Contains classes for various items (DuffBeer, Skateboard, NuclearPlant, Saxophone)
- **vehicles.py**: Contains classes for vehicles and their components (HomersCar, Engine, Wheel)
- **family.py**: Contains the Family class that aggregates Simpson members
- **game.py**: Main game file with the game logic and interactive elements

## OOP Concepts Demonstrated

1. **Inheritance**: All Simpson characters inherit from the base Simpson class
2. **Interfaces**: The CanSpeak interface defines a contract for speaking behavior
3. **Encapsulation**: Private attributes and methods are denoted with underscore (_)
4. **Abstraction**: Complex behaviors are broken down into simpler steps
5. **Association**: Homer has an association with DuffBeer and HomersCar
6. **Aggregation**: Bart owns a Skateboard, Family aggregates Simpson members
7. **Composition**: HomersCar is composed of Engine and Wheel objects
8. **Dependency**: Homer depends on NuclearPlant, Lisa depends on Saxophone

## How to Run the Game

To run the game, navigate to the project directory and run:

```
python game.py
```

Follow the on-screen prompts to interact with the game.

## Educational Purpose

This project serves as an educational example of OOP concepts in Python, particularly:
- How to implement inheritance hierarchies
- How to model different types of object relationships
- How to use encapsulation and abstraction to organize code
- How to translate UML diagrams into working code
