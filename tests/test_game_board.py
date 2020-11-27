
from source.game_board import GameBoard
from source.cell import CellCross, CellZero
from source.point import Point


def test_the_first_init_board(board):
    assert board == GameBoard(3)
    assert board.get_size() == 3


def test_set_position(board):
    assert board.set_position(Point(0, 2), CellCross()) is True
    assert isinstance(board._board[0][2], CellCross)


def test_set_position_is_busy(board):
    point = Point(2, 1)
    cell = CellZero()
    assert board.set_position(point, cell) is True
    assert board.set_position(point, cell) is False
    assert board.get_position(point) == cell


def test_reset_game_board(board):
    board.set_position(Point(0, 0), CellCross())
    board.reset()

    assert board == GameBoard(3)


def test_equals_different_boards(board):
    board.set_position(Point(0, 0), CellZero())

    assert board != GameBoard(3)


def test_get_position(board):
    board.set_position(Point(2, 1), CellCross())

    assert isinstance(board.get_position(Point(2, 1)), CellCross)


def test_check_free_cells(board):
    board.set_position(Point(1, 1), CellCross())

    assert board.check_free_cells() is True


def test_check_free_cells_is_busy(board_busy):
    assert board_busy.check_free_cells() is False
