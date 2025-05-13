'''
Genius Square
-------------
Top-level programme for generating and solving a The Genius Square puzzle
Based on "The Genius Square" by the Happy Puzzle Company
https://en.wikipedia.org/wiki/Happy_Puzzle_Company 
'''

from define_board import define_board
from define_pieces import define_pieces
from dice import Dice
from define_dice import define_dice
from matplotlib import pyplot as plt
from top_level_functions import draw_all_dice,\
                                roll_all_dice, solve_square


# Run this code if this is run as the main function
if __name__ == '__main__':
    '''
    Main programme for the Genius Square

    When programme is run:
        * Define/draw the board
        * Defint/roll the dice
        * Show the board with the counters on only
 
    When window is closed:
       * Open new window plotting the same information
       * Attempt to solve the Genius Square and plot the solution
    
    '''

    # Define and draw the board
    board = define_board()
    board.draw_mpl()

    # Roll the dice and draw counters/dice on the board
    dice = roll_all_dice(board)
#    dice = roll_all_dice(board, \
#            dice_values = [['A1'], ['A6'], ['B2'], ['C3'], ['E2'], ['E6'], ['F4']])

    print('Dice rolled: ',[dice[i].value for i in range(len(dice))])
    plt.show()

    # Code will pause at this point and continue when the matplotlib
    # window is closed. This means we'll need to redraw the board and dice 
    # before we can continue
    board.draw_mpl()
    draw_all_dice(dice)

    # Define pieces 
    pieces = define_pieces()

    # Call algorithm to solve the square
    solve_square(board,pieces,dice)

    plt.show()