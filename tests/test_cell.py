

from source.cell import CellCross, CellCZero, Cell


def test_init_cell(cell):

    assert cell == Cell()


def test_cells_is_equals():
    cell_1 = CellCross()
    cell_2 = CellCross()

    assert cell_1 == cell_2


def test_cells_is_not_equals():
    cell_1 = CellCross()
    cell_2 = CellCZero()

    assert (cell_1 == cell_2) is False
