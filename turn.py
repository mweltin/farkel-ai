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
        # ALL roll evaluation methods assume a sorted roll list
        self.__current_role = sorted(self.__current_role)

    ################### Roll evaluation methods #####################
    def has_six_of_a_kind(self):
        if len(self.__current_role) != 6:
            return False
        # we walk down current roll with a two element window
        for x, y in zip(self.__current_role, self.__current_role[1:]):
            if x != y:
                return False

        return True

    def has_two_triplets(self):
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
        if len(self.__current_role) < 5:
            return False

        count = 0
        for x, y in zip(self.__current_role, self.__current_role[1:]):
            if x == y:
                count += 1

        if count == 4:
            return True

        return False

    def has_straight(self):
        if len(self.__current_role) < 5:
            return False

        for idx, x in enumerate(self.__current_role):
            if x != idx +1:
                return False

        return True

    def has_three_pairs(self):
        if len(self.__current_role) != 6:
            return False

        if self.__current_role[0] == self.__current_role[1] and \
            self.__current_role[2] == self.__current_role[3] and \
            self.__current_role[4] == self.__current_role[5]:
            return True

        return False

    def has_four_of_a_kind_and_a_pair(self):
        if len(self.__current_role) != 6:
            return False

        min_value = min(self.__current_role)
        max_value = max(self.__current_role)

        if (self.__current_role.count(min_value) == 4 and self.__current_role.count(max_value) == 2) or \
           (self.__current_role.count(max_value) == 4 and self.__current_role.count(min_value) == 2):
            return True

        return False

    def has_four_of_a_kind(self):
        if len(self.__current_role) < 4:
            return False

        test_list = [1,2,3,4,5,6]

        for x in test_list:
            if self.__current_role.count(x) == 4:
                return True

        return False

    def has_three_sixes(self):
        if len(self.__current_role) < 3:
            return False

        if self.__current_role.count(6) >= 3:
            return True

        return False

    def has_three_fives(self):
        if len(self.__current_role) < 3:
            return False

        if self.__current_role.count(5) >= 3:
            return True

        return False

    def has_three_fours(self):
        if len(self.__current_role) < 3:
            return False

        if self.__current_role.count(4) >= 3:
            return True

        return False

    def has_three_threes(self):
        if len(self.__current_role) < 3:
            return False

        if self.__current_role.count(3) >= 3:
            return True

        return False

    def has_three_twos(self):
        if len(self.__current_role) < 3:
            return False

        if self.__current_role.count(2) >= 3:
            return True

        return False

    def has_three_ones(self):
        if len(self.__current_role) < 3:
            return False

        if self.__current_role.count(1) >= 3:
            return True

        return False
                ################### Getters / Setters #####################
    @property
    def current_role(self):
        return self.__current_role

    @current_role.setter
    def current_role(self, value):
        '''makes unit testing easier'''
        if len(value) <= 0 or len(value) > 6:
            raise InvalidNumberOfDice("Failed to set roll either too many (>6) or too few (0) ")
        for x in value:
            if x <= 0 or x >= 7:
                raise InvalidDieValue
        self.__current_role = sorted(value)

