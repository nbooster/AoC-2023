#7

from functools import cmp_to_key
from collections import Counter

cards = 'AKQJT98765432'

cardPowers = { v : 13 - i for i, v in enumerate(cards) }
#;cardPowers['J'] = 0  # 2

def handType1(hand):
    C = Counter(hand)
    values = C.values()
    if 5 in values:
        return 7
    if 4 in values:
        return 6
    if 3 in values:
        if 2 in values:
            return 5
        return 4
    if 2 in values:
        if len(values) == 3:
            return 3
        return 2
    return 1

def handType2(hand):
    if 'J' not in hand:
        return handType1(hand)
    C = Counter(hand)
    Js = C['J']
    del C['J']
    values = C.values()
    if Js in (4, 5):
        return 7
    if Js == 3:
        if 2 in values:
            return 7
        return 6
    if Js == 2:
        if 3 in values:
            return 7
        if 2 in values:
            return 6
        return 4
    if 4 in values:
        return 7
    if 3 in values:
        return 6
    if 2 in values:
        if 1 in values:
            return 4
        return 5
    return 2


def handCompare(tupleA, tupleB):
    handA, handB = tupleA[0], tupleB[0]
    typeA, typeB = handType1(handA), handType1(handB) # handType2 --> 2
    if typeA < typeB:
        return -1
    elif typeA > typeB:
        return 1
    else:
        t1 = tuple(cardPowers[card] for card in handA)
        t2 = tuple(cardPowers[card] for card in handB)
        if t1 < t2:
            return -1
        elif t1 > t2:
            return 1
        else:
            return 0
    

with open('i7.txt', 'r') as f:
    hands = list(x.split() for x in f.readlines())

hands.sort(key = cmp_to_key(handCompare))#;print([x[0] for x in hands])

total = 0
for i, v in enumerate(hands):
    total += (i + 1) * int(v[1])

print(total)

#251121738
#251421071