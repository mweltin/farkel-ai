class Score:
    def __init__(self):
        self.table = [
            {'name': 'Six_of_a_kind', 'value': 3000, 'min_dice_required': 6, 'func': 'has_six_of_a_kind'},
            {'name': 'Two_triplets', 'value': 2500, 'min_dice_required': 6, 'func': '' },
            {'name': 'Five_of_a_kind', 'value': 2000, 'min_dice_required': 5, 'func': '' },
            {'name': 'Straight', 'value': 1500, 'min_dice_required': 6, 'func': '' },
            {'name': 'Three_pairs', 'value': 1500, 'min_dice_required': 6, 'func': '' },
            {'name': 'Four_of_a_kind_and_a_pair', 'value': 1500, 'min_dice_required': 6, 'func': '' },
            {'name': 'Four_of_a_kind', 'value': 1000, 'min_dice_required': 4, 'func': '' },
            {'name': 'Three_6s', 'value': 600, 'min_dice_required': 3, 'func': '' },
            {'name': 'Three_5s', 'value': 500, 'min_dice_required': 3, 'func': '' },
            {'name': 'Three_4s', 'value': 400, 'min_dice_required': 3, 'func': '' },
            {'name': 'Three_3s', 'value': 300, 'min_dice_required': 3, 'func': '' },
            {'name': 'Three_1s', 'value': 300, 'min_dice_required': 3, 'func': '' },
            {'name': 'Three_2s', 'value': 200, 'min_dice_required': 3, 'func': '' },
            {'name': 'Single_1', 'value': 100, 'min_dice_required': 1, 'func': 'single_ones' },
            {'name': 'Single_5', 'value': 50, 'min_dice_required': 1, 'func': 'single_fives' },
        ]
