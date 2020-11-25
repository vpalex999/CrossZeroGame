

class Cell:
    """
    _status = состояние ячейки.
    - 1: крестик.
    - 0: нолик.
    - None: начальное состояние


    """

    def __init__(self):
        self._status = None

    def get_status(self):
        return self._status

    def set_cross(self):
        if self._status is None:
            self._status = 1

    def set_zero(self):
        if self._status is None:
            self._status = 0

    def reset(self):
        self._status = None
