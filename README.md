# 2022-Computing-MYE-Task-4
My solution for our Computing MYE task 4

## Question
- Create a 1D array, each index containing whether there is a mine or not, and whether the position has been chosen
- Array length is dependent on difficulty, which the user inputs (Easy: 9, Medium: 16, Hard: 25)
- Randomly populate array with n number of mines, depending on difficulty (Easy: 1, Medium: 3, Hard: 5)


- Prompt user for position
- Check if position has a mine, if there is, quit game
- If there isn't, count number of adjacent mines
- Set the current position to "visited" state, and make sure the position cannot be chosen again
- Quit game once player has stepped on all positions without mines
