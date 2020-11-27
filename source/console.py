
from source.point import Point
from source.game_board import GameBoard
from source.progress_status import ProgressStatus
from source.game_manager import GameManager
from source.move_handler import MoveHandler
from source.win_handler import WinHandler


class ConsoleGame:

    def __init__(self):
        self._board = GameBoard(3)
        self._progress_status = ProgressStatus()
        self._game_mngr = GameManager(self._board, self._progress_status)
        self._move_handler = MoveHandler(self._board, self._progress_status)
        self._win_handler = WinHandler(self._board, self._progress_status)

    def _show_board(self):

        print("  ", end='')
        for i in range(self._board.get_size()):
            print(str(i) + " ", end="")
        print()

        for count, row in enumerate(self._board._board):
            print(f"{count}|", end="")
            for column in row:
                print(str(column) + "|", end='')
            print()

    def _get_input_point(self):
        raw_point = input(
            f"q - выход; Ход игрока {self._progress_status.get_status()}:")

        if 'q' in raw_point:
            exit(0)

        row, column = raw_point.strip().replace(" ", '')
        return Point(row, column)

    def _is_continue(self) -> bool:
        if 'y' in input("Продолжить y/n?: "):
            self._game_mngr.reset_game()
            return True
        return False

    def _check_win(self, point):
        if self._win_handler.get_win(point):
            self._show_board()
            print(f"Игрок {self._progress_status.get_status()} выиграл")
            return True
        return False

    def _check_drawn_game(self):
        if self._move_handler.is_full_board():
            self._show_board()
            print("Ничья")
            return True
        return False

    def run(self):
        while True:
            self._show_board()
            point = self._get_input_point()
            if self._move_handler.make_move(point):
                if self._check_win(point):
                    if self._is_continue():
                        continue
                    break
                if self._check_drawn_game():
                    if self._is_continue():
                        continue
                    break
                self._progress_status.step()
