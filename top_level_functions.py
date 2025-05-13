"""Top-level functions not associated with a class"""
from define_dice import define_dice
from define_pieces import define_pieces
from matplotlib import pyplot as plt
from matplotlib import rcParams
from matplotlib.widgets import Button

def roll_all_dice(board,dice_values = 'preset'):
    '''    
    Randomly select values from each of the dice, add these dice values
    using counters to the board and display the dice as well

        Parameters:
            board: object
                object defining the Genius Square board
            dice_values: list
                (optional: default = string:'preset')
                list of lists of dice face values
                if this is just the string 'preset' it will use the
                pre-defined list of values describing the dice in the 
                Genius Square

        Returns:
            dice: list 
                list of pre-rolled 'dice' objects  
            '''

    # Default value of dice_values means call define_dice without arguments
    # to use the default Genius Square dice
    if dice_values == 'preset':
        dice = define_dice()
    # If dice_values is set then pass this through to define_dice to use
    # custom dice
    #
    # This can also be used to pre-select the rolled dice values by defining a set
    # of dice with only 1-side (i.e. a list of 7 lists of 1 face value)
    else:
        dice = define_dice(dice_values)

    # Loop over dice and roll them
    dice_num = 0
    for die in dice:
        die.roll()
        # Try to add the die to the board
        die_fits = board.add_die(die)
        # Draw the counters on the board and the dice next to this
        if die_fits:
            die.draw_mpl(dice_num)
        else:
            excpt_str = 'Die with value '+die.value+' added in invalid position'
            raise Exception(excpt_str)
        dice_num += 1

    return dice

def draw_all_dice(dice):
    '''    
    Redraw all of the dice and counters without rerolling them or returning objects

        Parameters:
            dice: list
                list of Dice objects to be drawn
    '''
    # Loop over dice
    dice_num = 0
    # Draw the counters on the board and the dice next to this
    for die in dice:
        die.draw_mpl(dice_num)
        dice_num += 1

def add_roll_dice_button(ax):
    '''
    An attempt to make the system interctive using mpl widgets.
    This is not working well at the moment.

        Parameter:
            ax: axis
                axis for the board to be reinstated after plotting the button

        Returns:
            button_dice: widget
                Button with which to roll the dice            
    '''
    # Change some parameters for the button text 
    rcParams['text.color'] = 'white'
    rcParams['font.size'] = 16  
 
    # Define new axes and add/activate button
    axes = plt.axes([0.02, 0.7, 0.15, 0.075])
    button_dice = Button(axes, 'Roll Dice',color="dimgrey",hovercolor='grey')

    # Reset text colour and figure axes
    rcParams['text.color'] = 'black'
    plt.sca(ax)

    # Return button_dice so that we can watch for a button press
    return button_dice

def add_solve_square_button(ax):
    '''
    An attempt to make the system interctive using mpl widgets.
    This is not working well at the moment.

        Parameter:
            ax: axis
                axis for the board to be reinstated after plotting the button

        Returns:
            button_solve: widget
                Button with which to solve the square            
  
        '''

    # Change some parameters for the button text 
    rcParams['text.color'] = 'white'
    rcParams['font.size'] = 16  
 
    # Define new axes and add/activate button
    axes = plt.axes([0.02, 0.5, 0.15, 0.075])
    button_solve = Button(axes, 'Solve Square',color="dimgrey",hovercolor='grey')

    # Reset text colour and figure axes
    rcParams['text.color'] = 'black'
    plt.sca(ax)

    # Return button_dice so that we can watch for a button press
    return button_solve

def sort_pieces(pieces):
    '''    
    Sort the pieces in the input list in order of decreasing complexity

        Parameters:
            pieces: list
                A list of pieces defined using the Piece object
            
    '''

    # Define a dictionary linking the pieces to their complexity
    keydict = dict(zip(pieces, [pieces[x].complexity for x in range(len(pieces))]))
    # Use this to sort the list in order of decreasing complexity
    pieces.sort(key=keydict.get, reverse=True)

    return

