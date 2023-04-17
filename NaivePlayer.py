from Player import *


class NaivePlayer(Player):
    """
    This class represents a NaivePlayer, Inherits from Player.
    """
    def __init__(self, name, age, hand):
        """
        Constructor, the class has the same attribute values as Player.
        """
        super().__init__(name, age, hand)

    def play(self, board):
        """
        Method that defines a naive player strategic play style and plays one move.
        the naive player tries to put a domino according to order of the domino's in his hand.
        if he is able to put a domino on the board that domino is removed from his hand into the board.
        :param board: Board - a domino board
        :return: bool - True - if he played his move (put a domino on the board) False - otherwise.
        """
        for domino in self.hand.array:
            if board.add(domino):
                self.hand.remove_domino(domino)
                return True
            elif board.add(domino, False):
                self.hand.remove_domino(domino)
                return True
        return False
