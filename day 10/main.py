input = [l.strip() for l in open('day 10\input.txt').readlines()]




x = 1
CYCLES = 0
for line in input:
    ins, n = line.split(" ")
    n = int(n)
    if ins == "addx":
        CYCLES+=2
        x += n
    print(line)
