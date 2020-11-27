

class Point:

    def __init__(self, row, column):
        self._row = row
        self._column = column

    @property
    def row(self):
        return int(self._row)

    @property
    def column(self):
        return int(self._column)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.row},{self.column}"

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.column == other.column
