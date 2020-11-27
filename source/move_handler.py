

class MoveHandler:

    def __init__(self, board, progress_status):
        self._board = board
        self._progress = progress_status

    def make_move(self, point) -> bool:

        if self._set_position(point):
            return True
        return False

    def is_full_board(self) -> bool:
        return not self._board.check_free_cells()

    def _set_position(self, point) -> bool:
        target_cell = self._progress.get_status()
        return self._board.set_position(point, target_cell)
