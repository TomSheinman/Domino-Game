from unittest import TestCase
from Collection import *

Collection1 = Collection(["I", "Domino", None, 1])
Collection2 = Collection(["I", "Domino", None, 1])
Collection3 = Collection([(1, 5), (5, 4)])
Collection4 = Collection([])


class TestCollection(TestCase):
    def test_get_collection(self):
        self.assertEqual(["I", "Domino", None, 1], Collection1.get_collection(), 0)

    def test_add(self):
        self.assertRaises(NotImplementedError, Collection([1]).add, 2, 3)

    def test_getitem(self):
        self.assertEqual(None, Collection1[5])
        self.assertEqual("Domino", Collection1[1])

    def test_ne(self):
        self.assertFalse(Collection1 != Collection2)
        self.assertTrue(Collection1 != Collection3)
        self.assertTrue(Collection1 == Collection2)
        self.assertTrue(Collection1 != ["I", "Domino", None, 1])

    def test_len(self):
        self.assertEqual(4, len(Collection1))
        self.assertEqual(0, len(Collection4))

    def test_contains(self):
        self.assertTrue((1, 5) in Collection3)
        self.assertFalse(1 in Collection4)

    def test_repr(self):
        self.assertTrue('IDominoNone1', repr(Collection1))
