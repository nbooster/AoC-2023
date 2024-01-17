#4

import re

with open('i4.txt', 'r') as f:
    result = 0
    for line in f:
        left, right = line.split('|')
        _, left = left.split(':')
        winning, mine = set(re.findall(r'\d+', left)), set(re.findall(r'\d+', right))
        matches = len(winning & mine)
        result += (2**(matches - 1) if matches > 0 else 0)
    print(result)


# not my code
matches = [len(set(line[:40].split()) & set(line[42:].split())) for line in open('i4.txt')]

cards = [1] * len(matches)
for i, n in enumerate(matches):
    for j in range(n):
        cards[i + j + 1] += cards[i]

#print(sum(2 ** (n - 1) for n in matches if n > 0))
print(sum(cards))

# 24848
# 75519888