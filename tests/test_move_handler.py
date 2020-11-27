
from source.move_handler import MoveHandler
from source.cell import CellCross
from source.point import Point


def test_init_move_handler(move):
    assert isinstance(move, MoveHandler)


def test_make_move(move):

    assert move.make_move(Point(2, 2)) is True
    assert move._board.get_position(Point(2, 2)) == CellCross()


def test_all_cells_is_busy(board_busy, progress_status):
    move = MoveHandler(board_busy, progress_status)

    assert move.make_move(Point(1, 1)) is False
    assert move._board.get_position(
        Point(2, 2)) == progress_status.get_status()


def test_move_cell_which_selected(move):
    point = Point(2, 2)
    assert move.make_move(point) is True
    assert move.make_move(point) is False


def test_move_when_full_board(board_busy, progress_status):
    move = MoveHandler(board_busy, progress_status)
    assert move.is_full_board() is True


def test_set_position(move):
    assert move._set_position(Point(0, 0)) is True
