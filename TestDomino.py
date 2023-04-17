from unittest import TestCase
from Domino import *
from Exceptions import *

Domino1 = Domino(1, 5)
Domino2 = Domino(5, 1)
Domino3 = Domino(4, 3)
Domino4 = Domino(1, 5)


class TestDomino(TestCase):
    def test_init(self):
        self.assertRaises(InvalidNumberException, Domino, 7, 1)
        self.assertRaises(InvalidNumberException, Domino, 6, -1)

    def test_get_left(self):
        self.assertEqual(1, Domino1.get_left())

    def test_get_right(self):
        self.assertEqual(5, Domino1.get_right())

    def test_repr(self):
        self.assertEqual("[1|5]", repr(Domino1))

    def test_flip(self):
        self.assertEqual("[5|1]", repr(Domino1.flip()))

    def test_ne_eq_gt(self):
        self.assertTrue(Domino1 == Domino2)
        self.assertTrue(Domino1 != Domino3)
        self.assertTrue(Domino1 == Domino4)
        self.assertTrue(Domino3 > Domino1)
        self.assertFalse(Domino3 > 4)
        self.assertFalse(Domino3 == 4)

    def test_contains(self):
        self.assertTrue(1 in Domino1)
