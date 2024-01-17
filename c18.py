#18
# 1 ------------------------------------------------------------------------------------------------

with open('i18.txt', 'r') as f:
    Instructions = tuple(row.strip() for row in f)

location = [(0, 0)]

for i in Instructions:
    direction, steps, color = i.split(' ')

    if direction == 'U':
        for _ in range(int(steps)):
            location.append((location[-1][0] - 1, location[-1][1]))
    elif direction == 'D':
        for _ in range(int(steps)):
            location.append((location[-1][0] + 1, location[-1][1]))
    elif direction == 'L':
        for _ in range(int(steps)):
            location.append((location[-1][0], location[-1][1] - 1))
    else:
        for _ in range(int(steps)):
            location.append((location[-1][0], location[-1][1] + 1))

location.pop()
minX, minY = min(location, key = lambda t: t[0])[0], min(location, key = lambda t: t[1])[1]
location = [ (x - minX, y - minY) for x, y in location ]
maxX, maxY = max(location, key = lambda t: t[0])[0], max(location, key = lambda t: t[1])[1]

Grid = [['.'] * (maxY + 3) for _ in range(maxX + 3)]
for x, y in location:
    Grid[x+1][y+1] = '#'

rows, cols, area = len(Grid), len(Grid[0]), 0

for i in range(2, rows - 2):
    inside, prev1, prev2 = False, Grid[i][1], Grid[i][0]

    for j in range(2, cols - 2):

        cell = Grid[i][j]
        if cell == '.':
            if prev1 == '#':
                if prev2 == '.': 
                    inside = not inside
                else:
                    right = 'U' if Grid[i-1][j-1] == '#' else 'D'

                    for k in range(j-3, -1, -1):
                        if Grid[i][k] == '.':
                            break

                    left = 'U' if Grid[i-1][k+1] == '#' else 'D'
                    
                    if left != right:
                        inside = not inside            
            if inside:
                area += 1

        prev2 = prev1
        prev1 = cell

area += len(location)

print(area)

# 2 ----------------------------------------------------------------------------------------------

corners = [(0, 0)]

for i in Instructions:
    direction, steps, color = i.split(' ')
    distance = int('0x' + color[2:-2], base = 16)
    prev = corners[-1]

    if (d := int(color[-2])) == 0: # R
        corners.append((prev[0], prev[1] + distance))
    elif d == 1: # D
        corners.append((prev[0] + distance, prev[1]))
    elif d == 2: # L
        corners.append((prev[0], prev[1] - distance))
    else: # U
        corners.append((prev[0] - distance, prev[1]))

minX, minY = min(corners, key = lambda t: t[0])[0], min(corners, key = lambda t: t[1])[1]
corners = [ (x - minX, y - minY) for x, y in corners ]
maxX, maxY = max(corners, key = lambda t: t[0])[0], max(corners, key = lambda t: t[1])[1]

sides, prevCorner = [], corners[0]
prevVerticalMoveUp, prevHorizontalMoveRight = True, True
prevVerticalSideTypeLeft, prevHorizontalSideTypeUp = False, True

for corner in corners[1:]:
    if prevCorner[0] == corner[0]: # H
        minY, maxY = min(prevCorner[1], corner[1]), max(prevCorner[1], corner[1])

        if prevCorner[1] == minY: # R
            if prevHorizontalMoveRight:
                sides.append([ corner[0], (minY, maxY), prevHorizontalSideTypeUp ])
            else:
                prevHorizontalSideTypeUp = not prevHorizontalSideTypeUp
                prevHorizontalMoveRight = True
                sides.append([ corner[0], (minY, maxY), prevHorizontalSideTypeUp ])
        else: # L
            if prevHorizontalMoveRight:
                prevHorizontalSideTypeUp = not prevHorizontalSideTypeUp
                prevHorizontalMoveRight = False
                sides.append([ corner[0], (minY, maxY), prevHorizontalSideTypeUp ])
            else:
                sides.append([ corner[0], (minY, maxY), prevHorizontalSideTypeUp ])
    else: # V
        minX, maxX = min(prevCorner[0], corner[0]), max(prevCorner[0], corner[0])

        if prevCorner[0] == minX: # U
            if prevVerticalMoveUp:
                sides.append([ (minX, maxX), corner[1], prevVerticalSideTypeLeft ])
            else:
                prevVerticalSideTypeLeft = not prevVerticalSideTypeLeft
                prevVerticalMoveUp = True
                sides.append([ (minX, maxX), corner[1], prevVerticalSideTypeLeft ])
        else: # D
            if prevVerticalMoveUp:
                prevVerticalSideTypeLeft = not prevVerticalSideTypeLeft
                prevVerticalMoveUp = False
                sides.append([ (minX, maxX), corner[1], prevVerticalSideTypeLeft ])
            else:
                sides.append([ (minX, maxX), corner[1], prevVerticalSideTypeLeft ])
        
    prevCorner = corner

borderArea = sum(y[1] - y[0] if type(x) == int else x[1] - x[0] for x, y, z in sides)

LS = len(sides)

for i in range(LS):
    prev, curr, next = sides[i-1], sides[i], sides[(i+1) % LS]

    if type(curr[0]) == int: # H
        l, r = curr[1]

        if curr[-1]: # U
            p, n = prev[-1], next[-1]
        else: # D
            p, n = next[-1], prev[-1]
        if p and not n: # LR
            sides[i][1] = (l+1, r-1)
        elif p and n: # LL
            sides[i][1] = (l+1, r)
        elif not p and not n: # RR
            sides[i][1] = (l, r-1)

upSides = sorted([ tuple(t[:-1]) for t in sides if t[-1] and type(t[0]) == int ], reverse = True)
downSides = sorted([ tuple(t[:-1]) for t in sides if not t[-1] and type(t[0]) == int ])

def findOverlap(start1, end1, start2, end2):
    if end1 < start2 or start1 > end2:
        overlap = None
    else:
        if start1 < start2:
            overlap = (start2, min(end1, end2))
        else:
            overlap = (start1, min(end1, end2))

    return overlap

def computeNewRange(uleft, uright, dleft, dright):
    overlap = findOverlap(uleft, uright, dleft, dright)

    if overlap is None:
        return 0, ((uleft, uright), )

    oleft, oright = overlap

    return oright - oleft + 1 , tuple(t for t in ((uleft, oleft-1), (oright+1, uright)) if t[0] <= t[1])

insideArea = 0
while upSides:
    uside = upSides.pop()
    urow, uleft, uright = uside[0], *uside[1]

    for dside in downSides:
        drow, dleft, dright = dside[0], *dside[1]

        if drow <= urow:
            continue

        overlap, newUps = computeNewRange(uleft, uright, dleft, dright)

        if overlap == 0:
            continue

        upSides.extend([ (urow, t) for t in newUps ])
        insideArea += (drow - urow - 1) * overlap
        break

print(insideArea + borderArea)

#46394
#201398068194715