import board.cell, board.section as section, board.board as layout, board.builder as builder

c = board.cell.Cell()
print(c.possibles)

print(c.hasResolved(), c.resolvedValue())

c.reduce([1, 3, 5])
print(c.possibles)

s = section.Section()
s.print()

s.rows[0].cols[0].setValue(3)
s.print()

s.reduce()
s.print()

l = layout.BoardRow()
c = l.columns(0)

print(c)

b = layout.Board()
for i in range(9):
    start = i
    row = b.columns(i)
    for cell in row:
        cellValue = start % 9
        cell.setValue(cellValue + 1)


def displaySect(b, row, col):
    sec1 = b._boardRows[row]._sectionCols[col]
    sec1.print()

displaySect(b, 0, 1)

sample = "034060901700012680080009000023050790007020005500078030010590000000000413078130020"
b = builder.Builder.buildPuzzle(sample)
displaySect(b, 2, 0)





"""

print (ls)
l = section.getResolvedValues(ls)
print (l)
"""
