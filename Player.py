from abc import ABC, abstractmethod


class Player(ABC):
    """
    This abstract class represents a Player.
    """
    def __init__(self, name, age, hand):
        """
        Constructor.
        :param name: str - Player name
        :param age: int - Player age (0-120)
        :param hand: Hand - Player Hand, an array of Domino's
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
        Method that defines the number of points a player has.
        :return: int - the sum of the domino's values in his hand.
        """
        summer = 0
        if self.hand:
            for domino in self.hand.array:
                summer += domino.get_left() + domino.get_right()
        return summer

    def has_dominoes(self):
        """
        Method that conclude if a player has domino's in his hand.
        :return: bool - True - if he has domino's False - otherwise
        """
        if len(self.hand) == 0:
            return False
        return True

    @abstractmethod
    def play(self, board):
        """
        Abstract method. have implementation only in inheriting classes.
        """
        pass

    def __str__(self):
        """
        str function override.
        """
        return f"Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}"

    def __repr__(self):
        """
        print function override using str function.
        """
        return str(self)
