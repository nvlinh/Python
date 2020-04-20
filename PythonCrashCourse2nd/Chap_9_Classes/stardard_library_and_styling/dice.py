"""A class that can be used to represent a dice"""
from random import randint


class Dice:
    """Model a dice"""

    def __init__(self, sides=None):
        if sides is None:
            self.sides = 6
        else:
            self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


dice_6 = Dice()
dice_10 = Dice(10)
dice_20 = Dice(20)
my_dices = [dice_6, dice_10, dice_20]

for dice in my_dices:
    print(f"Roll dice {dice.sides}")
    for number in range(10):
        dice.roll_die()
