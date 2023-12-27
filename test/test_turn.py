import unittest
from turn import Turn
from exception import InvalidNumberOfDice
class TestTurn(unittest.TestCase):

    def test_roll_throws_excpetions_if_number_of_dice_is_zero(self):
        self.assertRaises(InvalidNumberOfDice, Turn, 0 )
    def test_roll_throws_excpetions_if_number_of_dice_is_above_six(self):
        self.assertRaises(InvalidNumberOfDice, Turn, 7 )

    def test_roll_returns_a_list_of_dice_with_elements_equal_to_the_number_of_dice(self):
        number_of_dice = 3
        turn = Turn(number_of_dice)
        turn.roll()
        self.assertEqual(len(turn.current_role), number_of_dice)
        self.assertIsInstance(turn.current_role, list, msg="roll did not return list")

    def test_six_of_a_kind(self):
        turn = Turn()
        turn.current_role = [1,2,3,4]
        test_value = turn.is_six_of_a_kind()
        self.assertFalse(test_value)

        turn.current_role = [1, 2, 3, 4, 5, 6]
        test_value = turn.is_six_of_a_kind()
        self.assertFalse(test_value)

        turn.current_role = [5,5,5,5,5,5]
        test_value = turn.is_six_of_a_kind()
        self.assertTrue(test_value)

    def turn_currne_roll_setter_sorts_list_elements(self):
        test_list = [1,3,6,2,5]
        turn = Turn()
        turn._current_role = test_list
        test_value = turn.current_role
        self.assertEqual(test_value, sorted(test_list))


if __name__ == '__main__':
    unittest.main()