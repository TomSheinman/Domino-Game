from unittest import TestCase
from NaivePlayer import *
from Hand import *
from Domino import *
from Board import *


class TestPlayer(TestCase):
    def setUp(self):
        self.do1 = Domino(1, 2)
        self.do2 = Domino(3, 4)
        self.do3 = Domino(5, 6)
        self.hand1 = Hand([self.do1, self.do2, self.do3])
        self.hand2 = Hand([])
        self.b1 = Board(5)
        self.n_player1 = NaivePlayer("Tom", 24, self.hand1)
        self.n_player2 = NaivePlayer("Omri", 52, self.hand2)

    def test_score(self):
        self.assertEqual(21, self.n_player1.score())
        self.assertEqual(0, self.n_player2.score())

    def test_has_dominoes(self):
        self.assertFalse(self.n_player2.has_dominoes())
        self.assertTrue(self.n_player1.has_dominoes())
        self.assertTrue(self.n_player1.play(self.b1))

    def test_str(self):
        self.assertEqual("Name: Tom, Age: 24, Hand: [1|2][3|4][5|6], Score: 21", str(self.n_player1))
        self.assertEqual("Name: Omri, Age: 52, Hand: "", Score: 0", repr(self.n_player2))
