import unittest
from bowling import Game


class GameTest(unittest.TestCase):
    def test_all_ones(self):
        game = Game(roll_many("1", 20))
        self.assertEqual(game.score(), 20)

    def test_gutter_game(self):
        game = Game(roll_many("-", 20))
        self.assertEqual(game.score(), 0)


    def test_spare(self):
        game = Game("4/34" + roll_many("-", 16))
        self.assertEqual(game.score(), 20)

    def test_strike(self):
        game = Game("X34" + roll_many("-", 16))
        self.assertEqual(game.score(), 24)


    def test_always_normal(self):
        game = Game("12345123451234512345")
        self.assertEqual(game.score(), 60)

    def test_perfect_game(self):
        game = Game("XXXXXXXXXXXX")
        self.assertEqual(game.score(), 300)

    def test_heartbreak_game(self):
        game = Game("9-9-9-9-9-9-9-9-9-9-")
        self.assertEqual(game.score(), 90)

    def test_spare_game(self):
        game = Game("5/5/5/5/5/5/5/5/5/5/5")
        self.assertEqual(game.score(), 150)

def roll_many(roll, times):
    return roll * times

if __name__ == '__main__':
    unittest.main()