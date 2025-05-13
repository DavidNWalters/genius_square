'''
Genius Square
-------------
Top-level programme for generating and solving a The Genius Square puzzle
Based on "The Genius Square" by the Happy Puzzle Company
https://en.wikipedia.org/wiki/Happy_Puzzle_Company 
'''

from define_board import define_board
from dice import Dice
from define_dice import define_dice
from matplotlib import pyplot as plt
from top_level_functions import add_roll_dice_button,add_solve_square_button,\
                                roll_all_dice, solve_square


# Run this code if this is run as the main function
if __name__ == '__main__':
    '''
    Main programme for the Genius Square using interactive mpl widgets
    This does not currently work
    '''

    # Define and draw the board
    board = define_board()
    board.draw_mpl()

    # Save main axes to restore after adding the buttons
    board_ax = plt.gca()

    # Add button to roll dice 
    # Current axes are an argument so these can be restored after drawing button
    button_dice = add_roll_dice_button(board_ax)
    cid_dice = button_dice.on_clicked(roll_all_dice)

#    fig = plt.gcf()
#    fig.canvas.mpl_disconnect(cid_dice) 

    # Add button to solve square 
    # Current axes are an argument so these can be restored after drawing button
    button_solve = add_solve_square_button(board_ax)
    cid_solve = button_dice.on_clicked(solve_square)    

    plt.show()

