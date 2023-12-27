from random import randint
from exception import InvalidNumberOfDice, InvalidDieValue


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
        self.__current_role = sorted(self.__current_role)  # can we use the setter in this case for default sort?

    ################### Analyze rolls #####################
    def has_six_of_a_kind(self):
        ''' assumed self.__current_role is sorted'''
        if len(self.__current_role) != 6:
            return False
        # we walk down current roll with a two element window
        for x, y in zip(self.__current_role, self.__current_role[1:]):
            if x != y:
                return False

        return True

    def has_two_triplets(self):
        ''' assumed self.__current_role is sorted'''
        if len(self.__current_role) != 6:
            return False

        first_third = self.__current_role[:3]
        second_third = self.__current_role[3:]

        for x, y in zip(first_third, first_third[1:]):
            if x != y:
                return False

        for x, y in zip(second_third, second_third[1:]):
            if x != y:
                return False

        return True

    def has_five_of_a_kind(self):
        ''' assumed self.__current_role is sorted'''
        if len(self.__current_role) < 5:
            return False

        count = 0
        for x, y in zip(self.__current_role, self.__current_role[1:]):
            if x == y:
                count += 1

        if count == 4:
            return True

        return False

    ################### Getters / Setters #####################
    @property
    def current_role(self):
        return self.__current_role

    @current_role.setter
    def current_role(self, value):
        if len(value) <= 0 or len(value) > 6:
            raise InvalidNumberOfDice("Failed to set roll either too many (>6) or too few (0) ")
        for x in value:
            if x <= 0 or x >= 7:
                raise InvalidDieValue
        self.__current_role = sorted(value)

