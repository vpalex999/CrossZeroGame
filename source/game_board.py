
from source.cell import Cell


class GameBoard:
    """ Игровое поле """

    def __init__(self, size):
        self._size = size
        self._board = self._get_empty_board()

    def _get_empty_board(self):
        return [[Cell() for _ in range(self._size)]
                for _ in range(self._size)]

    def __eq__(self, other):
        return self._board == other._board

    def get_size(self):
        return self._size

    def set_position(self, point, cell):
        assert isinstance(cell, Cell)
        if self.get_position(point) == Cell():
            self._board[point.row][point.column] = cell
            return True
        return False

    def get_position(self, point):
        return self._board[point.row][point.column]

    def reset(self):
        self._board = self._get_empty_board()

    def check_free_cells(self):
        return any([Cell() in row for row in self._board])
