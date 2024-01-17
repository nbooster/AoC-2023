#21

# 1 ------------------------------------------------------------------------------------------------

with open('i21.txt', 'r') as f:
    Grid = tuple(row.strip() for row in f)
    rows, cols = len(Grid), len(Grid[0])
    for i,v in enumerate(Grid):
        if 'S' in v:
            start = (i, v.index('S'))
            break

def neighbors(row, col):
    return tuple((x, y) for x, y in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)) if 0 <= x < rows and 0 <= y < cols and Grid[x][y] != '#')


steps, cells = 15, set([start])

for i in range(steps):
    cells = set( n for cell in cells for n in neighbors(*cell) )

print(len(cells))

# 2 ------------------------------------------------------------------------------------------------

MAX = 1000

def neighbors1(row, col):
    return tuple((x, y) for x, y in (((row-1) % rows, col), ((row+1) % rows, col), (row, (col-1) % cols), (row, (col+1) % cols)) if Grid[x][y] != '#')

def tilesSteps(start):
    cells, tiles = set([start]), {0 : 1}#, set([(start,)])
    for step in range(1, MAX + 1):
        cells = set( n for cell in cells for n in neighbors(*cell) )
        #tiles[step] = len(cells)
        if len(cells) == 7699:
            return step #break
        '''prev = len(reachedSet)
        reachedSet.add(tuple(cells))
        if prev == len(reachedSet):
            break'''
    return 0#tiles#[step-1]

'''D = {}
for i in range(rows):
    cellLeft, cellRight = (i, 0), (i, cols-1)
    D[cellLeft] = tiles(cellLeft)
    D[cellRight] = tiles(cellRight)

for j in range(cols):
    cellUp, cellDown = (0, j), (rows-1, j)
    D[cellUp] = tiles(cellUp)
    D[cellDown] = tiles(cellDown)

for key, value in D.items():
    print(key, len(value))'''

a = set()
for i in range(rows):
    a.add(tilesSteps((i, cols-1)))

print(a)

#3770
#