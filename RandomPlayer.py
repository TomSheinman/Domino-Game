import random
import copy
from Player import Player


class RandomPlayer(Player):
    """
    This class represents a RandomPlayer, Inherits from Player.
    """
    def __init__(self, name, age, hand):
        """
        Constructor, the class has the same attribute values as Player.
        """
        super().__init__(name, age, hand)

    def play(self, board):
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        """
        Method that defines a random player strategic play style and plays one move.
        the random player tries to put a domino on the board after randomly shuffling his hand.
        if he is able to put a domino on the board that domino is removed from his hand into the board.
        :param board: Board - a domino board
        :return: bool - True - if he played his move (put a domino on the board), False - otherwise.
        """
        shuffle_hand = copy.copy(self.hand.array)
        random.shuffle(shuffle_hand)
        for domino in shuffle_hand:
            if board.add(domino):
                self.hand.remove_domino(domino)
                return True
            elif board.add(domino, False):
                self.hand.remove_domino(domino)
                return True
        return False
