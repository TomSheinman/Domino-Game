from Exceptions import *


class Domino:
    """
    This class represents a Domino.
    """
    def __init__(self, left, right):
        """
        constructor.
        :param left: int - the left side of the domino stone, if not in range 0-6 raises InvalidNumberException.
        :param right: int - the right side of the domino stone, if not in range 0-6 raises InvalidNumberException.
        """
        if left not in range(7):
            raise InvalidNumberException("Left integer out of range")
        if right not in range(7):
            raise InvalidNumberException("Right integer out of range")
        self.__left_side = left
        self.__right_side = right

    def get_left(self):
        """
        :return: Method that returns the left side of the domino stone.
        """
        return self.__left_side

    def get_right(self):
        """
        :return: Method that returns the right side of the domino stone.
        """
        return self.__right_side

    def __str__(self):
        """
        str function override - returns the str representation of the domino as [left_side|right_side]
        """
        return f"[{self.__left_side}|{self.__right_side}]"

    def __repr__(self):
        """
        print function override using str function.
        """
        return str(self)

    def __eq__(self, other):
        """
        == operator overload
        :param other: object - an object to check equality with self, if both objects have the same values they're equal
        :return: bool - True if equal False otherwise
        """
        if not isinstance(other, Domino):
            return False
        if self.__left_side == other.get_left() and self.__right_side == other.get_right():
            return True
        elif self.__right_side == other.get_left() and self.__left_side == other.get_right():
            return True
        return False

    def __ne__(self, other):
        """
        != operator overload
        :param other: object - an object to check inequality with self, checks using opposite of == operator
        """
        return not self == other

    def flip(self):
        """
        Method that flips the domino and returns the flipped object
        :return: Domino - the flipped object where the stone values are the opposite of self
        """
        flipped_left = self.__right_side
        flipped_right = self.__left_side
        flipped = Domino(flipped_left, flipped_right)
        return flipped

    def __gt__(self, other):
        """
        > operator overload
        :param other: an object to check if its smaller than self, determined by sum of both sides
        :return: bool - True if self is bigger than other, otherwise False
        """
        if not isinstance(other, Domino):
            return False
        return self.__left_side + self.__right_side > other.get_left() + other.get_right()

    def __contains__(self, key):
        """
        checks if key is in one of the sides of the domino
        :param key: int
        :return: bool - True or false
        """
        return key == self.__left_side or key == self.__right_side

