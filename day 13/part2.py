

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
    if r > l:
        return -1

s = 0
packets = [x for x in input.split("\n")]
for i in range(len(pairs)):
    pair = pairs[i]
    l, r = pair.split("\n")
    packets = [x for x in pairs.split("\n")]
    if l == r:
        raise Exception("no")
    l = eval(l)
    r = eval(r)
    if compare(l, r) == 1:
        s += i + 1
print(s)