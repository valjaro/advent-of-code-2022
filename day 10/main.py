

input = [l.strip() for l in open('day 10\input.txt').readlines()]
# PART 1
x = 1
CYCLES = 0
signals = []
VALUES = []
SPECIAL_CYCLES = [20, 60, 100, 140, 180, 220]
for line in input:
    ins, n = line.split(" ") if line[0:4] == 'addx' else (0,0)
    n = int(n)
    CYCLES += 1
    if CYCLES in SPECIAL_CYCLES:
            VALUES.append(CYCLES * x)
            signals.append(x)
    if ins == "addx":
        CYCLES += 1
        if CYCLES in SPECIAL_CYCLES:
            VALUES.append(CYCLES * x)
            signals.append(x)
        x += n

print(sum(VALUES))
#PART 2

# crt = (0, 1)
# S = [(0, _ + 1) for _ in range(3)]
crt = [[" " for x in range(40)] for y in range(6)]
CYCLES = 0
x = 1
def cycle():
    global CYCLES, x
    CYCLES += 1
    if abs((CYCLES - 1) % 40 - x) < 2:
        crt[(CYCLES-1) // 40][(CYCLES-1) % 40] = "#"
for line in input:
    ins, n = line.split(" ") if line[0:4] == 'addx' else (0,0)
    n = int(n)
    if ins == 'addx':
        cycle()
        cycle()
        x += n
    else:
        cycle()
for line in crt:
    print("".join(line))

