"""Functions to support the piece class"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
from board_functions import int_to_letter

def calc_orientations(shape):
    '''
    Take a 2d list of 1s and 0s and calculate the unique orientations
    of this achieved by rotating and flipping it
    
        Parameters
    ----------
    shape: list
        A 2d list defining the basic shape of the piece
        
        
    Returns
    -------
    orientations: list
        A list of 2d lists, each of which contains a unique orientation 
        of the input list/shape
    '''
    # Define this as the first orientation of the piece
    orientations = [shape]

    # Test 2 sides and 4 rotations by 90 degrees for new 
    # unique orientations        
    for side in [0,1]:
        # First time around "side" loop leave untouched
        if side == 1:
            # Second time make mirror image
            shape.reverse()

        # Loop over 4 rotations
        for _ in range(4):
        
            # Rotate latest shape by 90 degrees 
            shape = [list(r) for r in zip(*shape[::-1])]

            # Test if this is a new orientation
            # (start by assuming it is unique and test if it's not)
            unique = True
            for orientation in orientations:
                if shape == orientation:
                    unique = False
                
            if unique:
                orientations.append(shape)
                # length of 1st element is width

    return (orientations)

def reset_orientation(piece):
    '''Initialise the current orientation, location and numpy array'''
    piece.orientation=0
    piece.x = 0
    piece.y = 0
    piece.on_board = False
    # Set the array and its dimensions
    piece.array = np.array(piece.orientations[piece.orientation], dtype=int)
    piece.nx = len(piece.array[0,:])
    piece.ny = len(piece.array[:,0])

def change_orientation(piece,increment=1):
    # Use some local shorthand
    cur_orient = piece.orientation
    n_oreients = piece.n_orientations
    # Increment current orientation by input value increment (modulo the numer of orientations)
    piece.orientation = (cur_orient + n_oreients + increment) % n_oreients
    # Set the array and its dimensions
    piece.array = np.array(piece.orientations[piece.orientation], dtype=int)
    piece.nx = len(piece.array[0,:])
    piece.ny = len(piece.array[:,0])

def print_piece_terminal(piece):
    '''    
    Print the current orientation/position of the piece to
    the terminal using pandas
    '''

    # Calculate lists for x and y labels (if piece is on board)
    if (piece.on_board):
        # Labels run from 1 to nx and A to int_to_letter(my)
        # But coordinates run from 0
        x_arr = [ x + piece.x + 1 for x in range(len(piece.array[0,:]))]
        y_arr = [ int_to_letter(y + piece.y + 1) for y in range(len(piece.array[:,0]))]
    else:
        x_arr = ['*' for x in range(len(piece.array[0,:]))]
        y_arr = ['*' for y in range(len(piece.array[:,0]))]

    # Print some information about the piece
    print(piece.colour)
    print('===================')
    print('Complexity:',piece.complexity,' Orientations:',piece.n_orientations)
    print('Orientation:',piece.orientation)
 
    # Define pandas dataframe from which to print out the array
    df = pd.DataFrame(piece.array)

    # 
    df.columns = x_arr
    df.index = y_arr

    # Print the datafram
    print(df)
    print()    

def draw_piece_mpl(piece,remove=False):
    '''
    Draw (or remove) piece in its current location and orientation

    Parameters:
        piece: object
            Genius square piece defined by the object Piece

        remove: logical (optional, default=False)
            Remove rather than add the piece to the board
            (actually, this just plots a black square over the top of the coloured one)
    '''

    # Calculate a list of locations in the piece 
    # These are [rows,columns] (indexed from 0), so [y,x]
    x_vals = [ x + piece.x for x in range(len(piece.array[0,:]))]
    y_vals = [ y + piece.y for y in range(len(piece.array[:,0]))]

    ax = plt.gca()

    i = 0
    for y in y_vals:
        j = 0
        for x in x_vals:
            if piece.array[i,j] == 1:

                if remove == False:
                    colour = piece.colour
                else:
                    colour = 'k'

                pad=0.02
                rect = patches.FancyBboxPatch((x+pad, y+pad), 1-2*pad, 1-2*pad,
                        boxstyle="round,pad=-0.01,rounding_size=0.1",
                        fc=colour)

                ax.add_patch(rect)

            j += 1

        i += 1
