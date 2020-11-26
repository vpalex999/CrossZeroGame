
from unittest.mock import Mock

from source.game_manager import GameManager


def test_init_game_manager(game_manager):
    assert isinstance(game_manager, GameManager)


def test_reset_board(game_manager_with_mock_args):
    g_mngr = game_manager_with_mock_args
    g_mngr._reset_board()

    g_mngr._board.reset.assert_called_once()


def test_reset_progress(game_manager_with_mock_args):

    g_mngr = game_manager_with_mock_args
    g_mngr._reset_progress()

    g_mngr._progress.reset.assert_called_once()


def test_reset_game(game_manager_with_mock_args):
    g_mngr = game_manager_with_mock_args
    g_mngr.reset_game()

    g_mngr._board.reset.assert_called_once()
    g_mngr._progress.reset.assert_called_once()
