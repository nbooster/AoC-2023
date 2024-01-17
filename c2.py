#2

import re

with open('i2.txt', 'r') as f:
    result = 0
    for line in f.readlines():
        valid = True
        game, subsets_list = line.split(':')
        _, gid = game.split(' ')
        for subset in subsets_list.split(';'):
            for cubes in subset.split(','):
                if ('red' in cubes and int(re.findall(r'\d+', cubes)[0]) > 12) or \
                   ('green' in cubes and int(re.findall(r'\d+', cubes)[0]) > 13) or \
                   ('blue' in cubes and int(re.findall(r'\d+', cubes)[0]) > 14):
                    valid = False
                    break
        if valid:
            result += int(gid)

    print(result)
                    
        
with open('i2.txt', 'r') as f:
    result = 0
    for line in f.readlines():
        game, subsets_list = line.split(':')
        minr = minb = ming = 0
        for subset in subsets_list.split(';'):
            for cubes in subset.split(','):
                if 'red' in cubes and (r := int(re.findall(r'\d+', cubes)[0])) > minr:
                    minr = r
                elif 'green' in cubes and (g := int(re.findall(r'\d+', cubes)[0])) > ming:
                    ming = g
                elif 'blue' in cubes and (b := int(re.findall(r'\d+', cubes)[0])) > minb:
                    minb = b
        result += minr * ming * minb
    print(result)
        
        
# 1931
# 83105
