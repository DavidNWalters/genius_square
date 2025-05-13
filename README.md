# Genius_Square

Python code to generate and solve Genius Square Puzzles
based on The Genius Square puzzle
https://www.happypuzzle.co.uk/family-puzzles-and-games/the-genius-collection/genius-square
from The Happy Puzzle company:
https://en.wikipedia.org/wiki/Happy_Puzzle_Company

## Aim 
The aim of the puzzle is to roll the dice, which define the location of 1x1 circular
counters that block out squares on the board. The aim is then to fit the different coloure
and shaped pieces to fill every square on the board.

The Genius Square dice are defined so that every possible rolled set of dice leads to a
soluble puzzle. This code is guaranteed to find one of the valid solutions.

It's also possible to define your own dice in this code, to see whether this leads to a
possible solution.

## Method
The Genius Square board, dice and shaped/coloured pieces are defined as objects.

When programme is run:
 * Define/draw the board
 * Defint/roll the dice
 * Show the board with the counters on only
 
 When window is closed:
 * Open new window plotting the same information
 * Attempt to solve the Genius Square and plot the solution

## Algorithm (for solving the Genius Square)
* Select pieces in turn from the most to the least complex.
* For each piece in its first orientation, loop over possible locations on the board 
  and fit it into the first available slot. If it doesn't fit, try the next orientation
  and start from the first location again, looping through the locations until it fits.
* Move onto the next piece and attempt the same.
* If/when a piece doesn't fit, go back to the previous piece and try the next location
  and orientation.
* Continue this until all pieces fit onto the board.

## Usage

```
python3 genius_square.py
```

## Requirements

 * python3
 * numpy
 * matplot
 * pandas (only used for debugging, so could be removed easily)