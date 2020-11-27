
from unittest.mock import Mock

import pytest

from source.cell import Cell, CellCross
from source.game_board import GameBoard
from source.win_handler import WinHandler
from source.game_manager import GameManager
from source.move_handler import MoveHandler
from source.progress_status import ProgressStatus


@pytest.fixture
def cell():
    return Cell()


@pytest.fixture
def board():
    return GameBoard(3)


@pytest.fixture
def board_busy(board):
    board._board = [[CellCross() for _ in range(board._size)]
                    for _ in range(board._size)]
    return board


@pytest.fixture
def progress_status():
    return ProgressStatus()


@pytest.fixture
def game_manager(board, progress_status):
    return GameManager(board, progress_status)


@pytest.fixture
def game_manager_with_mock_args():
    board = Mock()
    progress = Mock()

    return GameManager(board, progress)


@pytest.fixture
def move(board, progress_status):
    return MoveHandler(board, progress_status)


@pytest.fixture
def win_handler(board, progress_status):
    return WinHandler(board, progress_status)
