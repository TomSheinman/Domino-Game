from unittest import TestCase
from Hand import *
from Domino import *

d1 = Domino(6, 2)
d2 = Domino(1, 4)
d3 = Domino(3, 5)
d4 = Domino(5, 6)
d5 = Domino(4, 1)
Hand1 = Hand([d2, d3, d4])
Hand2 = Hand([])


class TestHand(TestCase):

    def test_add(self):
        Hand1.add(d1)
        self.assertEqual("[1|4][3|5][5|6][6|2]", str(Hand1))
        Hand1.add(d2, 1)
        self.assertEqual("[1|4][1|4][3|5][5|6][6|2]", str(Hand1))
        Hand2.add(d3, 5)
        self.assertEqual("[3|5]", repr(Hand2))

    def test_remove(self):
        self.assertEqual(0, Hand1.remove_domino(d5))
        self.assertEqual(0, Hand1.remove_domino(d5))
        self.assertEqual(3, len(Hand1))
        self.assertRaises(NoSuchDominoException, Hand1.remove_domino, d5)

    def test_father(self):
        self.assertEqual(d3, Hand1[2])
        self.assertEqual(None, Hand2[4])
        self.assertTrue(d3 in Hand1)
        self.assertTrue(d5 in Hand1)
        self.assertFalse(d5 in Hand2)
        self.assertTrue(Hand1 != Hand2)
