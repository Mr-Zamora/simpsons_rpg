"""
main.py - Entry point for the Simpsons RPG game
"""

# Add the parent directory to the Python path so we can use relative imports
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the game module
from simpsons_rpg.game import run_game

if __name__ == "__main__":
    run_game()
