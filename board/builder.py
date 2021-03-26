import board.cell as Cell, board.section as Section, board.board as Board
from typing import List


class Builder:
    def __init__(self):
        pass

    @staticmethod
    def buildPuzzle(puzzle: str, size: int = 3) -> Board.Board:
        board = Board.Board(size)
        data = structPuzzleData(puzzle, size)
        rows = [board.columns(i) for i in range(size * size)]

        for r, dr in zip(rows, data):
            for c, dc in zip(r, dr):
                if dc != '0': c.setValue(dc)

        return board


def structPuzzleData(puzzle, size: int) -> List[List[str]]:
    data = [c for c in puzzle]
    count = size * size
    dataRows = []
    for i in range(count):
        s = i * count
        e = s + count
        row = data[s:e]
        print([c if c != '0' else '.' for c in row])
        dataRows.append(row)

    return dataRows
