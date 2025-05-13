"""A class used to represent a die in The Genius Square"""
from check_class_arguments import check_dice_values
from dice_functions import draw_counter_mpl, draw_dice_mpl
import random as rand

class Dice:
    """
    A class used to represent a die in The Genius Square

       Methods:
            draw_mpl()
                Draw the dice counter on the board and the dice next to the board

            roll()
                Randomly picks a side of the die and its face value
    """

    def __init__(self, values=['A2','A3','B1','B2','B3','C2']):
        """
        Parameters
        ----------
        values : list of strings
            List of strings, each of which should be of length 2 and 
            made up of 1 letter followed by 1 number (to represent a 
            locaiton on The Genius Square)
        """
        # Count number of sides
        self.sides = len(values)

        # Check that 'values' is a list of strings,
        #     each being 1 letter and 1 number
        check_dice_values(values)
        
        # Make all letter upper case
        self.values = list(map(str.upper,values))

        # Initialise roll to be 0th value
        self.side = 0
        self.value = self.values[self.side]

    def roll(self):
        """
        Randomly select one side of the dice and set value to its face value
        """
        # Randomly pick a side and set the value to that side
        self.side = rand.randrange(self.sides)
        self.value = self.values[self.side]

    def draw_mpl(self,dice_num=0):
        ''''
        Draw counter on board (if board has already been defined) 
        '''
        draw_counter_mpl(self.value)
        draw_dice_mpl(self.value,dice_num)