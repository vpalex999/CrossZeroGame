
from source.cell import CellCross
from source.cell import CellZero


def test_init_progress_status(progress_status):
    assert isinstance(progress_status._status, CellCross)


def test_check_turn_to_next_player(progress_status):
    progress_status.step()
    assert isinstance(progress_status._status, CellZero)


def test_serial_turn_next_player(progress_status):
    progress_status.step().step()

    assert isinstance(progress_status._status, CellCross)


def test_make_reset_progress_status(progress_status):
    progress_status.step().reset()

    assert isinstance(progress_status._status, CellCross)


def test_get_status(progress_status):
    progress_status.step()

    assert isinstance(progress_status.get_status(), CellZero)
