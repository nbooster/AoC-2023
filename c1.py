#11

import re

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
rev_digits = [ s[::-1] for s in digits ]

def find(s: str) -> int:
    first_digit = last_digit = fdi = ldi = None

    for i, c in enumerate(s):
        if c.isdigit():
            first_digit, fdi = c, i
            break

    rev_s = s[::-1]
    
    for i, c in enumerate(rev_s):
        if c.isdigit():
            last_digit, ldi = c, len(s) - 1 - i
            break

    positions_s = []
    for i, digit in enumerate(digits):
        try:
            positions_s.append((s.index(digit), str(i + 1)))
        except ValueError:
            pass

    positions_rev_s = []
    for i, digit in enumerate(rev_digits):
        try:
            positions_rev_s.append((len(s) - 1 - len(digit) - rev_s.index(digit), str(i + 1)))
        except ValueError:
            pass

    fldi, first_letter_digit = min(positions_s, key = lambda x: x[0], default = (len(s), ''))
    lldi, last_letter_digit = max(positions_rev_s, key = lambda x: x[0], default = (-1, ''))

    if fdi < fldi:
        if ldi > lldi:
            return int(first_digit + last_digit)
        else:
            return int(first_digit + last_letter_digit)
    else:
        if ldi > lldi:
            return int(first_letter_digit + last_digit)
        else:
            return int(first_letter_digit + last_letter_digit)
    

with open('i1.txt', 'r') as f:
    s = 0
    for line in f.readlines():
        #temp = re.findall(r'\d+', line)
        s += find(line)#int(temp[0][0] + temp[-1][-1])
    print(s)

# 55386
# 54824
