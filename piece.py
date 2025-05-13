"""A class used to represent a piece in The Genius Square"""
from check_class_arguments import check_piece_shape
import itertools
import numpy as np
from piece_functions import calc_orientations, change_orientation,\
                            draw_piece_mpl,\
                            print_piece_terminal, reset_orientation 

class Piece:
    """
    A class used to represent a "piece" in The Genius Square

    Methods
    -------
    reset_orientation(self)
        resets orientation choice, location and numpy array

    incr_orientation(self)
        increments orientation choice by 1 and sets numpy array
        leaves location unchanged

    decr_orientation(self)
        decrements orientation choice by 1 and sets numpy array
        leaves location unchanged
    """

    def __init__(self, colour='k', shape=[[1]]):
        """
        Parameters
        ----------
        colour: string of the colour of the block
        
        shape: list
            nx x ny list defining the basic shape (0s and 1s)
            
        """

        # Set colour
        self.colour = colour

        # Check that shape is a 2D list containing only 0s and 1s
        check_piece_shape(shape)

        # calculate and store the unique orientations of the shape
        # achienved via rotation and reflection (flipping)
        self.orientations = calc_orientations(shape)

        # Store a count of the number of orientations
        self.n_orientations=len(self.orientations)

        # Initialise current orientation, location on the board and numpy array
        # This sets values of x, y, nx, ny and on_board
        reset_orientation(self)

        # Also define a "complexity" so that we can fit most complex
        # pieces first.
        # Arbitrarily define as 10 * size + orientations
        complexity = 0
        for value in itertools.chain(*shape):
                if value == 1:
                    complexity += 10
        self.complexity = complexity + self.n_orientations

    def reset_orientation(self):
        '''
        Reset the current orientation, location and numpy array
        '''
        # Re-initialise current orientation, location on the board and numpy array
        reset_orientation(self)

    def incr_orientation(self):
        '''
        Update current orientation and numpy array to next orientation
        '''
        change_orientation(self,increment=1)


    def decr_orientation(self):
        '''
        Update current orientation and numpy array to previous orientation
        '''
        change_orientation(self,increment=-1)

    def print_terminal(self):
         '''
         Print information about current orientation/position to terminal
         '''
         print_piece_terminal(self)

    def draw_mpl(self):
         '''
         Draw piece on board (if board has already been defined)
         '''
         draw_piece_mpl(self)

    def delete_mpl(self):
         '''
         Remove piece from board (if board has already been defined)
         '''
         draw_piece_mpl(self,remove=True)