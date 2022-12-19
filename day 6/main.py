# PART 1
with open('day 6\input.txt') as f:
    line = f.readline()
    print(len(line))
    no_repeated = []
    position = 0
    for letter in line:
        if len(no_repeated) < 4:
            if letter not in no_repeated:
                no_repeated.append(letter)
            else:
                no_repeated = []
                no_repeated.append(letter)
            position += 1
    print(no_repeated)
    print(position)
#PART 2
with open('day 6\input.txt') as f:
    line = f.readline()
    print(len(line))
    no_repeated = []
    position = 0
    for letter in line:
        if len(no_repeated) < 14:
            if letter not in no_repeated:
                no_repeated.append(letter)
            else:
                index = no_repeated.index(letter)
                while index >= 0:
                    no_repeated.pop(index)
                    index -= 1
                no_repeated.append(letter)
            position += 1
    print(no_repeated)
    print(position)

# TESTS
with open('day 6\input.txt') as f:
    subroutine = list(f.read().strip())
    for i in range(len(subroutine) - 4):
        if len(set(subroutine[i:i+4])) == 4:
            print(set(subroutine[i:i+4]))
            print(i+4)
            exit()