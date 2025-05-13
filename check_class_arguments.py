"""Functions to check arguments in class definitions"""

import itertools

def check_dice_values(values):
    '''    
    Check that dice class is initiated with a valid set of face values

        Parameters:
            values: list
                List of strings, each of which should be of length 2 and 
                made up of 1 letter followed by 1 number (to represent a 
                locaiton on The Genius Square)
    '''

    excpt_str = "Dice must be initiated with a list of strings"
    # Loop over values assigned to the die
    for value in values:
        # Check all values are strings
        if not isinstance(value, str):
            raise Exception(excpt_str)

        # Check all values are 2 characters long
        value_len = 2
        if not len(value) == value_len:
            raise Exception(excpt_str+" of length "+str(value_len))

        # Check first (second) character is a letter (number) 
        if not value[0].isalpha() or not value[1].isdigit():
            raise Exception(excpt_str+" (letter,number)")

def check_piece_shape(shape):
    '''    
    Check that piece class is initiated with a valid list for its shape

        Parameters:
            shape: list 
                2d list of integers containing 0s and 1s 
    '''

    excpt_str = "Piece must be initiated with a list of 0s and 1"
    # Loop over values in the list assigned to the shape of the piece
    for value in itertools.chain(*shape):
        if not isinstance(value, int):
            raise Exception(excpt_str)
        if (value != 1) and (value != 0):
            raise Exception(excpt_str)