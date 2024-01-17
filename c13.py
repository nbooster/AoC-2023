#13

with open('i13.txt', 'r') as f:
    patterns, pattern = [], []

    for row in f:
        if len(row) == 1:
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(row.strip())

    patterns.append(pattern)

result = 0

def isReflection(pattern, row1, row2):
    return all(pattern[row1 - i] == pattern[row2 + i] for i in range(min(len(pattern) - row2, row1 + 1)))

lines = []

for pattern in patterns: 
    hMatches = [ (i, i+1) for i in range(len(pattern)-1) if pattern[i] == pattern[i+1] ]
    hMatches.sort(key = lambda t: t[0] + len(pattern) - t[1], reverse = True)
    
    hLine = None

    for hMatch in hMatches:
        if isReflection(pattern, *hMatch):
            hLine = hMatch

    if hLine != None:
        result += 100 * (hLine[0] + 1)
        lines.append(hLine + ('h',))
        continue

    pattern = tuple(zip(*pattern))

    vMatches = [ (i, i+1) for i in range(len(pattern)-1) if pattern[i] == pattern[i+1] ]
    vMatches.sort(key = lambda t: t[0] + len(pattern) - t[1], reverse = True)
    
    vLine = None

    for vMatch in vMatches:
        if isReflection(pattern, *vMatch):
            vLine = vMatch

    if vLine != None:
        result += vLine[0] + 1
        lines.append(vLine + ('v',))

print(result)

def diffs(pattern, row):
    return sum(sum(int(a != b) for a, b in zip(row1, row2)) for row1, row2 in zip(pattern[row::-1], pattern[row + 1:]))

result = 0

for line, pattern in zip(lines, patterns):
    skip = False

    for row in range(len(pattern) - 1):
        if (row, row + 1) == line:
            continue
        if diffs(pattern, row) == 1:
            result += 100 * (row + 1)
            skip = True

    if skip:
        continue

    pattern = tuple(zip(*pattern))

    for row in range(len(pattern) - 1):
        if (row, row + 1) == line:
            continue

        if diffs(pattern, row) == 1:
            result += row + 1

print(result)

#27502
#31947