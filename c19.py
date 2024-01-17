#19

# 1 ------------------------------------------------------------------------------------------------

from collections import defaultdict
from operator import mul
from functools import reduce

def partAccepted(Part, Workflows):
    workflow = 'in'

    while True:
        rules, end = Workflows[workflow], False

        for rule in rules[:-1]:
            attr, operator, number, dest = rule
            condition = (lambda x: x[attr] > number) if operator == '>' else (lambda x: x[attr] < number)
            
            if condition(Part):
                if dest == 'A':
                    return True
                if dest == 'R':
                    return False

                workflow = dest
                end = True
                break

        if end:
            continue

        if (rule := rules[-1]) == 'R':
            return False
        elif rule == 'A':
            return True
        else:
            workflow = rule

    return False

with open('i19.txt', 'r') as f:
    lines = [ line.strip() for line in f.readlines() ]
    Workflows = defaultdict(list)
    breakPoint = lines.index('')

    for line in lines[:breakPoint]:
        wName, right = line.split('{')
        rules = right[:-1].split(',')
        end = rules.pop()

        for rule in rules:
            condition, dest = rule.split(':')
            Workflows[wName].append((condition[0], condition[1], int(condition[2:]), dest))

        Workflows[wName].append(end)

    totalRating = 0
    
    for line in lines[breakPoint + 1:]:
        attrs = line.lstrip('{').rstrip('}').split(',')
        Part = { attr[0] : int(attr[2:]) for attr in attrs }

        if partAccepted(Part, Workflows):
            totalRating += sum(Part.values())

    print(totalRating)

# 2 ------------------------------------------------------------------------------------------------

Paths, pathSoFar = [], []

def inverse(condition):
    return ((condition[0], '<=') + condition[2:]) if condition[1] == '>' else ((condition[0], '>=') + condition[2:])

def traverse(currentNode = 'in'):
    global Workflows, Paths, pathSoFar

    if currentNode == 'R':
        return

    if currentNode == 'A':
        Paths.append(pathSoFar[:])
        return

    node = Workflows[currentNode]

    for i, t in enumerate(node[:-1]):
        pathSoFar.extend([ inverse(x[:-1]) for x in node[:i] ])
        pathSoFar.append(t[:-1])

        traverse(t[-1])

        pathSoFar.pop()
        for _ in range(i):
            pathSoFar.pop()

    pathSoFar.extend([ inverse(x[:-1]) for x in node[:-1] ])

    traverse(node[-1])
    
    for _ in range(len(node) - 1):
        pathSoFar.pop()

traverse()

totalRating = 0

for path in Paths:
    limits = { x : [1, 4000] for x in ('x', 's', 'm', 'a') }

    for condition in path:
        if condition[1] == '<':
            limits[condition[0]][1] = min(limits[condition[0]][1], condition[2] - 1)
        elif condition[1] == '<=':
            limits[condition[0]][1] = min(limits[condition[0]][1], condition[2])
        elif condition[1] == '>':
            limits[condition[0]][0] = max(limits[condition[0]][0], condition[2] + 1)
        else:
            limits[condition[0]][0] = max(limits[condition[0]][0], condition[2])

    totalRating += reduce(mul, (v[1] - v[0] + 1 if v[1] > v[0] else 0 for v in limits.values()), 1)

print(totalRating)

#495298
#132186256794011