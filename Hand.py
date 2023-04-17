from Collection import *
from Exceptions import *


class Hand(Collection):
    """
    This class represents a Hand, inherits from Collection.
    """
    def __init__(self, dominoes):
        """
        Constructor.
        :param dominoes: list - a list of Domino's
        """
        super().__init__(self)
        self.array = dominoes

    def add(self, domino, index=None):
        """
        Method that adds a domino into hand using index value
        :param domino: Domino - a domino stone to add to Hand
        :param index: None / int - default value is None, if None - domino added to the end of array, else domino added to index
                      location in the array
        """
        if index is None:
            self.array.append(domino)
        else:
            self.array.insert(index, domino)

    def remove_domino(self, domino):
        """
        Method that removes domino from hand
        :param domino: Domino stone to remove from Hand
        :return: Int / Exception - Int - if domino is in Hand Return the index of its location before removing it
                                   Exception - if domino isn't in Hand
        """
        if domino in self.array:
            for i in range(len(self.array)):
                if self.array[i] == domino:
                    self.array.pop(i)
                    return i
        raise NoSuchDominoException("Inserted domino not in hand")






















