#12

import itertools

def pack_n_items_in_k_piles(N, K):
    return set(i for i in itertools.permutations(tuple(range(N + 1)) * K, K) if sum(i) == N)
    '''if N == 0:
        return 1
    if N == 1:
        return K
    return pack_n_items_in_k_piles(N-1, K-1) + pack_n_items_in_k_piles(N-K, K)'''
    

def match(line, record):
    assert(len(line) == len(record))
    return all(r == '?' or l == r for l, r in zip(line, record))

def produceLines(group, length):
    cells = length - sum(group) - len(group) + 1
    assert(cells >= 0)
    arrangements = pack_n_items_in_k_piles(cells, len(group) + 1)
    lines = []
    for arrangement in arrangements:
        current = [arrangement[0] * '.']
        for i, x in enumerate(arrangement[1:-1]):
            current.extend(['#' * group[i], (x + 1) * '.'])
        current.extend(['#' * group[-1], arrangement[-1] * '.'])
        lines.append(''.join(current))
    return lines



with open('i12.txt', 'r') as f:
    result = 0

    for i, row in enumerate(f):
        record, group = row.strip().split(' ')
        group = tuple(map(int, group.split(',')))
        print(i, record, group)
        result += sum(int(match(line, record)) for line in produceLines(group, len(record)))

print(result)
#print(produceLines((1,1,3), 7))

#
#