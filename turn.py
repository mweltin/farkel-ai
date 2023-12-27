from random import randint
from exception import InvalidNumberOfDice
from score import Score


class Turn:

    def __init__(self, dice_in_play=6):
        if dice_in_play <= 0 or dice_in_play > 6:
            raise InvalidNumberOfDice("Turn class instantiation failed.")
        self.dice_in_play = dice_in_play
        self.__current_role = []
        is_farkel = False
        self.__score = 0

    def roll(self):
        self.__current_role = []
        for x in range(self.dice_in_play):
            self.__current_role.append(randint(1, 6))
        self.__current_role = sorted(self.__current_role) #can we use the setter in this case for default sort?

    def is_six_of_a_kind(self):
        if len(self.__current_role) < 6:
            return False

        for x, y in zip(self.__current_role, self.__current_role[1:]):
            if x != y:
                return False

        return True

    # /******  getters / setters ********/

    @property
    def current_role(self):
        return self.__current_role

    @current_role.setter
    def current_role(self, value):
        if len(value) <= 0 or len(value) > 6:
            raise InvalidNumberOfDice("Failed to set roll either too many (>6) or too few (0) ")
        self.__current_role = sorted(value)

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value
