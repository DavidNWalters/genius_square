"""A class used to represent the board in The Genius Square"""
import matplotlib.pyplot as plt
import numpy as np
from board_functions import int_to_letter, draw_board_mpl
from dice_functions import get_dice_coords

class Board:
    """
    A class used to represent the board in The Genius Square

        Methods:
            draw_mpl()
                Draw the board using matplotlib

            add_die()
                Check if a die can be added to the board in a location and do 
                so if it can

            add_piece()
                Check if a piece can be added to the board in a location and do 
                so if it can

            check_solution()
                Check whether the board, the dice and the pieces make up a valid 
                solution (i.e. every square is occupied exactly once)

            remove_piece()
                Remove a piece from the board but keep a record of board location
    """

    def __init__(self, width=6, height=6):
        """
        Parameters
        ----------
        width (default=6) : int

        height (default=6) : int
        """

        # Size of the board
        self.nx = width
        self.ny = height

        # Initialise array to hold number of times each square is filled
        self.array = np.zeros((height,width), dtype=int)

    def draw_mpl(self):
        """
        Draw the board using matplotlib
        """
        draw_board_mpl(self.nx,self.ny)  

    def add_piece(self,piece,x,y):
        '''
        Add a piece to the board after checking that there is space for it
        '''
        # Set x and y values of piece and assume that the piece fits
        piece.on_board = True
        piece.x = x
        piece.y = y

        # Piece won't fit if it doesn't fully overlap with the board
        if (x<0) or (x+piece.nx>self.nx) \
             or (y<0) or (y+piece.ny>self.ny):
            piece.on_board = False
            return piece.on_board

        # Add piece.array to board.array
        self.array[y:y+piece.ny,x:x+piece.nx] += piece.array

        # If the maximum value of board array > 1 then the piece doesn't fit
        # (i.e. at least one part is in the same place as something else)
        if self.array.max() > 1:
            # remove from board (delete from array) and unset x and y        
            self.array[y:y+piece.ny,x:x+piece.nx] -= piece.array
            piece.on_board = False

        return piece.on_board

    def remove_piece(self,piece):
        '''
        Remove a piece from the board wihtout chaging x, y or orientation.
        Leave piece unaltered if it isn't on the board.
        Note that this is a bit fragile as it assumes that the orientation hasn't
        changes since the piece was added to the board.
        '''
        if piece.on_board:
            piece.on_board = False

            # Subtract piece.array from board.array
            self.array[piece.y:piece.y+piece.ny,piece.x:piece.x+piece.nx] -= piece.array

    def add_die(self,die):
        '''
        Add a die counter to the board after checking that there is space for it
        '''
        # Initially set x and y values of die and assume that it fits
        die_fits = True

        x,y = get_dice_coords(die.value)

        # Dice must fit on the board
        if (x<0) or (x>self.nx) \
             or (y<0) or (y>self.ny):
            die_fits = False
            return die_fits

        # Check if die location on board = 0
        if self.array[y,x] == 0:
            self.array[y,x] = 1
        else:
            die_fits = False

        return die_fits

    def check_solution(self):
        '''Return True if all values of array are 1'''
        if np.all(self.array == 1):
            return True
        else:
            return False