
from source.progress_status import ProgressStatus as PS
from source.cell import CellCross
from source.cell import CellCZero


def test_init_progress_status(progress_status):
    assert issubclass(progress_status._status, CellCross)


def test_check_turn_to_next_player(progress_status):
    progress_status.step()
    assert issubclass(progress_status._status, CellCZero)


def test_serial_turn_next_player(progress_status):
    progress_status.step().step()

    assert issubclass(progress_status._status, CellCross)


def test_make_reset_progress_status(progress_status):
    progress_status.step().reset()

    assert issubclass(progress_status._status, CellCross)


def test_get_status(progress_status):
    progress_status.step()

    assert issubclass(progress_status.get_status(), CellCZero)
