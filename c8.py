#8

from math import lcm

def func(Map, instructions, start):
    L, steps, current = len(instructions), 0, start
    while True:
        current = Map[current][0 if instructions[steps % L] == 'L' else 1]
        steps += 1
        if current[-1] == 'Z':
            return steps

with open('i8.txt', 'r') as f:
    Map, instructions = {}, f.readline().strip()
    L = len(instructions)
    f.readline()
    
    for x in f.readlines():
        key, temp = x.strip().split(' = ')
        left, right = temp.split(', ')
        Map[key] = (left[1:], right[:-1])

    steps, current = 0, 'AAA'
    while current != 'ZZZ':
        current = Map[current][0 if instructions[steps % L] == 'L' else 1]
        steps += 1
    print(steps)

    print(lcm(*[ func(Map, instructions, start) for start in filter(lambda node: node[-1] == 'A', Map.keys()) ]))
    

#14257
#16187743689077