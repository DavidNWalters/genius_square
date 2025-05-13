"""Functions for use to support the board class"""
import matplotlib.pyplot as plt

def int_to_letter(num):
    '''    
    Convert an integer from (1,26) to an upper case letter string

    Parameters:
        num: integer
            must be between 1 and 26

    Returns:
        letter: str
            single character string of corresponding letter
    '''

    excpt_str = "num must be an integer between 1 and 26"
    # Check for integer
    if not isinstance(num, int):
        raise Exception(excpt_str)

    # Check within range
    if (num < 1) or (num > 26):
        raise Exception(excpt_str)

    # Convert to upper case letter (A = chr(65), B = chr(66), ...)
    letter = chr(64+num)

    return letter

def letter_to_int(letter):
    '''    
    Convert an upper case letter string to an integer from (1,26)

        Parameters:
            letter: string
                single alpha character string

        Returns:
            num: int
                integer corresponding to number
    '''

    excpt_str = "letter must be a string of 1 letter"
    # Ensure string is upper case
    letter.upper()
    # Check for stromg
    if not isinstance(letter, str):
        raise Exception(excpt_str)

    # Check 1 character
    if len(letter) != 1:
        raise Exception(excpt_str)

    # Check for a letter
    if not letter.isalpha():
        raise Exception(excpt_str)

    # Convert to a number
    num = ord(letter) - 64

    return num


def draw_board_mpl(nx,ny):
    '''    
    Draw the basic board using matplotlib

        Parameters:
            num: integer
                must be between 1 and 26

        Returns:
            letter: str
                single character string of corresponding letter
    '''

    # Cosmetic options
    bgcolour = 'black'
    linecolour = 'dimgray'
    textcolour = 'white'
    linewidth = 3
    font = 'arial black'
    fontsize = 36

    # Setup matplotlib figure object
    fig, ax = plt.subplots(figsize=(12, 8))

    # Setup colours
    fig.patch.set_facecolor(bgcolour)
    ax.patch.set_facecolor(bgcolour)
    for spine in ['top','bottom','left','right']:
        ax.spines[spine].set_color(linecolour)
        ax.spines[spine].set_linewidth(linewidth)

    # Setup axes for the board to be the right size and running top-down
    ax.axis([0, nx, ny, 0])

    # Set major tick marks to be lines between squares
    # Set tick marks to zero length
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False,\
        axis=u'both', which=u'both',length=0, pad=12)
    ax.set_xticks(range(0,nx))
    ax.set_yticks(range(0,ny))
    ax.set_xticklabels('')
    ax.set_yticklabels('')
    plt.grid(color=linecolour,linewidth=0.5)
    
    # Set minor tickmarks to label middle of the squares
    ax.set_xticks([float(n)+0.5 for n in range(0,nx)],minor=True)
    ax.set_xticklabels([str(n+1) for n in range(0,nx)],minor=True)
    ax.set_yticks([float(n)+0.5 for n in range(0,ny)],minor=True)
    ax.set_yticklabels([int_to_letter(n+1) for n in range(0,ny)],minor=True)
    ax.tick_params(axis="both",)

    # Setup fonts/colours of the grid square labels
    for tick in ax.get_xticklabels(minor=True):
        tick.set_font(font)
        tick.set_fontweight('bold')
        tick.set_fontsize(fontsize)
        tick.set_color(textcolour)
    for tick in ax.get_yticklabels(minor=True):
        tick.set_font(font)
        tick.set_fontweight('bold')
        tick.set_fontsize(fontsize)
        tick.set_color(textcolour)

    # Set square aspect ratio
    ax.set_aspect('equal', adjustable='box')