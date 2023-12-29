from random import randint
from turn.score import Score
from turn.exception import InvalidNumberOfDice

class Turn:

    def __init__(self, dice_in_play=6):
        if dice_in_play <= 0 or dice_in_play > 6:
            raise InvalidNumberOfDice("Turn class instantiation failed.")
        self.dice_in_play = dice_in_play
        self.__current_role = []
        self.__score = 0
        self.score_table = Score()
        self.__scoring_opportunities = {
            'Six_of_a_kind': False,
            'Two_triplets': False,
            'Five_of_a_kind': False,
            'Straight': False,
            'Three_pairs': False,
            'Four_of_a_kind_and_a_pair': False,
            'Four_of_a_kind': False,
            'Three_6s': False,
            'Three_5s': False,
            'Three_4s': False,
            'Three_3s': False,
            'Three_1s': False,
            'Three_2s': False,
            'Single_1': False,
            'Single_5': False,
        }
        from ._getters_setters import current_role, scoring_opportunities
        from ._roll_evaluation import single_ones, single_fives, has_straight, has_three_fives, has_three_ones, \
            has_three_fours, has_three_pairs, has_three_sixes, has_three_twos, has_two_triplets, has_four_of_a_kind, \
            has_three_threes, has_six_of_a_kind, has_five_of_a_kind, has_four_of_a_kind_and_a_pair

    def roll(self):
        self.__current_role = []
        for x in range(self.dice_in_play):
            self.__current_role.append(randint(1, 6))
        # ALL roll evaluation methods assume a sorted roll list
        self.__current_role = sorted(self.__current_role)

    def find_valid_scoring_opportunities(self):
        rolled_dice = len(self.__current_role)

        for scoring_opportunity in self.score_table.table:
            if rolled_dice <= scoring_opportunity['min_dice_required']:
                self.__scoring_opportunities[scoring_opportunity['name']] = getattr(self, scoring_opportunity['func'])()

    def reset_score_opportunities(self):
        self.__scoring_opportunities = {
            'Six_of_a_kind': False,
            'Two_triplets': False,
            'Five_of_a_kind': False,
            'Straight': False,
            'Three_pairs': False,
            'Four_of_a_kind_and_a_pair': False,
            'Four_of_a_kind': False,
            'Three_6s': False,
            'Three_5s': False,
            'Three_4s': False,
            'Three_3s': False,
            'Three_1s': False,
            'Three_2s': False,
            'Single_1': False,
            'Single_5': False,
        }
