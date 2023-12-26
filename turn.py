from random import randint
from exception import InvalidNumberOfDice


class Score:
    {
        'Six_of_a_kind': 3000,
        'Two_triplets': 2500,
        'Five_of_a_kind': 2000,
        'Straight': 1500,
        'Three_pairs': 1500,
        'Four_of_a_kind_and_a_pair': 1500,
        'Four_of_a_kind': 1000,
        'Three_6s': 600,
        'Three_5s': 500,
        'Three_4s': 400,
        'Three_3s': 300,
        'Three_1s': 300,
        'Three_2s': 200,
        'Single_1': 100,
        'Single_5': 50,
    }
        


    class Turn:

        def __init__(self, dice_in_play=6):
            if dice_in_play <= 0 or dice_in_play > 6:
                raise InvalidNumberOfDice("Turn class instantiation failed.")
            dice_in_play = dice_in_play
            current_role = []
            is_farkel = False
            _scores_ = Score
            score = 0

        def roll(self):
            self.current_role = []
            for x in range(self.dice_in_play):
                self.current_role(randint(1, 6))
            self.current_role = sorted(self.current_role)
