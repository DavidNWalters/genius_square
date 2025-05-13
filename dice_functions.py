"""Functions to support the dice class"""
from board_functions import letter_to_int
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def get_dice_coords(value):
    '''
    Convert the value of the dice into x,y coords
    -------
    Parameters
    value str
        The face value of the die (1 letter, 1 number)

    Returns
    x, y ints
        Coordinates of the die
    '''

    # Convert dice face values into coordinates
    x = int(value[1]) - 1 # x coord is second value on die
    y = letter_to_int(value[0]) - 1 # y coord in from first value on die
    return x,y


def draw_counter_mpl(value):
    '''
    Draw counter in the location on the die
    -------
    Parameters
    value str
        The face value of the die (1 letter, 1 number)
    '''

    x,y = get_dice_coords(value)

    # Get axis from previous plotting
    ax = plt.gca()

    # Plot a circle to represent counter
    circle = patches.Circle((x+0.5, y+0.5), 0.45,fc='palegoldenrod')

    ax.add_patch(circle)


def draw_dice_mpl(value,dice_num):
    '''
    Draw dice next to the board
    -------
    Parameters
    value str
        The face value of the die (1 letter, 1 number)
    dice_num int
        Used to determine where to draw the dice in the y direction
    '''

    # Get axis from previous plotting
    ax = plt.gca()


    # Draw a rounded rectangle to represent dice
    dice_size = 0.9

    # Define x location w.r.t max x value
    x = 0.5 + ax.get_xlim()[1]
    y = -0.75 + dice_num
    rect = patches.FancyBboxPatch((x, y), dice_size, dice_size,
                        boxstyle="round,pad=-0.01,rounding_size=0.1",
                        fc='white',clip_on=False)

    # Draw the rectangle
    ax.add_patch(rect)

    plt.annotate(value, xy=(x+dice_size/2, y+dice_size/2), annotation_clip=False, 
                 ha='center', va='center', fontsize=18, font = 'arial black')

