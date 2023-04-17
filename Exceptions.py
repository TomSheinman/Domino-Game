class EmptyBoardException(Exception):
    """
    Exception class - will raise when the board is empty.
    """
    pass


class FullBoardException(Exception):
    """
    Exception class - will raise when the board is full and domino cant be added.
    """
    pass


class NoSuchDominoException(Exception):
    """
    Exception class - will raise when the board is full.
    """
    pass


class InvalidNumberException(Exception):
    """
    Exception class - will a number is out of range.
    """
    def __init__(self, text_error):
        """
        Constructor.
        :param text_error: string - an error message
        """
        self.text_error = text_error

    def __str__(self):
        """
        str function override - returns an "ERROR " + the the sent error message
        """
        return "ERROR " + self.text_error
