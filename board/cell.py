from typing import List;


class Cell:
    def __init__(self, size: int = 9):
        self.possibles = [i for i in range(1, size +1)]

    def setValue(self, v: int) -> None: self.possibles = [v]

    def hasResolved(self) -> bool:
        return len(self.possibles) == 1;

    def resolvedValue(self) -> List[int]:
        return self.possibles[0] if self.hasResolved() else None

    def reduce(self, values: List[int]) -> bool:
        curSize = len(self.possibles);
        self.possibles = [item for item in self.possibles if item not in values]
        return len(self.possibles) < curSize

    def print (self) -> None:
        print (self.possibles)
