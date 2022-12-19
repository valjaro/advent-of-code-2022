# A for ROCK
# B for PAPER 
# C for SCISSORS
# X ROCK
# Y PAPER
# Z SCISSORS


#PART 1
with open('day 2\input.txt') as f:
    lines = f.readlines()
    score = 0
    for i,line in enumerate(lines):
        plays = line.strip().split(' ')
        op_play = plays[0]
        my_play= plays[1]
        if op_play == 'A':
            # WIN FOR ROCK --> PAPER
            if my_play == 'Y':
                score += 8
            # DRAW FOR ROCK --> ROCK
            elif my_play == 'X': 
                score += 4
            # LOST FOR ROCK --> SCISSORS
            else:
                score += 3
        elif op_play == 'B':
            # WIN FOR PAPER --> SCISSORS
            if my_play == 'Z':
                score += 9
            # DRAW FOR PAPER --> PAPER
            elif my_play == 'Y':
                score += 5
            # LOST FOR PAPER --> ROCK
            else:
                score += 1
        else:
            # WIN FOR SCISSORS --> ROCK
            if my_play == 'X':
                score += 7
            # DRAW FOR SCISSORS --> SCISSORS
            elif my_play == 'Z':
                score += 6
            # LOST FOR SCISSORS --> PAPER
            else:
                score += 2
print(score)

# PART 2
#X LOST
#Y DRAW
#Z WIN
LOST = 0
DRAW = 3
WIN = 6
ROCK = 1
PAPER = 2
SCISSORS = 3
with open('day 2\input.txt') as f:
    lines = f.readlines()
    score = 0
    for i,line in enumerate(lines):
        plays = line.strip().split(' ')
        op_play = plays[0]
        final_result= plays[1]
        if op_play == 'A':
            # FINAL RESULT FOR ROCK --> DRAW --> ROCK
            if final_result == 'Y':
                score += ROCK + DRAW
             # FINAL RESULT FOR ROCK --> LOST --> SCISSORS
            elif final_result == 'X': 
                score += SCISSORS + LOST
             # FINAL RESULT FOR ROCK --> WIN --> PAPER
            else:
                score += PAPER + WIN
        elif op_play == 'B':
            # FINAL RESULT FOR PAPER --> WIN --> SCISSORS
            if final_result == 'Z':
                score += SCISSORS + WIN
            # FINAL RESULT FOR PAPER --> DRAW --> PAPER
            elif final_result == 'Y':
                score += PAPER + DRAW
            # FINAL RESULT FOR PAPER --> LOST --> ROCK
            else:
                score += ROCK + LOST
        else:
            # FINAL RESULT FOR SCISSORS --> LOST --> PAPER
            if final_result == 'X':
                score += LOST + PAPER            
             # FINAL RESULT FOR SCISSORS --> WIN --> ROCK
            elif final_result == 'Z':
                score += ROCK + WIN
             # FINAL RESULT FOR SCISSORS --> DRAW --> SCISSORS
            else:
                score += SCISSORS + DRAW
print(score)