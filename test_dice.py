
from dice import Dice

'''
Test the error capture for the dice class
'''

if __name__ == '__main__':
    # Run this code if this is run as the main function

    # Valid dice
    d = Dice(values=['A6','A6','A6','F1','F1','F1'])


    # Not all length 2
    #d = Dice(['5','A6','A6','F1','F1','F1'])
    
    # Not all strings
    #d = Dice([5,'A6','A6','F1','F1','F1'])

    # Not all 1 letter 1 number
    #d = Dice(['AA','A6','A6','F1','F1','F1'])


    print(d.sides)

    print(d.values)   

    d.roll()

    print(d.side)

    d.roll()
    print(d.side)

    print(d.value) 
