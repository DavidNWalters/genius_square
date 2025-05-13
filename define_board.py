from board import Board
'''Define the Genius Square board'''

def define_board():
    """
    Define Genius Square board
    """

    # The basic 6x6 dimensions of the board
    (width,height) = (6,6)

    board = Board(width,height)

    return board