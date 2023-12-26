import unittest
from turn import Turn
from exception import InvalidNumberOfDice
class TestDice(unittest.TestCase):

    def test_roll_throws_excpetions_if_number_of_dice_is_zero(self):
        self.assertRaises(InvalidNumberOfDice, Turn, 0 )
    def test_roll_throws_excpetions_if_number_of_dice_is_above_six(self):
        self.assertRaises(InvalidNumberOfDice, Turn, 7 )

    def test_roll_returns_a_list_of_dice_with_elements_equal_to_the_number_of_dice(self):
        number_of_dice = 3
        turn = Turn(number_of_dice)
        turn.roll()
        self.assertEqual(len(Turn.current_role), number_of_dice)
        self.assertIsInstance(Turn.current_role, list, msg="roll did not return list")


if __name__ == '__main__':
    unittest.main()