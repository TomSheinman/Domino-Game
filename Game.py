class Game:
    """
    This class represents a Game.
    """
    def __init__(self, board, team1, team2):
        """
        Constructor.
        :param board: Board - domino board
        :param team1: Team - first team
        :param team2: Team - second team
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """
        Method that runs the game between the two team.
        team 1 starts and after that team 2 plays, in each turn every team tries to add a domino to the
        board. the game ends if one team runs out of domino stones or if both team are out of moves.
        the Board changes according to teams plays and so does their players hands.
        :return: str - a string representing which team won / draw, a win is defined by which team has
                 the lowest score at the end of the game.
        """
        if self.team1.has_dominoes_team() and self.team2.has_dominoes_team():
            while len(self.board) < self.board.max_capacity:
                if not self.team1.play(self.board):
                    if not self.team2.play(self.board):
                        # both teams are out of moves
                        break
                    if not self.team2.has_dominoes_team():
                        break
                elif not self.team1.has_dominoes_team():
                    break
                # checks if the board is full after team 1 play
                elif len(self.board) == self.board.max_capacity:
                    break
                elif self.team2.play(self.board):
                    if not self.team2.has_dominoes_team():
                        break
        if self.team1.score_team() < self.team2.score_team():
            return f"Team {self.team1.name} wins Team {self.team2.name}"
        if self.team1.score_team() > self.team2.score_team():
            return f"Team {self.team2.name} wins Team {self.team1.name}"
        else:
            return "Draw!"
