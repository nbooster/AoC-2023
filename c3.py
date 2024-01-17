#3
'''
import re

def check(array, row, start, end):
    indices = ((row, start-1), (row-1, start-1), (row+1, start-1), (row, end), (row-1, end), (row+1, end)) + \
        tuple((row-1, i) for i in range(start, end)) + tuple((row+1, i) for i in range(start, end))

    for i, j in indices:
        if (char := array[i][j]) != '.' and not char.isdigit():
            return True

    return False

with open('i3e.txt', 'r') as f:
    result, indices, lines = 0, [], []

    for index, line in enumerate(f.readlines()):
        line_fixed = '.' + line + '.'
        lines.append(line_fixed)
        for m in re.finditer(r'\d+', line_fixed):
            indices.append((index + 1, m.start(), m.end()))

    lines.insert(0, '.' * len(line_fixed))
    lines.append('.' * len(line_fixed))

    for i, j, e in indices:
        if check(lines, i, j, e):
            result += int(lines[i][j:e]);print(int(lines[i][j:e]))

    print(result)'''
                    
        
#with open('i3.txt', 'r') as f:
    #result = 0
    #for line in f.readlines():
        
    #print(result)
        
        
# 1931
# 75519888

#not my code
import math as m, re

board = list(open('i3.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140) if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1) for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p) for p in chars.values()), sum(m.prod(p) for p in chars.values() if len(p) == 2))

# 509115 75220503