from dice import Dice
'''Define a set of Genius Square dice'''
def define_dice(dice_lists = [
        ['A1','C1','D1','D2','E2','F3'],
        ['A2','A3','B1','B2','B3','C2'],
        ['A4','B5','C5','C6','D6','F6'],
        ['A5','A5','B6','E1','F2','F2'],
        ['A6','A6','A6','F1','F1','F1'],
        ['B4','C3','C4','D3','D4','E3'],
        ['D5','E4','E5','E6','F4','F5'] ]):
    """
    Define dice and return as a list of Dice objects

    Parameters:
        dice_lists list (optional)
            List of lists of values on each die
            If not set, defaults to 7 Genius Square dice
    """

    # Setup a list to hold the dice objects    
    dice = []
    for dice_values in dice_lists:
        # Define the next die and add it to the list
        dice.append(Dice(dice_values))
    # Return the list of dice
    return dice