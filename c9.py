#9

def sequenceNext1(sequence):
    if all((temp := sequence[0]) == x for x in sequence):
        return temp
    return sequence[-1] + sequenceNext1(list(map(lambda x, y: y - x, sequence[:-1], sequence[1:])))

def sequenceNext2(sequence):
    if all((temp := sequence[0]) == x for x in sequence):
        return temp
    return sequence[0] - sequenceNext2(list(map(lambda x, y: y - x, sequence[:-1], sequence[1:])))

with open('i9.txt', 'r') as f:
    lines = list(f)
    print(sum(sequenceNext1(list(map(int, x.strip().split()))) for x in lines))
    print(sum(sequenceNext2(list(map(int, x.strip().split()))) for x in lines))

    

#1806615041
#1211