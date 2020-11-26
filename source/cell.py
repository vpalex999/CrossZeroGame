

class Cell:
    """ Пустая ячейка """

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


class CellCross(Cell):
    """ Ячейка Х """


class CellCZero(Cell):
    """ Ячейка 0 """
