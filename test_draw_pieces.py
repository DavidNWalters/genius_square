from define_board import define_board
from define_pieces import define_pieces
from matplotlib import pyplot as plt

''' 
Test code for plotting a single piece on the board
'''


if __name__ == '__main__':
    # Run this code if this is run as the main function

    # Define and draw the board
    board = define_board()
    ax = board.draw_mpl()

    # Define pieces
    pieces = define_pieces()

    # Select a piece and test drawing it in a specific location
    x = 4 ; y = 1
    piece = pieces[1]
    piece.incr_orientation()

    piece.x = x
    piece.y = y

    # Draw the piece
    piece.draw_mpl()

    # Plot image
    plt.show()