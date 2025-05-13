from define_board import define_board
from dice import Dice
from dice_functions import draw_counter_mpl, draw_dice_mpl
from define_pieces import define_pieces
from matplotlib import pyplot as plt
'''
Test code for adding a full set of pieces and dice on the board
and testing for a solution
'''
#

def add_piece(board,piece,x,y,orientation):
    if orientation > 0:
        for i in range(orientation):
            piece.incr_orientation()

    piece_fits = board.add_piece(piece,x,y)
    if piece_fits:
        piece.draw_mpl()

if __name__ == '__main__':
    # Run this code if this is run as the main function

    # Define and draw the board
    board = define_board()
    board.draw_mpl()

    # Define some 1-side dice to manually set locations
    dice_vals = ['A1','A6','B2','B5','C3','E5','F2']
    d=0
    for val in dice_vals:
        dice=Dice([val])
        board.add_die(dice)
        dice.draw_mpl(d)
        d += 1

    # Define pieces
    pieces = define_pieces()

    # Pieces laid out in a valid solution
    # grey
    add_piece(board,pieces[0],1,0,2)
    # blue
    add_piece(board,pieces[1],4,1,5)
    # red
    add_piece(board,pieces[2],0,1,0)
    # yellow
    add_piece(board,pieces[3],0,3,0)
    # green
    add_piece(board,pieces[4],2,3,0)
    # orange
    add_piece(board,pieces[5],2,5,0)
    # purple
    add_piece(board,pieces[6],2,1,2)
    # brown
    add_piece(board,pieces[7],5,4,1)
    # darkblue
    add_piece(board,pieces[8],4,2,0)

    #
    print(board.array)
    if board.check_solution():
        print('Valid solution')
    else:
        print('Not a complete solution')

    # Plot image
    plt.show()