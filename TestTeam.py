from unittest import TestCase
from Domino import *
from Board import *
from Hand import *
from MaxScorePlayer import *
from NaivePlayer import *
from RandomPlayer import *
from Team import *


class TestTeam(TestCase):
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
        self.h2 = Hand([self.d2, self.d5, self.d6])
        self.h3 = Hand([self.d1, self.d7, self.d8])
        self.h4 = Hand([self.d3, self.d10, self.d4])
        self.h5 = Hand([self.d9, self.d11, self.d7])
        self.np1 = NaivePlayer("Tom", 24, self.h1)
        self.np2 = NaivePlayer("Omri", 52, self.h5)
        self.mp1 = MaxScorePlayer("God", 23, self.h4)
        self.mp2 = MaxScorePlayer("Shai", 12, self.h2)
        self.rp1 = RandomPlayer("Noga", 12, self.h3)
        self.t1 = Team("Goats", [self.np1, self.mp1, self.rp1])
        self.t2 = Team("Losers", [])

    def test_get_Team(self):
        self.assertEqual(str([self.np1, self.mp1, self.rp1]), str(self.t1.get_team()))

    def test_score_team(self):
        self.assertEqual(77, self.t1.score_team())
        self.assertEqual(0, self.t2.score_team())

    def test_has_dominoes_team(self):
        self.assertTrue(self.t1.has_dominoes_team())
        self.assertFalse(self.t2.has_dominoes_team())

    def test_play(self):
        self.b1 = Board(5)
        self.b1.add(self.d2)
        self.b1.add(self.d5)
        self.b1.add(self.d9, False)
        self.assertFalse(self.t2.play(self.b1))
        self.assertTrue(self.t1.play(self.b1))
        self.assertEqual(repr(self.t1), 'Name Goats, Score team: 67, Players:'
                         ' Name: Tom, Age: 24, Hand: [1|1][6|5][5|6], Score: 24 '
                         'Name: God, Age: 23, Hand: [4|3][6|5], Score: 18, I can win the game! '
                         'Name: Noga, Age: 12, Hand: [1|1][5|6][6|6], Score: 25')



