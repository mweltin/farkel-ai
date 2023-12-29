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
        if x != idx + 1:
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

    test_list = [1, 2, 3, 4, 5, 6]

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


def single_ones(self):
    return self.__current_role.count(1) * 100


def single_fives(self):
    return self.__current_role.count(5) * 50
