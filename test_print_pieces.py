import pandas as pd
from define_pieces import define_pieces
'''
Test code for printing pieces to the terminal using pandas
'''
def print_piece(piece):
    for i in range(piece.n_orientations):
        piece.print_terminal()
        piece.incr_orientation()


if __name__ == '__main__':
    # Run this code if this is run as the main function

    pieces = define_pieces()

    for piece in pieces:
        print_piece(piece)
