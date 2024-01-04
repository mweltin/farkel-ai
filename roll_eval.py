class RollEval:
    def __init__(self, roll):
        self.table = [
            {'name': 'Six_of_a_kind', 'value': 3000, 'min_dice_required': 6, 'func': 'has_six_of_a_kind'},
            {'name': 'Two_triplets', 'value': 2500, 'min_dice_required': 6, 'func': 'has_two_triplets'},
            {'name': 'Five_of_a_kind', 'value': 2000, 'min_dice_required': 5, 'func': 'has_five_of_a_kind'},
            {'name': 'Straight', 'value': 1500, 'min_dice_required': 6, 'func': 'has_straight'},
            {'name': 'Three_pairs', 'value': 1500, 'min_dice_required': 6, 'func': 'has_three_pairs'},
            {'name': 'Four_of_a_kind_and_a_pair', 'value': 1500, 'min_dice_required': 6,
             'func': 'has_four_of_a_kind_and_a_pair'},
            {'name': 'Four_of_a_kind', 'value': 1000, 'min_dice_required': 4, 'func': 'has_four_of_a_kind'},
            {'name': 'Three_6s', 'value': 600, 'min_dice_required': 3, 'func': 'has_three_sixes'},
            {'name': 'Three_5s', 'value': 500, 'min_dice_required': 3, 'func': 'has_three_fives'},
            {'name': 'Three_4s', 'value': 400, 'min_dice_required': 3, 'func': 'has_three_fours'},
            {'name': 'Three_3s', 'value': 300, 'min_dice_required': 3, 'func': 'has_three_threes'},
            {'name': 'Three_1s', 'value': 300, 'min_dice_required': 3, 'func': 'has_three_ones'},
            {'name': 'Three_2s', 'value': 200, 'min_dice_required': 3, 'func': 'has_three_twos'},
            {'name': 'Single_1', 'value': 100, 'min_dice_required': 1, 'func': 'single_ones'},
            {'name': 'Single_5', 'value': 50, 'min_dice_required': 1, 'func': 'single_fives'},
        ]
        self.current_roll = sorted(roll)
        self.scoring_opportunities = {
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
        self.set_scoring_opportunities()

    def set_scoring_opportunities(self):
        rolled_dice = len(self.current_roll)

        for scoring_opportunity in self.table:
            if rolled_dice >= scoring_opportunity['min_dice_required']:
                self.scoring_opportunities[scoring_opportunity['name']] = getattr(self,
                                                                                  scoring_opportunity['func'])()

    def show_scoring_choices(self):
        i = 0
        for key, value in self.scoring_opportunities.items():
            if value:
                points = self.get_points(key)
                print(str(i) + " " + key + " " + str(points))
                i += 1

    def get_points(self, lookup):
        row = next(item for item in self.table if item["name"] == lookup)

        match lookup:

            case 'Six_of_a_kind' | 'Two_triplets' | 'Five_of_a_kind' | 'Straight' | 'Three_pairs' | \
                 'Four_of_a_kind_and_a_pair' | 'Four_of_a_kind' | 'Three_6s' | 'Three_5s' | 'Three_4s' | 'Three_3s' | \
                 'Three_1s' | 'Three_2s':
                return row['value']
            case 'Single_1':
                return row['value'] * self.current_roll.count(1)
            case 'Single_5':
                return row['value'] * self.current_roll.count(1)

    @property
    def is_farkel(self):
        for key, value in self.scoring_opportunities.items():
            if value:
                return False
        return True

    ############### roll evaluation

    def has_six_of_a_kind(self):
        if len(self.current_roll) != 6:
            return False
        # we walk down current roll with a two element window
        for x, y in zip(self.current_roll, self.current_roll[1:]):
            if x != y:
                return False

        return True

    def has_two_triplets(self):
        if len(self.current_roll) != 6:
            return False

        first_third = self.current_roll[:3]
        second_third = self.current_roll[3:]

        for x, y in zip(first_third, first_third[1:]):
            if x != y:
                return False

        for x, y in zip(second_third, second_third[1:]):
            if x != y:
                return False

        return True

    def has_five_of_a_kind(self):
        if len(self.current_roll) < 5:
            return False

        count = 0
        for x, y in zip(self.current_roll, self.current_roll[1:]):
            if x == y:
                count += 1

        if count == 4:
            return True

        return False

    def has_straight(self):
        if len(self.current_roll) < 5:
            return False

        for idx, x in enumerate(self.current_roll):
            if x != idx + 1:
                return False

        return True

    def has_three_pairs(self):
        if len(self.current_roll) != 6:
            return False

        if self.current_roll[0] == self.current_roll[1] and \
                self.current_roll[2] == self.current_roll[3] and \
                self.current_roll[4] == self.current_roll[5]:
            return True

        return False

    def has_four_of_a_kind_and_a_pair(self):
        if len(self.current_roll) != 6:
            return False

        min_value = min(self.current_roll)
        max_value = max(self.current_roll)

        if (self.current_roll.count(min_value) == 4 and self.current_roll.count(max_value) == 2) or \
                (self.current_roll.count(max_value) == 4 and self.current_roll.count(min_value) == 2):
            return True

        return False

    def has_four_of_a_kind(self):
        if len(self.current_roll) < 4:
            return False

        test_list = [1, 2, 3, 4, 5, 6]

        for x in test_list:
            if self.current_roll.count(x) == 4:
                return True

        return False

    def has_three_sixes(self):
        if len(self.current_roll) < 3:
            return False

        if self.current_roll.count(6) >= 3:
            return True

        return False

    def has_three_fives(self):
        if len(self.current_roll) < 3:
            return False

        if self.current_roll.count(5) >= 3:
            return True

        return False

    def has_three_fours(self):
        if len(self.current_roll) < 3:
            return False

        if self.current_roll.count(4) >= 3:
            return True

        return False

    def has_three_threes(self):
        if len(self.current_roll) < 3:
            return False

        if self.current_roll.count(3) >= 3:
            return True

        return False

    def has_three_twos(self):
        if len(self.current_roll) < 3:
            return False

        if self.current_roll.count(2) >= 3:
            return True

        return False

    def has_three_ones(self):
        if len(self.current_roll) < 3:
            return False

        if self.current_roll.count(1) >= 3:
            return True

        return False

    def single_ones(self):
        return self.current_roll.count(1) * 100

    def single_fives(self):
        return self.current_roll.count(5) * 50
