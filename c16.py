#16

with open('i16.txt', 'r') as f:
    Grid = tuple(row.strip() for row in f)

def horizontal(x, y, Grid, Energized, beams, mirrorUp):
    Energized[x][y] = True
    if (cell := Grid[x][y]) in ('.', '-'):
        return False
    else:
        if cell == mirrorUp:
            beams.append((x, y, 'u'))
        elif cell == '|':
            beams.extend([(x, y, 'u'), (x, y, 'd')])
        else:
            beams.append((x, y, 'd'))
        return True

def vertical(x, y, Grid, Energized, beams, mirrorLeft):
    Energized[x][y] = True
    if (cell := Grid[x][y]) in ('.', '|'):
        return False
    else:
        if cell == mirrorLeft:
            beams.append((x, y, 'l'))
        elif cell == '-':
            beams.extend([(x, y, 'l'), (x, y, 'r')])
        else:
            beams.append((x, y, 'r'))
        return True

def intializeBeams(Grid, direction, sx, sy):
    cell = Grid[sx][sy]
    if direction == 'r':
        if cell == '|':
            return [(sx, sy, 'u'), (sx, sy, 'd')]
        elif cell == '/':
            return [(sx, sy, 'u')]
        elif cell == '\\':
            return [(sx, sy, 'd')]
        return [(sx, sy, 'r')]
    elif direction == 'l':
        if cell == '|':
            return [(sx, sy, 'u'), (sx, sy, 'd')]
        elif cell == '/':
            return [(sx, sy, 'd')]
        elif cell == '\\':
            return [(sx, sy, 'u')]
        return [(sx, sy, 'l')]
    elif direction == 'd':
        if cell == '-':
            return [(sx, sy, 'l'), (sx, sy, 'r')]
        elif cell == '/':
            return [(sx, sy, 'l')]
        elif cell == '\\':
            return [(sx, sy, 'r')]
        return [(sx, sy, 'd')]
    else:
        if cell == '-':
            return [(sx, sy, 'l'), (sx, sy, 'r')]
        elif cell == '/':
            return [(sx, sy, 'r')]
        elif cell == '\\':
            return [(sx, sy, 'l')]
        return [(sx, sy, 'u')]


def simulate(Grid, direction, sx, sy):
    beams = intializeBeams(Grid, direction, sx, sy)
    rows, cols = len(Grid), len(Grid[0]),
    seen, Energized = set(), [ [False] * cols for _ in range(rows) ]
    Energized[sx][sy] = True

    while beams:
        beam = beams.pop()

        if beam in seen:
            continue

        seen.add(beam)
        x, y, d = beam
        
        if d == 'r':
            for j in range(y + 1, cols):
                if horizontal(x, j, Grid, Energized, beams, '/'):
                    break
        elif d == 'l':
            for j in range(y - 1, -1, -1):
                if horizontal(x, j, Grid, Energized, beams, '\\'):
                    break
        elif d == 'u':
            for i in range(x - 1, -1, -1):
                if vertical(i, y, Grid, Energized, beams, '\\'):
                    break
        else:
            for i in range(x + 1, rows):
                if vertical(i, y, Grid, Energized, beams, '/'):
                    break

    return sum(int(x) for row in Energized for x in row)

maxEnergy = 0
rows, cols = len(Grid), len(Grid[0])

for i in range(rows):
    if (energy := simulate(Grid, 'r', i, 0)) > maxEnergy:
        maxEnergy = energy

    if (energy := simulate(Grid, 'l', i, cols - 1)) > maxEnergy:
        maxEnergy = energy

for j in range(cols):
    if (energy := simulate(Grid, 'd', 0, j)) > maxEnergy:
        maxEnergy = energy
        
    if (energy := simulate(Grid, 'u', rows - 1, j)) > maxEnergy:
        maxEnergy = energy

print(maxEnergy)

#6902
#7697