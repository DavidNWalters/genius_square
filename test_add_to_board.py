from define_board import define_board
from dice_functions import draw_counter_mpl, draw_dice_mpl
from define_pieces import define_pieces
from dice import Dice
from matplotlib import pyplot as plt

''' 
Test code for adding pieces and dice to the board
(rather than just drawing them there)
'''

if __name__ == '__main__':
    # Run this code if this is run as the main function

    # Define and draw the board
    board = define_board()
    board.draw_mpl()

    # Define pieces
    pieces = define_pieces()
    
    # Test add dice a dice to the board
    # Create a die with 1 side
    die = Dice(['A1'])
    
    die_fits = board.add_die(die)
 
    # Draw the die
    if die_fits:
        die.draw_mpl()
    
    # Test adding first piece
    piece = pieces[1]
    (x,y) = (1,3)
    piece_fits = board.add_piece(piece,x,y)
    print(piece_fits)
    print(board.array)

    if piece_fits:
        piece.draw_mpl()

    # Test adding first piece
    piece = pieces[4]
    (x,y) = (1,2)
    piece_fits = board.add_piece(piece,x,y)
    print(piece_fits)
    print(board.array)

    if piece_fits:
        piece.draw_mpl()

    plt.show()