from Player import *
import copy


class MaxScorePlayer(Player):
    """
    This class represents a MaxScorePlayer, Inherits from Player.
    """
    def __init__(self, name, age, hand):
        """
        Constructor, the class has the same attribute values as Player.
        """
        super().__init__(name, age, hand)

    def play(self, board):
        """
        Method that defines a Max Score Player strategic play style and plays one move.
        the Max Score Player tries to lower his score as much as he can on every move,
        According to that he will try to get rid of the highest scored domino first.
        that is way the method first sort his hand from the highest scored domino to the lowest and then the
        player plays his move.
        if he is able to put a domino on the board that domino is removed from his hand into the board.
        :param board: Board - a domino board
        :return: bool - True - if he played his move (put a domino on the board), False - otherwise.
        """
        max_hand = copy.copy(self.hand.array)
        max_hand.sort(reverse=True)
        for domino in max_hand:
            if board.add(domino):
                self.hand.remove_domino(domino)
                return True
            elif board.add(domino, False):
                self.hand.remove_domino(domino)
                return True
        return False

    def __str__(self):
        """
        str function override.
        :return:
        """
        return f"Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}, " \
               f"I can win the game!"
