
scores = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
    }
# PART 1 
with open('day 3\input.txt') as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        line = line.strip()
        res_first = line[0:len(line)//2]
        res_second = line[len(line)//2 if len(line)%2 == 0 else ((len(line)//2)+1):]
        for letter in res_first:
            if letter in res_second:
                score += scores[letter]
                break
        # print(len(res_first))
        # print(len(res_second))
print(score)
# PART 2
with open('day 3\input.txt') as f:
    lines = f.readlines()
    score, i, j = 0, 0, 3
    len_lines = int(len(lines) /3 )
    for iter in range(len_lines):
        group_lines = lines[i:j]
        for letter in group_lines[0].strip():
            if letter in group_lines[1].strip() and letter in group_lines[2].strip():
                score += scores[letter]
                break
        i += 3
        j += 3
print(score)
