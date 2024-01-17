#6

import re
from math import sqrt, ceil

with open('i6.txt', 'r') as f:
    times = tuple(map(int, re.findall(r'\d+', f.readline())))
    dists = tuple(map(int, re.findall(r'\d+', f.readline())))

result = 1

for T, D in zip(times, dists):
    lower = 0.5 * (T - sqrt(T * T - 4 * D))
    upper = 0.5 * (sqrt(T * T - 4 * D) + T)
    dist_exclusive = int(upper) - ceil(lower) + 1
    if lower == int(lower):
        dist_exclusive -= 1
    if upper == int(upper):
        dist_exclusive -= 1
    result *= dist_exclusive
    #print(dist_exclusive)

print(result)

with open('i6.txt', 'r') as f:
    T = int(''.join(re.findall(r'\d+', f.readline())))
    D = int(''.join(re.findall(r'\d+', f.readline())))

lower = 0.5 * (T - sqrt(T * T - 4 * D))
upper = 0.5 * (sqrt(T * T - 4 * D) + T)
dist_exclusive = int(upper) - ceil(lower) + 1
if lower == int(lower):
    dist_exclusive -= 1
if upper == int(upper):
    dist_exclusive -= 1
print(dist_exclusive)

#6209190
#28545089