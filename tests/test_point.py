
from source.point import Point


def test_init_point():
    point = Point('1', 2)

    assert point.row, point.column == (1, 2)
