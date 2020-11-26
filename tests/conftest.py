
from unittest.mock import Mock

import pytest

from source.cell import Cell
from source.game_board import GameBoard
from source.game_manager import GameManager
from source.progress_status import ProgressStatus


@pytest.fixture
def cell():
    return Cell()


@pytest.fixture
def board():
    return GameBoard(3, 3)


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
