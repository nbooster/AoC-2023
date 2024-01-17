#5

import re

with open('i5.txt', 'r') as f:
    lines = list(f.readlines())

seeds = tuple(int(x) for x in re.findall(r'\d+', lines[0].split(':')[1]))

StS, StF, FtW, WtL, LtT, TtH, HtL = [], [], [], [], [], [], []

i = 3
while True:
    line = lines[i]
    if len(line) == 1:
        break
    StS.append(tuple(map(int, line.split())))
    i += 1
StS.sort(key = lambda t: t[1])

i += 2
while True:
    line = lines[i]
    if len(line) == 1:
        break
    StF.append(tuple(map(int, line.split())))
    i += 1
StF.sort(key = lambda t: t[1])

i += 2
while True:
    line = lines[i]
    if len(line) == 1:
        break
    FtW.append(tuple(map(int, line.split())))
    i += 1
FtW.sort(key = lambda t: t[1])

i += 2
while True:
    line = lines[i]
    if len(line) == 1:
        break
    WtL.append(tuple(map(int, line.split())))
    i += 1
WtL.sort(key = lambda t: t[1])

i += 2
while True:
    line = lines[i]
    if len(line) == 1:
        break
    LtT.append(tuple(map(int, line.split())))
    i += 1
LtT.sort(key = lambda t: t[1])

i += 2
while True:
    line = lines[i]
    if len(line) == 1:
        break
    TtH.append(tuple(map(int, line.split())))
    i += 1
TtH.sort(key = lambda t: t[1])

i += 2
while True:
    if i >= len(lines):
        break
    line = lines[i]
    HtL.append(tuple(map(int, line.split())))
    i += 1
HtL.sort(key = lambda t: t[1])
#print(StS, StF, FtW, WtL, LtT, TtH, HtL)
lowest = HtL[0][0]

def Map(mapL, item):
    mapped = item
    for dest_start, source_start, length in mapL:
        if source_start <= item <= source_start + length:
            mapped = dest_start + (item - source_start)
            break
    return mapped

def Map2(mapL, ranges):
    mapped = []
    for range in ranges:
        start, end = range
        for dest_start, source_start, length in mapL:
            if source_start <= start <= source_start + length:
                if end <= source_start + length:
                    mapped.append((dest_start + (start - source_start), dest_start + (start - source_start) + end - start + 1))
                    break
                mapped.append((dest_start + (start - source_start), dest_start + (start - source_start) + length))
                start = dest_start + (start - source_start) + length + 1
    return mapped


for i in range(0, len(seeds), 2):
    start, length = seeds[i], seeds[i+1]

    for seed in range(start, start + length):
        soil = Map(StS, seed)
        fertilizer = Map(StF, soil)
        water = Map(FtW, fertilizer)
        light = Map(WtL, water)
        temperature = Map(LtT, light)
        humidity = Map(TtH, temperature)
        location = Map(HtL, humidity)

        if location < lowest:
            lowest = location

print(lowest)

# 24848
# 75519888