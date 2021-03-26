import board.cell as Cell
from typing import List


class SectionRow:
    def __init__(self, size: int = 3):
        self.cols = [Cell.Cell(size * size) for i in range(size)]

    def resolvedItems(self) -> List[Cell.Cell]:
        return [cell for cell in self.cols if cell.hasResolved()]

    def print(self) -> None:
        print([cell.possibles for cell in self.cols])


class Section:
    def __init__(self, size: int = 3):
        self.rows = [SectionRow(size) for i in range(size)]

    def resolvedItems(self) -> List[Cell.Cell]:
        return [cell for row in self.rows
                for cell in row.cols if cell.hasResolved()]

    def reduce(self) -> List[bool]:
        resolvedValues = getResolvedValues(self.resolvedItems())
        result = [cell.reduce(resolvedValues) for row in self.rows
                  for cell in row.cols if not cell.hasResolved()]
        return result

    def print(self) -> None:
        [row.print() for row in self.rows]
        print("----------------------")


def getResolvedValues(items: List[Cell.Cell]) -> List[int]: return [i.resolvedValue() for i in items]
