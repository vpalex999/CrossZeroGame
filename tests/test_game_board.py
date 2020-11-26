
from source.game_board import GameBoard
from source.cell import CellCross, CellCZero


def test_the_first_init_board(board):
    assert board == GameBoard(3, 3)


def test_reset_game_board(board):
    board.set_position(0, 0, CellCross)
    board.reset()

    assert board == GameBoard(3, 3)


def test_equals_different_boards(board):
    board.set_position(0, 0, CellCZero)

    assert board != GameBoard(3, 3)


def test_get_position(board):
    board.set_position(2, 1, CellCross)

    assert isinstance(board.get_position(2, 1), CellCross)
