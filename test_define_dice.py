
from define_dice import define_dice

if __name__ == '__main__':
    # Run this code if this is run as the main function

    dice = define_dice()

    for die in dice:
            die.roll()
    
            if False:
                print('Values: ',die.values)
                print('    Side: ',die.side)
                print('    Value: ',die.value)
            else:
                print(die.value)