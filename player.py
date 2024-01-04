from random import randint
from play import roll


class Player:

    def __init__(self, name=None):
        self.turn_score = 0
        self.score = 0  # holds cumulative score
        self.done = False
        self.name = name

    def __str__(self):
        return self.name

    def pick_scoring_option(self, choice):
        if self.score_table[choice]['name'] != 'Single_1' or self.score_table[choice]['name'] != 'Single_5':
            self.turn_score += self.score_table[choice]['value']
            self.turn.dice_in_play -= self.score_table[choice]['min_dice_required']
        elif self.score_table[choice]['name'] == 'Single_1':
            number_of_dice_that_can_be_used = self.score_table[choice]['value'] / 100
            if number_of_dice_that_can_be_used == 1:
                self.turn.dice_in_play -= 1
            else:
                pass
                # here you have to make a second choice of how many you want to use to score
        elif self.score_table[choice]['name'] == 'Single_1':
            number_of_dice_that_can_be_used = self.score_table[choice]['value'] / 50
            if number_of_dice_that_can_be_used == 1:
                self.turn.dice_in_play -= 1
            else:
                pass
                # here you have to make a second choice of how many you want to use to score
        else:
            pass

    def end_turn(self):
        self.score += self.turn_score
        self.turn_score = 0
