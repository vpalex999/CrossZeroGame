
import pytest

from source.cell import Cell, CellCross, CellZero
from source.point import Point
from source.win_handler import WinHandler


def test_init_win_handler(win_handler):
    assert isinstance(win_handler, WinHandler)


win_points = [
    ((Point(0, 0), Point(0, 1), Point(0, 2)), Point(0, 1)),
    ((Point(0, 2), Point(1, 2), Point(2, 2)), Point(2, 2)),
    ((Point(0, 0), Point(1, 1), Point(2, 2)), Point(0, 0)),
    ((Point(0, 2), Point(1, 1), Point(2, 0)), Point(2, 0)),
]


def test_get_win_was_win(win_handler):

    win_handler._board.set_position(Point(1, 1), CellCross())

    assert win_handler.get_win(Point(1, 1)) is False


@pytest.mark.parametrize('points, point', win_points)
def test_get_win_not_was_win(win_handler, points, point):

    [win_handler._board.set_position(point, CellCross()) for point in points]

    assert win_handler.get_win(point) is True


def test_get_row_to_filling_equals_cells(win_handler):
    points = [Point(1, 0), Point(1, 1), Point(1, 2)]
    cells = [CellCross() for _ in range(3)]
    [win_handler._board.set_position(*item) for item in zip(points, cells)]

    assert win_handler._get_row(Point(1, 1)) == tuple(cells)


def test_get_row_to_filling_no_equals_cells(win_handler):
    points = [Point(1, 0), Point(1, 1), Point(1, 2)]
    cells = [CellCross(), CellZero(), Cell()]
    [win_handler._board.set_position(*item) for item in zip(points, cells)]

    assert win_handler._get_row(Point(1, 2)) == tuple(cells)


def test_get_column_filling_equals_cells(win_handler):
    points = [Point(0, 1), Point(1, 1), Point(2, 1)]
    cells = [CellCross() for _ in range(3)]
    [win_handler._board.set_position(*item) for item in zip(points, cells)]

    assert win_handler._get_column(Point(1, 1)) == tuple(cells)


def test_get_left_diagonal(win_handler):
    points = [Point(0, 0), Point(1, 1), Point(2, 2)]
    cells = [CellCross() for _ in range(3)]
    [win_handler._board.set_position(*item) for item in zip(points, cells)]

    assert win_handler._get_left_diagonal() == tuple(cells)


def test_get_right_diagonal(win_handler):
    points = [Point(0, 2), Point(1, 1), Point(2, 0)]
    cells = [CellCross() for _ in range(3)]
    [win_handler._board.set_position(*item) for item in zip(points, cells)]

    assert win_handler._get_right_diagonal() == tuple(cells)
