'''
Test code for plotting the board
'''
from board import Board
from define_board import define_board
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Run this code if this is run as the main function

    # Define the board
    board = define_board()

    # Draw the blank board using matplotlib
    board.draw_mpl()      
    plt.show()  
