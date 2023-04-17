from unittest import TestCase
from RandomPlayer import *
from Hand import *
from Domino import *
from Board import *


class TestRandomPlayer(TestCase):
    def setUp(self):
        self.do1 = Domino(5, 2)
        self.do2 = Domino(1, 1)
        self.do3 = Domino(4, 3)
        self.do4 = Domino(5, 2)
        self.do5 = Domino(3, 6)
        self.do6 = Domino(6, 4)
        self.do7 = Domino(5, 5)
        self.b1 = Board(6)
        self.b2 = Board(4)
        self.ha1 = Hand([self.do1, self.do2, self.do3])
        self.ha2 = Hand([])
        self.ha3 = Hand([self.do7, self.do2])
        self.ha4 = Hand([self.do1, self.do2, self.do3, self.do4, self.do5])
        self.b1.add(self.do5)
        self.b1.add(self.do6)
        self.b2.add(self.do7)
        self.r_player1 = RandomPlayer("Tom", 24, self.ha1)
        self.r_player2 = RandomPlayer("Noga", 23, self.ha2)
        self.r_player3 = RandomPlayer("Ronaldo", 10, self.ha3)
        self.r_player4 = RandomPlayer("Messi", 35, self.ha4)

    def test_play(self):
        self.assertTrue(self.r_player1.play(self.b1))
        self.assertFalse(self.r_player2.play(self.b1))
        self.assertTrue(self.r_player1.play(self.b2))
        self.assertTrue(self.r_player3.play(self.b2))
        self.assertTrue(self.r_player4.play(self.b1))
