import unittest
from turn import Turn
from turn.exception import InvalidNumberOfDice, InvalidDieValue


class TestTurn(unittest.TestCase):

    def test_roll_throws_exceptions_if_number_of_dice_is_zero(self):
        self.assertRaises(InvalidNumberOfDice, Turn, 0)

    def test_roll_throws_exceptions_if_number_of_dice_is_above_six(self):
        self.assertRaises(InvalidNumberOfDice, Turn, 7)

    def test_roll_throws_exceptions_if_roll_has_an_invalid_die(self):
        turn = Turn
        self.assertRaises(InvalidDieValue, Turn.current_role.__set__, turn, [1, 2, 7])
        self.assertRaises(InvalidDieValue, Turn.current_role.__set__, turn, [1, 2, -1])
        self.assertRaises(InvalidDieValue, Turn.current_role.__set__, turn, [1, 0, 1])

    def test_roll_returns_a_list_of_dice_with_elements_equal_to_the_number_of_dice(self):
        number_of_dice = 3
        turn = Turn(number_of_dice)
        turn.roll()
        self.assertEqual(len(turn.current_role), number_of_dice)
        self.assertIsInstance(turn.current_role, list, msg="roll did not return list")

    def test_six_of_a_kind(self):
        turn = Turn()
        turn.current_role = [1, 2, 3, 4]
        test_value = turn.has_six_of_a_kind()
        self.assertFalse(test_value)

        turn.current_role = [1, 2, 3, 4, 5, 6]
        test_value = turn.has_six_of_a_kind()
        self.assertFalse(test_value)

        turn.current_role = [5, 5, 5, 5, 5, 5]
        test_value = turn.has_six_of_a_kind()
        self.assertTrue(test_value)

    def turn_current_roll_setter_sorts_list_elements(self):
        test_list = [1, 3, 6, 2, 5]
        turn = Turn()
        turn._current_role = test_list
        test_value = turn.current_role
        self.assertEqual(test_value, sorted(test_list))

    def test_two_triplets(self):
        turn = Turn()
        turn.current_role = [1, 2, 3, 4]
        test_value = turn.has_two_triplets()
        self.assertFalse(test_value)

        turn.current_role = [1, 6, 6, 4, 5, 6]
        test_value = turn.has_two_triplets()
        self.assertFalse(test_value)

        turn.current_role = [1, 6, 6, 1, 1, 6]
        test_value = turn.has_two_triplets()
        self.assertTrue(test_value)

    def test_has_five_of_a_kind(self):
        turn = Turn()
        turn.current_role = [1, 2, 3, 4]
        test_value = turn.has_five_of_a_kind()
        self.assertFalse(test_value)

        turn.current_role = [1, 2, 3, 4, 5]
        test_value = turn.has_five_of_a_kind()
        self.assertFalse(test_value)

        turn.current_role = [1, 2, 2, 2, 2, 2]
        test_value = turn.has_five_of_a_kind()
        self.assertTrue(test_value)

        turn.current_role = [6, 6, 6, 1, 6, 6]
        test_value = turn.has_five_of_a_kind()
        self.assertTrue(test_value)

    def test_has_straight(self):
        turn = Turn()
        turn.current_role = [1, 2, 3, 4]
        test_value = turn.has_straight()
        self.assertFalse(test_value)

        turn.current_role = [1, 2, 3, 3, 4, 5]
        test_value = turn.has_straight()
        self.assertFalse(test_value)

        turn.current_role = [1, 3, 5, 2, 4, 6]
        test_value = turn.has_straight()
        self.assertTrue(test_value)

    def test_has_three_pairs(self):
        turn = Turn()
        turn.current_role = [1, 2, 3, 4]
        test_value = turn.has_three_pairs()
        self.assertFalse(test_value)

        turn.current_role = [1, 2, 3, 3, 4, 5]
        test_value = turn.has_three_pairs()
        self.assertFalse(test_value)

        turn.current_role = [1, 2, 3, 1, 2, 3]
        test_value = turn.has_three_pairs()
        self.assertTrue(test_value)

        turn.current_role = [2, 2, 2, 2, 2, 2]
        test_value = turn.has_three_pairs()
        # technically true but why would you score it that way
        self.assertTrue(test_value)

    def test_has_four_of_a_kind_and_a_pair(self):
        turn = Turn()
        turn.current_role = [1, 2, 3, 4]
        test_value = turn.has_four_of_a_kind_and_a_pair()
        self.assertFalse(test_value)

        turn.current_role = [1, 1, 1, 1, 4, 5]
        test_value = turn.has_four_of_a_kind_and_a_pair()
        self.assertFalse(test_value)

        turn.current_role = [1, 3, 3, 1, 3, 3]
        test_value = turn.has_four_of_a_kind_and_a_pair()
        self.assertTrue(test_value)

        turn.current_role = [1, 3, 1, 3, 1, 1]
        test_value = turn.has_four_of_a_kind_and_a_pair()
        self.assertTrue(test_value)

    def test_has_four_of_a_kind(self):
        turn = Turn()
        turn.current_role = [1, 2, 3]
        test_value = turn.has_four_of_a_kind()
        self.assertFalse(test_value)

        turn.current_role = [5, 3, 5, 6, 1, 5]
        # technically true but why would you score 4 of a kind and a pair this way
        test_value = turn.has_four_of_a_kind()
        self.assertFalse(test_value)

        turn.current_role = [1, 3, 1, 6, 1, 1]
        # technically true but why would you score 4 of a kind and a pair this way
        test_value = turn.has_four_of_a_kind()
        self.assertTrue(test_value)

        turn.current_role = [1, 3, 1, 3, 1, 1]
        # technically true but why would you score 4 of a kind and a pair this way
        test_value = turn.has_four_of_a_kind()
        self.assertTrue(test_value)

    def test_has_three_sixes(self):
        turn = Turn()
        turn.current_role = [1, 2]
        test_value = turn.has_three_sixes()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [1, 1, 1]
        test_value = turn.has_three_sixes()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [6, 6, 6, 6]
        test_value = turn.has_three_sixes()
        self.assertTrue(test_value)

        turn = Turn()
        turn.current_role = [1, 6, 6, 6]
        test_value = turn.has_three_sixes()
        self.assertTrue(test_value)

    def test_has_three_fives(self):
        turn = Turn()
        turn.current_role = [1, 2]
        test_value = turn.has_three_fives()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [1, 1, 1]
        test_value = turn.has_three_fives()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [5, 5, 5, 5]
        test_value = turn.has_three_fives()
        self.assertTrue(test_value)

        turn = Turn()
        turn.current_role = [1, 5, 5, 5]
        test_value = turn.has_three_fives()
        self.assertTrue(test_value)

    def test_has_three_fours(self):
        turn = Turn()
        turn.current_role = [1, 2]
        test_value = turn.has_three_fours()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [1, 1, 1]
        test_value = turn.has_three_fours()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [4, 4, 4, 4]
        test_value = turn.has_three_fours()
        self.assertTrue(test_value)

        turn = Turn()
        turn.current_role = [1, 4, 4, 4]
        test_value = turn.has_three_fours()
        self.assertTrue(test_value)

    def test_has_three_threes(self):
        turn = Turn()
        turn.current_role = [1, 2]
        test_value = turn.has_three_threes()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [1, 1, 1]
        test_value = turn.has_three_threes()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [3, 3, 3, 3]
        test_value = turn.has_three_threes()
        self.assertTrue(test_value)

        turn = Turn()
        turn.current_role = [1, 3, 3, 3]
        test_value = turn.has_three_threes()
        self.assertTrue(test_value)

    def test_has_three_twos(self):
        turn = Turn()
        turn.current_role = [1, 2]
        test_value = turn.has_three_twos()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [1, 1, 1]
        test_value = turn.has_three_twos()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [2, 2, 2, 2]
        test_value = turn.has_three_twos()
        self.assertTrue(test_value)

        turn = Turn()
        turn.current_role = [1, 2, 2, 2]
        test_value = turn.has_three_twos()
        self.assertTrue(test_value)

    def test_has_three_ones(self):
        turn = Turn()
        turn.current_role = [1, 2]
        test_value = turn.has_three_ones()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [2, 2, 2]
        test_value = turn.has_three_ones()
        self.assertFalse(test_value)

        turn = Turn()
        turn.current_role = [1, 1, 1, 1]
        test_value = turn.has_three_ones()
        self.assertTrue(test_value)

        turn = Turn()
        turn.current_role = [1, 1, 1, 1]
        test_value = turn.has_three_ones()
        self.assertTrue(test_value)

    def test_single_ones(self):
        turn = Turn()
        test_list = [5, 5, 5, 6]
        turn.current_role = test_list
        test_value = turn.single_ones()
        actual_value = test_list.count(1) * 100
        self.assertEqual(test_value, actual_value)

        test_list = [1, 5, 5, 6]
        turn.current_role = test_list
        test_value = turn.single_ones()
        actual_value = test_list.count(1) * 100
        self.assertEqual(test_value, actual_value)

        test_list = [5, 5, 1, 1, 1, 6]
        turn.current_role = test_list
        test_value = turn.single_ones()
        actual_value = test_list.count(1) * 100
        self.assertEqual(test_value, actual_value)

    def test_single_fives(self):
        turn = Turn()
        test_list = [1, 1, 1, 6]
        turn.current_role = test_list
        test_value = turn.single_fives()
        actual_value = test_list.count(5) * 50
        self.assertEqual(test_value, actual_value)

        test_list = [5, 1, 1, 6]
        turn.current_role = test_list
        test_value = turn.single_fives()
        actual_value = test_list.count(5) * 50
        self.assertEqual(test_value, actual_value)

        test_list = [1, 1, 5, 5, 5, 6]
        turn.current_role = test_list
        test_value = turn.single_fives()
        actual_value = test_list.count(5) * 50
        self.assertEqual(test_value, actual_value)

    def test_reset_score_opportunities(self):
        turn = Turn()
        turn.scoring_opportunities = ('Six_of_a_kind', True)
        turn.reset_score_opportunities()
        self.assertFalse(turn.scoring_opportunities['Six_of_a_kind'])

    def test_find_valid_scoring_opportunities(self):
        turn = Turn()
        test_list = [2, 2, 2, 2, 2, 2]
        turn.current_role = test_list
        turn.find_valid_scoring_opportunities()
        self.assertTrue(turn.scoring_opportunities['Six_of_a_kind'])




if __name__ == '__main__':
    unittest.main()
