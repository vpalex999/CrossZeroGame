
from source.cell import CellZero, CellCross


class ProgressStatus:
    """
    Хранит статус хода
    Про инициализации ход передаётися игороку Х.

    _status: чей ход
    - 1: ход игрока Х
    - 0: ход игрока 0

    """

    def __init__(self):
        self._status = CellCross()

    def get_status(self):
        return self._status

    def step(self):
        if isinstance(self._status, CellCross):
            self._status = CellZero()
        else:
            self._status = CellCross()
        return self

    def reset(self):
        self._status = CellCross()
        return self
