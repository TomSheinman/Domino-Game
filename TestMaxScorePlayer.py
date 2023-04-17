from unittest import TestCase
from MaxScorePlayer import *
from Domino import *
from Board import *
from Hand import *


class TestMaxScorePlayer(TestCase):
    def setUp(self):
        self.d1 = Domino(1, 5)
        self.d2 = Domino(4, 4)
        self.d3 = Domino(5, 5)
        self.d4 = Domino(2, 2)
        self.d5 = Domino(6, 5)
        self.d6 = Domino(1, 3)
        self.d7 = Domino(5, 3)
        self.b1 = Board(5)
        self.b2 = Board(10)
        self.hand1 = Hand([self.d1, self.d7])
        self.hand2 = Hand([self.d1, self.d5])
        self.hand3 = Hand([self.d4, self.d2])
        self.hand4 = Hand([self.d1, self.d2, self.d3, self.d4, self.d5, self.d6])
        self.b1.add(self.d3)
        self.m_player1 = MaxScorePlayer("Tom", 24, self.hand1)
        self.m_player2 = MaxScorePlayer("Louis", 41, self.hand2)
        self.m_player3 = MaxScorePlayer("baby", 2, self.hand3)
        self.m_player4 = MaxScorePlayer("baby", 2, [])
        self.m_player5 = MaxScorePlayer("Tom", 24, self.hand4)

    def test_play(self):
        self.assertTrue(self.m_player1.play(self.b1))
        self.assertEqual("Name: Tom, Age: 24, Hand: [1|5], Score: 6, I can win the game!", str(self.m_player1))
        self.assertTrue(self.m_player2.play(self.b1))
        self.assertEqual("Name: Louis, Age: 41, Hand: [1|5], Score: 6, I can win the game!", repr(self.m_player2))
        self.assertFalse(self.m_player3.play(self.b1))
        self.assertEqual("Name: baby, Age: 2, Hand: [2|2][4|4], Score: 12, I can win the game!", repr(self.m_player3))
        self.assertFalse(self.m_player3.play(self.b1))
        self.assertEqual("Name: baby, Age: 2, Hand: [], Score: 0, I can win the game!", str(self.m_player4))
        self.assertTrue(self.m_player5.play(self.b1))
