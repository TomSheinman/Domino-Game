from unittest import TestCase
from NaivePlayer import *
from Hand import *
from Domino import *
from Board import *


class TestNaivePlayer(TestCase):

    def setUp(self):
        self.d1 = Domino(1, 4)
        self.d2 = Domino(4, 3)
        self.d3 = Domino(5, 3)
        self.d4 = Domino(1, 2)
        self.d5 = Domino(6, 6)
        self.d6 = Domino(6, 2)
        self.b1 = Board(5)
        self.b1.add(self.d1)
        self.b1.add(self.d2)
        self.h1 = Hand([self.d3, self.d4])
        self.h2 = Hand([self.d5, self.d6])
        self.h3 = Hand([self.d4, self.d3])
        self.n_player1 = NaivePlayer("Tom", 12, self.h1)
        self.n_player2 = NaivePlayer("Tom", 24, self.h2)
        self.n_player3 = NaivePlayer("Tom", 24, self.h3)

    def test_play(self):
        self.assertTrue(self.n_player1.play(self.b1))
        self.assertFalse(self.n_player2.play(self.b1))
        self.assertTrue(self.n_player3.play(self.b1))
