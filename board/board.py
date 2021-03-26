import board.cell as Cell, board.section as Section
from typing import List


class BoardRow:
    def __init__(self, size: int = 3):
        self._sectionCols = [Section.Section(size) for i in range(size)]
        pass

    def columns(self, row: int) -> List[Cell.Cell]:
        cols = [sec.rows[row].cols for sec in self._sectionCols]
        return [cell for part in cols for cell in part]


class Board:
    def __init__(self, size: int = 3):
        self._boardRows = [BoardRow(size) for i in range(size)]
        pass

    def columns(self, row: int) -> List[Cell.Cell]:
        size = len(self._boardRows)
        sectId = int(row / size)
        sectRowId = row % size
        return self._boardRows[sectId].columns(sectRowId)
