from turn import Turn
from score import Score
class Player:

    def __init__(self):
        self.turn_score = 0
        self.cumulative_score = 0
        self.turn = Turn
        self.score_table = Score()
        self.scoring_options = {}

    def take_a_turn(self, number_of_dice):
        self.scoring_options = self.turn.full_turn(number_of_dice)

    def show_scoring_choices(self):
        for key, value in self.scoring_options:
            if value == True:
                print(key)
