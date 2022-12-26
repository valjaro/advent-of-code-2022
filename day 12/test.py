input = [list(line.strip()) for line in open('day 12\input.txt').readlines()]

n = len(input)
m = len(input[0])
print(n , m)

sx, sy = [(i, j) for i in range(n) for j in range(m) if input[i][j] == "S"][0]
dx, dy = [(i, j) for i in range(n) for j in range(m) if input[i][j] == "E"][0]
print(sx, sy)
print(dx, dy)
input[sx][sy] = "a"
input[dx][dy] = "z"
input = [[ord(c) - ord('a') for c in r] for r in input]
print(input)