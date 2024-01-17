#15

def HASH(s):
    value = 0
    for c in s:
        value = ((value + ord(c)) * 17) % 256
    return value

with open('i15.txt', 'r') as f:
    steps = f.readline().strip().split(',')

print(sum(HASH(step) for step in steps))

from collections import OrderedDict

boxes = [OrderedDict() for _ in range(256)]

for step in steps:
    if '-' in step:
        label = step[:-1]
        boxes[HASH(label)].pop(label, None)
    else:
        label, focus = step[:-2], int(step[-1])
        boxes[HASH(label)][label] = focus

print(sum((i + 1) * (j + 1) * value for i, box in enumerate(boxes) for j, value in enumerate(box.values())))

#519603
#244342