def solve_square(board,pieces,dice,plot_when_solving=False):
    '''    
    Start the algorithm to solve the Genius Square

        Parameters:
            board: object
                The Genius Square board defined using the Piece object
            pieces: list
                A list of pieces defined using the Piece object
            dice: list
                A list of Genius Square dice defined using the Dice object
            plot_when_solving: logical (optional, default=False)
                Plot the pieces as they're being fitted if True
                Plot at the end (so long as there's a solution) if False
            
        Returns:
            solution_found: logical
                True if a solution is found, False if not

    General method:
        * Loop over all pieces from the most complex to the least complex
        * Loop over all the orientations and potential locations for that orientation
        * Add the pieces to the board when they fit and move onto the next piece
        * If the piece doesn't fit anywhere, go back to the previous piece and carry on

        * So long as the dice used are valid Genius Square dice, this is guaranteed to work
    '''

    debug = False
    # Switch on interactive plotting if plot_when_solving is set
    # Delay between plotted shapes is frame_delay (in seconds) 
    if plot_when_solving:
        frame_delay = 0.2
        plt.ion()

    # Start by sorting the pieces into order of decreasing complexity
    sort_pieces(pieces)

    # Initialise all pieces to be at orientation, x, y = 0
    # and not to be on the board
    for piece in pieces: 
        piece.reset_orientation()

    # Initialise count of numer of steps
    i_steps = 0
    # Start loop over pieces
    i_piece = 0
    # Loop over all pieces
    while (i_piece < len(pieces)): 
        piece = pieces[i_piece]

        # Define a local version of this variable as function to increment this 
        # is set to loop, so the while loop would always be true
        i_orientation = piece.orientation
        # Start loop over orientation 
        while (i_orientation < piece.n_orientations and not piece.on_board):
            # Start loop over y location
            max_y = board.ny-piece.ny+1
            while (piece.y < max_y and not piece.on_board):
                # Start loop over x location
                max_x = board.nx-piece.nx+1
                while (piece.x < max_x and not piece.on_board):
                    if debug:
                        print(i_piece, i_orientation, piece.y, piece.x)
    
                    # Attempt to add piece to the board. It will only be added
                    # if it fits (which sets piece.on_board to True)
                    board.add_piece(piece,piece.x,piece.y)
                    if piece.on_board:
                        if plot_when_solving:
                            piece.draw_mpl()
                            plt.pause(frame_delay)

                    # Add to number of steps
                    i_steps += 1
                    # Increment x unless piece has been added to board
                    if not piece.on_board:
                        piece.x += 1

                # Increment y and reset row valu unless piece has been added to board
                if not piece.on_board:
                    piece.x = 0
                    piece.y += 1

            # Increment orientiation reset y unless piece has been added to board
            if not piece.on_board:
                piece.y = 0
                piece.incr_orientation()
                i_orientation += 1 
    
        # Increment piece by 1 if the piece fits on the board
        if piece.on_board:
            if debug:
                print(piece.colour,' fits')
                piece.print_terminal()
            i_piece += 1

        else:
            (piece, i_piece, i_orientation) = revert_to_last_piece(\
                board,piece,i_piece,pieces,i_orientation,plot_when_solving,debug)

    # Finally check that we have a valid solution
    square_solved = board.check_solution()
    if square_solved:
        # Plot pieces if this hasn't been done already
        if not plot_when_solving:
            for piece in pieces:
                piece.draw_mpl()
        print('Square solved in ',i_steps,' steps.')
    else:
        print('No valid solution to this Genuis Square after ',i_steps,' steps.')
  
    if plot_when_solving:
        plt.ioff()
    
    return

def revert_to_last_piece(board,piece,i_piece,pieces,i_orientation,plot_when_solving,debug):
    
    # If piece doesn't fit then reset piece and go back to last piece in its last position
    if debug:
        print(piece.colour,' does not fit.')
        piece.print_terminal()
    piece.reset_orientation()
 
    # Move back to last piece
    i_piece -=1
    piece = pieces[i_piece]
    # Set i_orientaiton to the piece's orientation
    i_orientation = piece.orientation

    if debug:
        print('After reverting piece:',i_piece, i_orientation, piece.y, piece.x)
        piece.print_terminal()
    
    # Remove the previous piece from the board
    board.remove_piece(piece)
    # And remove it from the board
    fig = plt.gcf()
    if plot_when_solving:
        for patch in piece.patches:
            patch.remove()

    # Increase x by 1
    piece.x += 1
    # Carry over to next loop position if this is the max x value
    if piece.x == board.nx-piece.nx+1:
        piece.x = 0
        piece.y += 1

        # Carry over to next loop position if this is the max y value
        if piece.y == board.ny-piece.ny+1:
            piece.y = 0
            piece.incr_orientation()
            i_orientation += 1 

            # Finally, if this carries over past the last orientation,
            # then we move back to the last piece again.
            # Do this by recursively calling self
            if i_orientation == piece.n_orientations:
                (piece, i_piece, i_orientation) = revert_to_last_piece(board,piece,i_piece,pieces,i_orientation,plot_when_solving,debug)

    return (piece, i_piece, i_orientation)