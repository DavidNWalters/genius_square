'''Define a set of Genius Square pieces'''

from piece import Piece
def define_pieces():
    """
    Define the 9 pieces and return as a list of Piece objects
    """

    # The 9 coloured pices included in The Genius Square
    shapes = [
        [[1,1,1,1]],

        [[1,0],
         [1,0],
         [1,1]],

        [[1,0],
         [1,1],
         [0,1]],

        [[1,0],
         [1,1],
         [1,0]],

        [[1,1],
         [1,1]],

        [[1,1,1]],

        [[1,0],
         [1,1]],

        [[1,1]],

        [[1]]
             ]
 
    # Colours of the squares.
    colours = ['dimgrey','deepskyblue','red','gold','forestgreen',
               'darkorange','mediumorchid','saddlebrown','mediumblue']
    # darkblue is closer than mediumblue, but difficult to see

    # Set up blank list for pieces
    pieces = []
    # Loop over input data, define pieces and add to the list
    for (shape, colour) in zip(shapes, colours):
        pieces.append(Piece(colour=colour,shape=shape))

    return pieces




