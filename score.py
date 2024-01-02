class Score:
    def __init__(self):
        self.table = [
            {'name': 'Six_of_a_kind', 'value': 3000, 'min_dice_required': 6, 'func': 'has_six_of_a_kind'},
            {'name': 'Two_triplets', 'value': 2500, 'min_dice_required': 6, 'func': 'has_two_triplets' },
            {'name': 'Five_of_a_kind', 'value': 2000, 'min_dice_required': 5, 'func': 'has_five_of_a_kind' },
            {'name': 'Straight', 'value': 1500, 'min_dice_required': 6, 'func': 'has_straight' },
            {'name': 'Three_pairs', 'value': 1500, 'min_dice_required': 6, 'func': 'has_three_pairs' },
            {'name': 'Four_of_a_kind_and_a_pair', 'value': 1500, 'min_dice_required': 6, 'func': 'has_four_of_a_kind_and_a_pair' },
            {'name': 'Four_of_a_kind', 'value': 1000, 'min_dice_required': 4, 'func': 'has_four_of_a_kind' },
            {'name': 'Three_6s', 'value': 600, 'min_dice_required': 3, 'func': 'has_three_sixes' },
            {'name': 'Three_5s', 'value': 500, 'min_dice_required': 3, 'func': 'has_three_fives' },
            {'name': 'Three_4s', 'value': 400, 'min_dice_required': 3, 'func': 'has_three_fours' },
            {'name': 'Three_3s', 'value': 300, 'min_dice_required': 3, 'func': 'has_three_threes' },
            {'name': 'Three_1s', 'value': 300, 'min_dice_required': 3, 'func': 'has_three_ones' },
            {'name': 'Three_2s', 'value': 200, 'min_dice_required': 3, 'func': 'has_three_twos' },
            {'name': 'Single_1', 'value': 100, 'min_dice_required': 1, 'func': 'single_ones' },
            {'name': 'Single_5', 'value': 50, 'min_dice_required': 1, 'func': 'single_fives' },
        ]
