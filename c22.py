#22

# 1 ------------------------------------------------------------------------------------------------

with open('i22.txt', 'r') as f:
    Bricks = tuple(sorted((tuple(tuple(int(i) for i in x.split(',')) for x in row.strip().split('~')) for row in f), key = lambda t: t[0][2]))
    LB = len(Bricks)

def cross(b1, b2):
    start1, end1 = b1
    start2, end2 = b2

    xs1, ys1, zs1 = start1
    xe1, ye1, ze1 = end1
    xs2, ys2, zs2 = start2
    xe2, ye2, ze2 = end2

    def between(a, b, c):
        return (a <= b <= c) or (c <= b <= a)

    if ys1 == ye1: # H
        if ys2 == ye2: # H
            temp = (ys1 == ys2) and (between(xs1, xs2, xe1) or between(xs1, xe2, xe1) or between(xs2, xs1, xe2) or between(xs2, xe1, xe2))
        else: # V
            temp = between(xs1, xs2, xe1) and between(ys2, ys1, ye2)
    else: # V
        if ys2 == ye2: # H
            temp = between(xs2, xs1, xe2) and between(ys1, ys2, ye1)
        else: # V
            temp = (xs1 == xs2) and (between(ys1, ys2, ye1) or between(ys1, ye2, ye1) or between(ys2, ys1, ye2) or between(ys2, ye1, ye2))

    return temp

Above, Beyond, Levels, top = {}, {}, [set() for _ in range(max(t[1][-1] for t in Bricks))], 0

def putBrick(brick, level):
    for i in range(level, level + abs(brick[1][-1] - brick[0][-1]) + 1):
        Levels[i].add(brick)
    return i

putBrick(Bricks[0], 0)

for brick in Bricks[1:]:
    for index in range(top, -1, -1):
        if any(cross(b, brick) for b in Levels[index]):
            top = max(top, putBrick(brick, index + 1))
            break
    else:
        top = max(top, putBrick(brick, 0))

for index, level in enumerate(Levels[:top + 1]):
    for brick in level:
        Above[brick] = set( b for b in Levels[index + 1] if cross(brick, b) and brick != b )

for index in range(top, 0, -1):
    for brick in Levels[index]:
        Beyond[brick] = set( b for b in Levels[index - 1] if cross(brick, b) and brick != b )

disintegrated = sum( int(all( len(Beyond[b]) > 1 for b in Above[brick] )) for brick in Bricks )

print(disintegrated)

# 2 ------------------------------------------------------------------------------------------------

def fallen(brick):

    toFall = set( ab for ab in Above[brick] if len(Beyond[ab]) == 1 )
    totalFall = toFall.copy()

    while True:
        newToFall = set( b for fb in toFall for b in Above[fb] if Beyond[b].issubset(totalFall))
        toFall = newToFall
        totalFall.update(newToFall)

        if not newToFall:
            break

    return len(totalFall)

totalToFall = sum(fallen(brick) for brick in Bricks)

print(totalToFall)

#407
#59266