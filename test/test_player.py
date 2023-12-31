import unittest
from player import  Player
from turn import Turn
class TestTurn(unittest.TestCase):

    def test_player_initialization(self):
        player = Player()
        self.assertEqual(player.turn_score, 0)
        self.assertEqual(player.score, 0)
        self.assertIsInstance(player.turn, Turn)
        self.assertIsInstance(player.scoring_options, dict)
        self.assertTrue(player.first_turn)
        self.assertFalse(player.hit_ten_thousand)