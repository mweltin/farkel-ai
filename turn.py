from random import randint
from exception import InvalidNumberOfDice

'''
 Single 1 = 100
 Single 5 = 50
 Three 1s = 300
 Three 2s = 200
 Three 3s = 300
 Three 4s = 400
 Three 5s = 500
 Three 6s = 600
 
Four of any number = 1,000
Five of any number = 2,000
Six of any number = 3,000
1–6 straight = 1,500
Three pairs = 1,500
Four of any number with a pair = 1,500
Two triplets = 2,500
'''


class Turn:

    def __init__(self, dice_in_play=6):
        if dice_in_play <= 0 or dice_in_play > 6:
            raise InvalidNumberOfDice("Turn class instantiation failed.")
        dice_in_play = dice_in_play
        current_role = []
        is_farkel = False

    def roll(self):
        self.current_role = []
        for x in range(self.dice_in_play):
            self.current_role(randint(1, 6))
        self.current_role = sorted(self.current_role)
