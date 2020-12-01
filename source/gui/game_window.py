

import tkinter as tk
import tkinter.messagebox as messagebox

from source.point import Point
from source.game_board import GameBoard
from source.progress_status import ProgressStatus
from source.game_manager import GameManager
from source.move_handler import MoveHandler
from source.win_handler import WinHandler

from source.cell import Cell


class CoreGame:

    def __init__(self, size=3):
        self._size = size
        self._board = GameBoard(self._size)
        self._progress_status = ProgressStatus()
        self._move_handler = MoveHandler(self._board, self._progress_status)
        self._win_handler = WinHandler(self._board, self._progress_status)
        self._game_mngr = GameManager(self._board, self._progress_status)

    def get_size(self):
        return self._size

    @property
    def board(self):
        return self._board

    @property
    def progress_status(self):
        return self._progress_status

    @property
    def move_handler(self):
        return self._move_handler

    @property
    def win_handler(self):
        return self._win_handler

    @property
    def game_manager(self):
        return self._game_mngr

    def make_move(self, point):
        return self._move_handler.make_move(point)

    def full_board(self):
        return self._move_handler.is_full_board()

    def get_current_player(self):
        return self._progress_status.get_status()

    def next_player(self):
        self._progress_status.step()

    def current_player_win(self, point):
        return self._win_handler.get_win(point)

    def reset_game(self):
        self._game_mngr.reset_game()


class GameWindow(tk.Frame):

    padNSWE = dict(sticky=(tk.N, tk.S, tk.E, tk.W), padx="0.5m", pady="0.5m")

    def __init__(self, root=None, size=3):
        super().__init__(root)
        self._size = size
        self._core = CoreGame(self._size)
        self._current_player = tk.StringVar()

        self._create_playing_area()
        self._create_status_bar()
        self._init_layout()

    def _create_playing_area(self):
        self._playing_area = WindowArea(
            self._size, self.make_move, self.master)
        self._playing_area.grid(row=0, column=0, **self.padNSWE)

    def _create_status_bar(self):
        status_bar = tk.Frame(self.master)
        status_label = tk.Label(status_bar, textvariable=self._current_player)
        status_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        status_bar.columnconfigure(0, weight=1)
        status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self._set_current_player()

    def _set_current_player(self):
        self._current_player.set(
            f"Игрок: {self._core.get_current_player()}")

    def _init_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.master.columnconfigure(0, weight=2)
        self.master.rowconfigure(0, weight=2)
        self.master.minsize(100, 100)

    def make_move(self, point):
        if self._core.make_move(point):
            self._playing_area.set_position(
                point, self._core.get_current_player())

            if self._core.current_player_win(point):
                messagebox.showinfo(
                    f"Игрок {self._core.get_current_player()} выиграл")
                self._reset_game()
                return
            if self._core.full_board():
                messagebox.showinfo("Ничья")
                self._reset_game()
                return
            self._core.next_player()
            self._set_current_player()

    def _reset_game(self):
        self._core.reset_game()
        self._playing_area.init_board()
        self._set_current_player()


class WindowArea(tk.Frame):

    padWE = dict(sticky=(tk.N, tk.S, tk.E, tk.W), padx="0.5m", pady="0.5m")

    def __init__(self, size, routine_make_move, root=None):
        super().__init__(root)
        self._size = size
        self._routine_make_move = routine_make_move

        self._board_variables = self._create_board_variables()
        self._board_buttons = self._create_board_buttons()
        self.init_board()
        self._init_layout()

    def init_board(self):

        for num_row in range(self._size):
            for num_col in range(self._size):
                self._board_variables[num_row][num_col].set(Cell())

    def set_position(self, point, cell):
        self._board_variables[point.row][point.column].set(cell)

    def _init_layout(self):
        self._colums_configure()
        self._rows_configure()
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.master.columnconfigure(0, weight=2)
        self.master.rowconfigure(0, weight=2)

    def _create_board_variables(self):
        return [[tk.StringVar() for _ in range(self._size)]
                for _ in range(self._size)]

    def _create_board_buttons(self):

        return [[self._make_btn(row, column) for column in range(self._size)]
                for row in range(self._size)]

    def _make_btn(self, row, column):
        _btn = tk.Button(
            self, textvariable=self._board_variables[row][column],
            command=lambda: self._make_move(Point(row, column)))

        _btn.grid(row=row, column=column, **self.padWE)

    def _rows_configure(self):
        [self.rowconfigure(num_col, weight=1)
         for num_col in range(self._size)]

    def _colums_configure(self):
        [self.columnconfigure(num_col, weight=1)
         for num_col in range(self._size)]

    def _make_move(self, point):
        self._routine_make_move(point)
