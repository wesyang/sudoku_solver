import board.cell, board.section as section, board.board as layout;

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
        start += 1

sec1 = b._boardRows[1]._sectionCols[0]
sec1.print()

"""

print (ls)
l = section.getResolvedValues(ls)
print (l)
"""
