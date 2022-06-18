# minesweeper.py
# Simple 1D minesweeper game

# Libraries
import random

# Variables
gameboard = []
available_positions = 0

# Position class
# .mine: Determines if there is a mine or not, values: M, NM
# .chosen: Determines if player visited position, values: 0, 1
# Read up on classes here: https://www.w3schools.com/python/python_classes.asp
class Position:
    def __init__(self, mine):
        self.mine = mine
        self.chosen = 0

# Function to populate gameboard based on difficulty
# Input: easy, medium, hard
# Output: None
def populate(difficulty):
    global gameboard, available_positions  # read up on global variables if u dunno

    # Populate gameboard based on difficulty
    if difficulty == "easy":
        positions = 9
        mines = 1
    elif difficulty == "medium":
        positions = 16
        mines = 3
    elif difficulty == "hard":
        positions = 25
        mines = 5
    available_positions = positions - mines
    gameboard = [Position("NM") for i in range(positions)]

    # Randomly put mines on gameboard
    for i in range(mines):
        pos = random.choice(gameboard)
        while pos.mine == "M":              # While there is a mine on chosen position,
            pos = random.choice(gameboard)  # Choose another position
        
        pos.mine = "M"                      # Put mine on position

# Function to get number of adjacent mines
# Input: position, the position the user entered
# Output: Number of adjacent mines
def getAdjacentMines(pos):
    pos -= 1  # The actual index is 1 less than the input position
    
    adjacent_count = 0

    if pos < len(gameboard) - 1: # If the position is not the rightmost of the gameboard (to prevent IndexError when we do pos + 1)
        if gameboard[pos + 1].mine == "M": # and there is a mine, add 1 to adjacent count
            adjacent_count += 1
    if pos != 0: # If position is not leftmost of the gameboard
        if gameboard[pos - 1].mine == "M":
            adjacent_count += 1

    return adjacent_count
        
# Gameloop
# In charge of running the game
# Returns: 0 if won, 1 if lost, -1 if quit
def gameloop():
    global gameboard, available_positions

    # Define suitable inputs
    options = list(range(1, len(gameboard) + 1)) # This actually gives a list of numbers from 1 to gameboard length
    options = [str(x) for x in options] # Convert everything to string so that we can compare input
    options.append("q") # Add quit option

    # Continue game if all non-mine positions are not discovered
    while available_positions > 0:
        pos = input("Enter position (1 to " + str(len(gameboard)) + "): ")
        # Input validation
        while pos.lower() not in options:
            pos = input("Invalid Input!\nEnter position: ")

        # Quit if Q is entered
        if pos.lower() == "q":
            return -1  # rmb -1 is the defined return value for quit

        # Cast position to int
        pos = int(pos)

        # Check if position was chosen, continue to next iteration
        if gameboard[pos - 1].chosen == 1:
            continue # This would cause us to jump back to the start of the while loop, skipping the code below
            
        # d)i) Display pos and quit if there is mine
        print("You chose position " + str(pos) + "!")
        if gameboard[pos - 1].mine == "M":
            return 1  # rmb 1 is the defined return value for loss

        # d)ii) If chosen pos doesn't contain mine, display adjacent mine count and update position chosen
        # Code will never reach here if we stepped on a mine, as it will be returned
        # Return is something like break in this case, hence we don't need a if statement
        print("There are " + str(getAdjacentMines(pos)) + " mine(s) beside you!")
        gameboard[pos - 1].chosen = 1
        available_positions -= 1
        print("There are " + str(available_positions) + " available positions left!\n")

    # Once we're here, it means the while loop is broken out
    # which means that we've discovered all available positions
    # Hence we return the winning code, 0
    return 0
        
# Main function
# Gathers input from player and sets gameboard up
def main():
    options = ["easy", "medium", "hard"]
    print("Welcome to minesweeper!\nPls enter your difficulty " + str(options))
    difficulty = input("> ").lower()

    # Validate input
    while difficulty not in options:              # while input is not in avaliable options
        difficulty = input("Invalid Choice!\n> ").lower() # ask for input again

    # Setup gameboard
    populate(difficulty)

    # Enter game
    ret = gameloop()

    # Display appropriate output based on quit condition
    if ret == -1:
        print("Successfully quit game!")
    elif ret == 0:
        print("Congratulations! You won!")
    elif ret == 1:
        print("You stepped on a mine!\nBetter luck next time!")

# Better python practice to write this
# Writing main() also works
if __name__ == "__main__":
    main()
