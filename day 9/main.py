
# PART 1
input = [l.strip() for l in open('day 9\input.txt').readlines()]
DIRS = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}
def addt(x, y):
    if len(x) == 2:
        return (x[0] + y[0], x[1] + y[1])
def dist(x, y):
    return max(abs(x[0]-y[0]), abs(x[1]-y[1]))
head = (0, 0)
tail = (0, 0)
tail_locs = set()
tail_locs.add(tail)
for move in input:
    dir, steps = move.split(" ")
    steps = int(steps)
    for i in range(steps):
        new_head = addt(head, DIRS[dir])
        if dist(new_head, tail) > 1:
            tail = head
            tail_locs.add(tail)
        head = new_head
print(len(tail_locs))

# PART 2

R = [[0, 0] for _ in range(10)]
tail_locs = set()
tail_locs.add((0, 0))
for line in input:
    x, y = line.split()
    y = int(y)

    for _ in range(y):
        dx = 1 if x == "R" else -1 if x == "L" else 0
        dy = 1 if x == "U" else -1 if x == "D" else 0

        R[0][0] += dx
        R[0][1] += dy

        for i in range(9):
            H = R[i]
            T = R[i + 1]

            _x = H[0] - T[0]
            _y = H[1] - T[1]

            if abs(_x) > 1 or abs(_y) > 1:
                if _x == 0:
                    T[1] += _y // 2
                elif _y == 0:
                    T[0] += _x // 2
                else:
                    T[0] += 1 if _x > 0 else -1
                    T[1] += 1 if _y > 0 else -1

        tail_locs.add(tuple(R[-1]))
print(len(tail_locs))
