
# PART 1
with open('day 4\input.txt') as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        pairs = line.split(',')
        first_pair = pairs[0]
        second_pair = pairs[1].strip()
        first_pair_first_number = int(first_pair.split('-')[0])
        first_pair_second_number = int(first_pair.split('-')[1])
        second_pair_first_number = int(second_pair.split('-')[0])
        second_pair_second_number = int(second_pair.split('-')[1])
        # EX: 2-7, 3,6
        if first_pair_first_number <= second_pair_first_number and first_pair_second_number >= second_pair_second_number:
            score += 1
        # EX: 4-5, 3-8
        elif first_pair_first_number >= second_pair_first_number and first_pair_second_number <= second_pair_second_number:
            score += 1
        # print(first_pair)
        # print(second_pair)
print(score)

# PART 2
with open('day 4\input.txt') as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        pairs = line.split(',')
        first_pair = pairs[0]
        second_pair = pairs[1].strip()
        first_pair_first_number = int(first_pair.split('-')[0])
        first_pair_second_number = int(first_pair.split('-')[1])
        second_pair_first_number = int(second_pair.split('-')[0])
        second_pair_second_number = int(second_pair.split('-')[1])
        # EX: 2-7, 3,6
        # range_1 = range(first_pair_first_number, first_pair_second_number)
        # range_2 = range(second_pair_first_number, second_pair_second_number)
        # if second_pair_first_number in range_1 or second_pair_second_number in range_1:
        #     score+=1
        # elif first_pair_first_number in range_2 or first_pair_second_number in range_2:
        #     score+=1
        if first_pair_first_number <= second_pair_first_number <= first_pair_second_number or first_pair_first_number <= second_pair_second_number <= first_pair_second_number :
            score += 1
        # EX: 4-5, 3-8
        elif second_pair_first_number <= first_pair_first_number <= second_pair_second_number or second_pair_first_number <= first_pair_second_number <= second_pair_second_number :
            score += 1
        # print(first_pair)
        # print(second_pair)
print(score)