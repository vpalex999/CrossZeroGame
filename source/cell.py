

class Cell:
    """ Пустая ячейка """

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__

    def __repr__(self):
        return str(self.__class__.__name__)

    def __str__(self):
        return " "


class CellCross(Cell):
    """ Ячейка Х """
    def __str__(self):
        return "X"


class CellZero(Cell):
    """ Ячейка 0 """
    def __str__(self):
        return "0"
