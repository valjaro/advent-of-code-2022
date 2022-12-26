with open('day 13\input.txt') as f:
    input = f.read().split("\n\n")
wrong = 0
pairs = [x for x in open('day 13\input.txt').read().strip().split('\n\n')]
def compare(l, r):
    if isinstance(l, list) and isinstance(r, list):
        for i in range(min(len(l), len(r))):
            c = compare(l[i], r[i])
            if c != 0:
                return c
        return compare(len(l), len(r))
    if isinstance(l, list):
        return compare(l, [r])
    if isinstance(r, list):
        return compare([l], r)
    if l == r:
        return 0
    if l < r:
        return 1
    if r < l:
        return -1

s = 0

pkts = []
for i in range(len(pairs)):
    pair = pairs[i]
    l, r = pair.split("\n")
    if l == r:
        raise Exception("no")
    l = eval(l)
    r = eval(r)
    pkts.append(l)
    pkts.append(r)
    if compare(l, r) == 1:
        s += i + 1
print(s)

# PART 2
pkts.append([[2]])
pkts.append([[6]])

for i in range(len(pkts)):
    for j in range(len(pkts) - 1):
        if compare(pkts[j], pkts[j+1]) < 0:
            pkts[j], pkts[j + 1] = pkts[j + 1], pkts[j]
result = [i+1 for i in range(len(pkts)) if pkts[i] == [[2]] or pkts[i] == [[6]]]
from functools import reduce
result = reduce((lambda x, y: x * y), result)
print(result)