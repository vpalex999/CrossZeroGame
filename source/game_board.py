
from source.cell import Cell


class GameBoard:
    """ Игровое поле """

    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._board = self._get_empty_board()

    def _get_empty_board(self):
        return [[Cell() for _ in range(self._columns)]
                for _ in range(self._rows)]

    def __eq__(self, other):
        return self._board == other._board

    def set_position(self, row, column, cell_class):
        self._board[row][column] = cell_class()

    def get_position(self, row, column):
        return self._board[row][column]

    def reset(self):
        self._board = self._get_empty_board()
