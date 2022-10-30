from Game_main import Player
import unittest

class TestLoto(unittest.TestCase):

    def setUp(self):
        self.player1 = Player('Alex',True)
        self.player2 = Player('PC',False)

    def test_init(self):
        with self.assertRaises(ValueError):
            player = Player(1, 1)
        with self.assertRaises(ValueError):
            player = Player(1, 0)
        with self.assertRaises(ValueError):
            player = Player(1, 'a')
        with self.assertRaises(ValueError):
            player = Player(1, 'True')
        with self.assertRaises(ValueError):
            player = Player(1, 'False')

    def test_property(self):
        self.assertEqual(self.player1.is_human, True)
        self.assertEqual(self.player2.is_human, False)

    def test_setter(self):
        self.player1.is_human = False
        self.player2.is_human = True
        self.assertEqual(self.player1.is_human, False)
        self.assertEqual(self.player2.is_human, True)
        with self.assertRaises(ValueError):
            self.player1.is_human = 1
        with self.assertRaises(ValueError):
            self.player1.is_human = 0
        with self.assertRaises(ValueError):
            self.player1.is_human = 'a'
        with self.assertRaises(ValueError):
            self.player1.is_human = 'True'
        with self.assertRaises(ValueError):
            self.player1.is_human = 'False'