# Part 1
with open('day 1\input.txt') as f:
    lines = f.readlines()
    suma = 0
    highest = 0
    for line in lines:
        if line != '\n':
            suma+=float(line)
        else:
            if suma > highest:
                highest = suma 
            suma = 0
print(int(highest))

# Part 2
with open('day 1\input.txt') as f:
    lines = f.readlines()
    suma = 0
    top3 = [0, 0, 0,]
    for line in lines:
        if line != '\n':
            suma+=int(line)
        else:
            top3.sort()
            if top3[0] < suma:
                top3[0] = suma
            suma = 0
print(int(highest))
print(sum(top3))
