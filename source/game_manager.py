

class GameManager:

    def __init__(self, board, progress_status):
        self._board = board
        self._progress = progress_status

    def reset_game(self):
        self._reset_board()
        self._reset_progress()

    def _reset_board(self):
        self._board.reset()

    def _reset_progress(self):
        self._progress.reset()
