#10

def nextCell(Grid, row, col, fromCell):
    cell = Grid[row][col]
    if cell == '-':
        if fromCell == 'right':
            return (row, col-1, 'right')
        else:
            return (row, col+1, 'left')
    elif cell == '|':
        if fromCell == 'up':
            return (row+1, col, 'up')
        else:
            return (row-1, col, 'down')
    elif cell == 'F':
        if fromCell == 'down':
            return (row, col+1, 'left')
        else:
            return (row+1, col, 'up')
    elif cell == 'L':
        if fromCell == 'up':
            return (row, col+1, 'left')
        else:
            return (row-1, col, 'down')
    elif cell == '7':
        if fromCell == 'left':
            return (row+1, col, 'up')
        else:
            return (row, col-1, 'right')
    elif cell == 'J':
        if fromCell == 'up':
            return (row, col-1, 'right')
        else:
            return (row-1, col, 'down')

with open('i10.txt', 'r') as f:
    Grid = list(f)

rows, cols = len(Grid), len(Grid[0])
startRow, startCol = next(((i, row.index('S')) for i, row in enumerate(Grid) if 'S' in row), None)
currNodes = []

if (r := startRow - 1) >= 0 and Grid[r][startCol] in ('|', 'F', '7'):
    currNodes.append((r, startCol, 'down'))
if (r := startRow + 1) < len(Grid) and Grid[r][startCol] in ('|', 'L', 'J'):
    currNodes.append((r, startCol, 'up'))
if (c := startCol - 1) >= 0 and Grid[startRow][c] in ('-', 'F', 'L'):
    currNodes.append((startRow, c, 'right'))
if (c := startCol + 1) < len(Grid[0]) and Grid[startRow][c] in ('-', 'J', '7'):
    currNodes.append((startRow, c, 'left'))

current1, current2 = currNodes
steps = steps1 = steps2 = 1
loop = [(startRow, startCol), currNodes[0][:-1], currNodes[1][:-1]]

while True:
    current1 = nextCell(Grid, *current1)
    steps1 += 1
    loop.append(current1[:-1])

    if current1[0:2] == current2[0:2]:
        steps = steps1
        break

    current2 = nextCell(Grid, *current2)
    steps2 += 1
    loop.append(current2[:-1])

    if current1[0:2] == current2[0:2]:
        steps = steps2
        break

print(steps)

loop.remove(loop[-1])

loop = set(loop)
Grid = [ list(row.strip()) for row in Grid ]
area = 0

for i, row in enumerate(Grid):
    inside, prev = False, None

    for j, cell in enumerate(row):
        if (i, j) in loop:
            if cell == 'S':
                cell = Grid[i][j] = '7' # find it manually
            if cell == '-':
                continue
            elif cell == '|':
                inside = not inside
            else:
                if prev is None:
                    inside = True
                elif cell in ('F', 'L'):
                    inside = not inside
                else:
                    if (prev, cell) in (('L', 'J'), ('F', '7')):
                        inside = not inside

            prev = cell

        else:
            if inside:
                area += 1
print(area)

#6773
#493