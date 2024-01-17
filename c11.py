#11

with open('i11.txt', 'r') as f:
    Space = []
    emptyRows, emptyCols = set(), set()
    for i, row in enumerate(f):
        Space.append(row)
        if '#' not in row:
            Space.append(row)
            emptyRows.add(i)
    TransSpace = zip(*Space)
    Space = []
    for i, row in enumerate(TransSpace):
        Space.append(row)
        if '#' not in row:
            Space.append(row)
            emptyCols.add(i)
    Space = zip(*Space)

Galaxies = [ (i, j) for i, row in enumerate(Space) for j, cell in enumerate(row) if cell == '#' ]
minPathsSum = 0

for i in range(len(Galaxies) - 1):
    for j in range(i+1, len(Galaxies)):
        galI, galJ = Galaxies[i], Galaxies[j]
        minPathsSum += abs(galI[0] - galJ[0]) + abs(galI[1] - galJ[1])

print(minPathsSum)


with open('i11.txt', 'r') as f:
    Space = list(f)

expansion = 1000000
Galaxies = [ (i, j) for i, row in enumerate(Space) for j, cell in enumerate(row) if cell == '#' ]
minPathsSum = 0

emptyRowsFromStart = [0] * (len(Space) + 1)
for i in range(len(Space)):
    if i in emptyRows:
        emptyRowsFromStart[i+1] = emptyRowsFromStart[i] + 1
    else:
        emptyRowsFromStart[i+1] = emptyRowsFromStart[i]

del emptyRowsFromStart[0]

emptyColsFromStart = [0] * (len(Space[0]) + 1)
for i in range(len(Space[0])):
    if i in emptyCols:
        emptyColsFromStart[i+1] = emptyColsFromStart[i] + 1
    else:
        emptyColsFromStart[i+1] = emptyColsFromStart[i]

del emptyColsFromStart[0]

for i in range(len(Galaxies) - 1):
    for j in range(i+1, len(Galaxies)):
        galI, galJ = Galaxies[i], Galaxies[j]
        rows, cols = abs(emptyRowsFromStart[galI[0]] - emptyRowsFromStart[galJ[0]]), abs(emptyColsFromStart[galI[1]] - emptyColsFromStart[galJ[1]])
        minPathsSum += abs(galI[0] - galJ[0]) - rows + expansion * rows + abs(galI[1] - galJ[1]) - cols + expansion * cols

print(minPathsSum)

#9418609
#593821230983