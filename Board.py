from Collection import Collection
from Exceptions import *


class Board(Collection):
    """
     This class represents a Board, inherits from Collection.
     """
    def __init__(self, max_capacity):
        """
        Constructor. array will set as an empty list.
        :param max_capacity: int - in range between 1 and 28, represents the max number of domino's that can be in board
        if int not in range 1 to 28 InvalidNumberException will raise
        """
        super().__init__(self)
        if max_capacity not in range(1, 29):
            raise InvalidNumberException("Inserted integer not in range 1-28!")
        self.max_capacity = max_capacity
        self.array = []

    def in_left(self):
        """
        Method that returns the left_side integer of the far left stone in board.
        :return: exception - if board is empty, int - value of far left stone in board
        """
        if not self.array:
            raise EmptyBoardException("Board is empty!")
        else:
            return self.array[0].get_left()

    def in_right(self):
        """
        Method that returns the right_side integer of the far right stone in board.
        :return: exception - if board is empty, int - value of far right stone in board
        """
        if not self.array:
            raise EmptyBoardException("Board is empty!")
        else:
            return self.array[-1].get_right()

    def add(self, domino, add_to_right=True):
        """
        Method that adds domino stone to the board if its legal, uses add_left, add_right methods to add in each side
        :param domino: Domino - a domino stone wished to add to the board
        :param add_to_right: bool - if add to right is True the method tries to add to the right side of the board
                                    else tries to add to the left side of the board.
        :return: Exception - if the board is full, else, True - if adding was successful, False otherwise
        """
        if self.max_capacity == len(self):
            raise FullBoardException("Board is full!")
        if add_to_right:
            return self.add_right(domino)
        return self.add_left(domino)

    def add_left(self, domino):
        """
        Method that tries to add a domino to the board on the left side, at first it tries to add it in it original
        form, if that is not successful it tries to add it using the flip method.
        :return: True if successful, False otherwise
        """
        flipped = domino.flip()
        if not self.array or domino.get_right() == self.in_left():
            self.array.insert(0, domino)
            return True
        elif flipped.get_right() == self.in_left():
            self.array.insert(0, flipped)
            return True
        return False

    def add_right(self, domino):
        """
        Method that tries to add a domino to the board on the right side, at first it tries to add it in it original
        form, if that is not successful it tries to add it using the flip method.
        :return: True if successful, False otherwise
        """
        flipped = domino.flip()
        if not self.array or domino.get_left() == self.in_right():
            self.array.append(domino)
            return True
        elif flipped.get_left() == self.in_right():
            self.array.append(flipped)
            return True
        return False

    def __eq__(self, other):
        """
        == operator overload
        :param other: object - an object to check equality with self, if both objects have the same max capacity,
        and same arrays(domino's in matching places and order)
        :return: bool - True if equal False otherwise
        """
        if not isinstance(other, Board):
            return False
        if self.max_capacity == other.max_capacity and len(self.array) == len(other.array):
            for i in range(len(self.array)):
                if self.array[i].get_left != other.array[i].get_left or self.array[i].get_right != other.array[i].get_right:
                    return False
            return True
        return False
