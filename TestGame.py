from unittest import TestCase
from Domino import *
from Board import *
from Hand import *
from MaxScorePlayer import *
from NaivePlayer import *
from RandomPlayer import *
from Team import *
from Game import *


class TestGame(TestCase):
    def setUp(self):
        self.d1 = Domino(1, 1)
        self.d2 = Domino(2, 1)
        self.d3 = Domino(4, 3)
        self.d4 = Domino(6, 5)
        self.d5 = Domino(1, 4)
        self.d6 = Domino(2, 6)
        self.d7 = Domino(5, 6)
        self.d8 = Domino(6, 6)
        self.d9 = Domino(2, 2)
        self.d10 = Domino(6, 4)
        self.d11 = Domino(3, 6)
        self.d12 = Domino(5, 1)
        self.h1 = Hand([self.d1, self.d4, self.d7])
        self.ch1 = Hand([self.d1, self.d4, self.d7])
        self.h2 = Hand([self.d2, self.d5, self.d6])
        self.h3 = Hand([self.d1, self.d7, self.d8])
        self.h4 = Hand([self.d3, self.d10, self.d4])
        self.ch4 = Hand([self.d3, self.d10, self.d4])
        self.h5 = Hand([self.d9, self.d11, self.d7])
        self.h6 = Hand([self.d8, self.d1])
        self.h7 = Hand([self.d7, self.d10])
        self.np1 = NaivePlayer("Tom", 24, self.h1)
        self.cnp1 = NaivePlayer("Tom", 24, self.ch1)
        self.np2 = NaivePlayer("Omri", 52, self.h5)
        self.np3 = NaivePlayer("Yuval", 12, self.h6)
        self.np4 = NaivePlayer("David", 13, self.h7)
        self.mp1 = MaxScorePlayer("God", 23, self.h4)
        self.cmp1 = MaxScorePlayer("God", 23, self.ch4)
        self.mp2 = MaxScorePlayer("Shai", 12, self.h2)
        self.rp1 = RandomPlayer("Noga", 12, self.h3)
        self.t1 = Team("Goats", [self.np1, self.mp1, self.mp2])
        self.t2 = Team("Losers", [self.np2, self.rp1, self.cmp1])
        self.t3 = Team("No Random", [self.np2, self.cnp1, self.cmp1])
        self.t4 = Team("One", [self.cmp1])
        self.t5 = Team("L", [self.np3])
        self.t6 = Team("W", [self.np4])
        b1 = Board(1)
        b2 = Board(20)
        b3 = Board(8)
        self.g1 = Game(b1, self.t1, self.t2)
        self.g2 = Game(b2, self.t1, self.t2)
        self.g3 = Game(b2, self.t1, self.t1)
        self.g4 = Game(b2, self.t1, self.t3)
        self.g5 = Game(b3, self.t1, self.t4)
        self.g6 = Game(b3, self.t5, self.t6)
        self.g7 = Game(b3, self.t4, self.t6)

    def test_play(self):
        self.assertEqual("Draw!", self.g3.play())

    def test_play2(self):
        self.assertEqual("Team Goats wins Team Losers", self.g1.play())

    def test_play3(self):
        self.assertEqual("Team Goats wins Team Losers", self.g2.play())

    def test_play4(self):
        self.assertEqual("Team Goats wins Team No Random", self.g4.play())
        self.assertEqual(0, self.t1.score_team())
        self.assertEqual(20, self.t3.score_team())

    def test_play5(self):
        self.assertEqual("Team One wins Team Goats", self.g5.play())

    def test_play6(self):
        self.assertEqual("Team W wins Team L", self.g6.play())

    def test_play7(self):
        self.assertEqual("Team W wins Team One", self.g7.play())
