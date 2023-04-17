import copy


class Team:
    """
    This class represents a Team.
    """
    def __init__(self, name, players):
        """
        Constructor.
        :param name: str - Team name
        :param players: list - List of Players
        """
        self.name = name
        self.__players = players

    def get_team(self):
        """
        Method that returns a deepcopy of the list of players
        """
        return copy.deepcopy(self.__players)

    def score_team(self):
        """
        Method that sum the score of every player in the team and returns the score of the team
        :return: int - the team score
        """
        summer = 0
        for player in self.__players:
            summer += player.score()
        return summer

    def has_dominoes_team(self):
        """
        Method that checks if a team has domino's
        :return: True - if there is at least one player with domino, False - if the team has no domino's
        """
        for player in self.__players:
            if player.has_dominoes():
                return True
        return False

    def play(self, board):
        """
        Method that plays one move for the team, the first player who can play for the team (according to players list)
        plays his move, after then that team turn to play ends.
        :param board: Domino Board, if a player on the team can play his domino is added to the board
        :return: True - if a move was made, False - otherwise
        """
        for player in self.__players:
            if player.play(board):
                return True
        return False

    def __str__(self):
        """
        str function override.
        """
        str_player = ""
        for player in self.__players:
            str_player += str(player) + " "
        return f"Name {self.name}, Score team: {self.score_team()}, Players: {str_player.strip()}"

    def __repr__(self):
        """
        print function override using str function.
        """
        return str(self)
