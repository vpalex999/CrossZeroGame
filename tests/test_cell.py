

def test_init_cell(cell):

    assert cell.get_status() is None


def test_set_to_cross(cell):
    cell.set_cross()

    assert cell.get_status() == 1


def test_set_zero(cell):
    cell.set_zero()

    assert cell.get_status() == 0


def test_set_busy_cross_cell(cell):
    cell.set_cross()
    cell.set_zero()

    assert cell.get_status() == 1


def test_set_busy_zero_cell(cell):
    cell.set_zero()
    cell.set_cross()

    assert cell.get_status() == 0


def test_cell_reset(cell):
    cell.set_zero()
    cell.reset()

    assert cell.get_status() is None
