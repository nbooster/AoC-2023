#14

def tiltPlatformVertical(platform: list, north: bool) -> None:
    L = len(platform)
    if north:
        a, b, plus, condition = 0, -1, 1, lambda x: x < L
    else:
        a, b, plus, condition = L - 1, L, -1, lambda x: x >= 0
    for j in range(len(platform[0])):
        i, currentRock = a, b
        while condition(i):
            cell = platform[i][j]
            if cell != 'O':
                if cell == '#':
                    currentRock = i
                i += plus
                continue
            platform[i][j] = '.'
            index = currentRock + plus
            platform[index][j] = 'O'
            currentRock = index
            i += plus

def tiltPlatformHorizontal(platform: list, west: bool) -> None:
    platform[:] = list(list(row) for row in zip(*platform))
    if west:
        tiltPlatformVertical(platform, True)
    else:
        tiltPlatformVertical(platform, False)
    platform[:] = list(list(row) for row in zip(*platform))

def cyclePlatform(platform: list) -> None:
    tiltPlatformVertical(platform, True)
    tiltPlatformHorizontal(platform, True)
    tiltPlatformVertical(platform, False)
    tiltPlatformHorizontal(platform, False)

def calculateNorthTotalLoad(platform: list) -> int:
    return sum((len(platform) - i) * row.count('O') for i, row in enumerate(platform))

with open('i14.txt', 'r') as f:
    platform = list(list(x.strip()) for x in f)

platformCopy = platform[:]
tiltPlatformVertical(platformCopy, True)
print(calculateNorthTotalLoad(platformCopy))
del platformCopy

R, easts, loads, start = 1_000_000_000, {}, [], 0

for i in range(R):
    cyclePlatform(platform)
    temp = tuple(tuple(row) for row in platform)
    if temp in easts:
        start = easts[temp]
        break
    easts[temp] = i
    loads.append(calculateNorthTotalLoad(platform))

del loads[:start]

print(loads[(R - start - 1) % len(loads)])

#113424
#96003