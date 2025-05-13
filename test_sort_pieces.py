from define_pieces import define_pieces
from top_level_functions import sort_pieces

'''
Test code for sorting the pieces in order of decreasing complexity
'''

if __name__ == '__main__':
    # Run this code if this is run as the main function

    pieces = define_pieces()
    
    print('before sort')
    for piece in pieces:
        print(piece.complexity,': ',piece.colour)    
        
    sort_pieces(pieces)
    
    print('after sort')
    for piece in pieces:
        print(piece.complexity,': ',piece.colour)