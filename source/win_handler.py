
from source.point import Point
from source.progress_status import ProgressStatus


class WinHandler:

    def __init__(self, board, progress: ProgressStatus):
        self._board = board
        self._progress = progress

    def get_win(self, point):

        return all([cell == self._progress.get_status()
                    for cell in self._get_row(point)]) or \
            all([cell == self._progress.get_status()
                 for cell in self._get_column(point)]) or \
            all([cell == self._progress.get_status()
                 for cell in self._get_left_diagonal()]) or \
            all([cell == self._progress.get_status()
                 for cell in self._get_right_diagonal()])

    def _get_row(self, point):
        cells = []

        for column in range(self._board.get_size()):
            cells.append(self._board.get_position(Point(point.row, column)))

        return tuple(cells)

    def _get_column(self, point):
        cells = []

        for row in range(self._board.get_size()):
            cells.append(self._board.get_position(Point(row, point.column)))

        return tuple(cells)

    def _get_left_diagonal(self):
        cells = []

        for i in range(self._board.get_size()):
            cells.append(self._board.get_position(Point(i, i)))

        return tuple(cells)

    def _get_right_diagonal(self):
        cells = []

        for i in range(self._board.get_size()):
            cells.append(self._board.get_position(
                Point(i, self._board.get_size() - i - 1)))

        return tuple(cells)
