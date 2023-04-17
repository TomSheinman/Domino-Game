from unittest import TestCase
from Board import *
from Domino import *

a = Board(15)
b = Board(15)
c = Board(15)
d = Board(15)
Board1 = Board(4)
Board2 = Board(1)
Board3 = Board(4)
d1 = Domino(1, 5)
d2 = Domino(5, 4)
d3 = Domino(1, 2)
d4 = Domino(3, 4)
d5 = Domino(4, 3)


class TestBoard(TestCase):
    def test_init(self):
        self.assertRaises(InvalidNumberException, Board, 0)
        self.assertEqual([], Board(1).get_collection())

    def test_add(self):
        self.assertTrue(Board1.add(d1, True))
        self.assertTrue(Board1.add(d2, True))
        self.assertTrue(Board2.add(d2, False))
        self.assertTrue(a.add(d4, True))
        self.assertTrue(b.add(d4, True))
        self.assertTrue(c.add(d5, True))
        self.assertRaises(FullBoardException, Board2.add, d1, False)
        self.assertRaises(FullBoardException, Board2.add, d1, True)

    def test_add_left(self):
        self.assertTrue(Board1.add_left(d3))
        self.assertFalse(Board1.add_left(d2))

    def test_add_right(self):
        self.assertTrue(Board1.add_right(d4))
        self.assertFalse(b.add_right(d1))

    def test_in_left(self):
        self.assertRaises(EmptyBoardException, Board(10).in_left)
        self.assertTrue(2, Board1.in_left())

    def test_in_right(self):
        self.assertRaises(EmptyBoardException, Board(5).in_right)
        self.assertTrue(3, Board1.in_right())

    def test_father_meth(self):
        self.assertTrue(4, len(Board1))
        self.assertEqual(1, len(Board2))
        self.assertEqual(str(Board1), '[2|1][1|5][5|4][4|3]')
        self.assertEqual(repr(Board2), '[5|4]')
        self.assertTrue(Board2 != Board1)

    def test_eq(self):
        self.assertFalse(Board3 == 3)
        self.assertTrue(a == b)
        self.assertTrue(b != c)
