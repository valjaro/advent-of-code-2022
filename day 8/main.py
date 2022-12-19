import numpy as np
# PART 1
# input = [l.strip() for l in open('day 8\input.txt').readlines()]
# # print(input)
# score = 0
# for i, row in enumerate(input):
#     arr_transpose = [*zip(*input)]
#     if i == 0 or i == len(input):
#         score += len(row)
#     else:
#         col_index = 1
#         for pos, tree in enumerate(row):
#             if pos == 0 or pos == len(row):
#                 score += 1
#             else:
#                 col = ''.join(arr_transpose[pos])
#                 # check left and right
#                 left = any(int(row[num]) >= int(tree) for num in range(pos - 1, -1, -1))
#                 right = any(int(row[num]) >= int(tree) for num in range(pos + 1, len(row), 1))
#                 #check top and bot
#                 top = any(int(col[num]) >= int(tree) for num in range(i - 1, -1, -1))
#                 bottom = any(int(col[num]) >= int(tree) for num in range(i + 1, len(row), 1))
#                 # print(col)
#                 # print(row)
#                 # print("///////////////////////////////////////////////")
#                 # print(tree)
#                 # print(left, right, top, bottom)
#                 if not left or not right or not top or not bottom:
#                     score += 1
# print(score) 
# PART 2
input = [l.strip() for l in open('day 8\input.txt').readlines()]
# print(input)
score = []
for i, row in enumerate(input):
    arr_transpose = [*zip(*input)]
    if i == 0 or i == len(input):
        continue
    else:
        col_index = 1
        for pos, tree in enumerate(row):
            if pos == 0 or pos == len(row):
                continue
            else:
                col = ''.join(arr_transpose[pos])
                # check left and right
                left_index = pos - 1
                right_index = pos + 1
                top_index = i - 1
                bot_index = i + 1
                score_left = score_right = score_top = score_bot = 0
                # print(col)
                # print(row)
                # print("///////////////////////////////////////////////")
                # left_row = row[0:left_index]
                # right_row = row[right_index:len(row)]
                # top_row = col[0:top_index]
                # bot_row = col[bot_index:len(col)]
                while left_index > -1:
                    if row[left_index] >= tree:
                        score_left += 1
                        break
                    score_left += 1
                    left_index -= 1                 
                while right_index < len(row):
                    if row[right_index] >= tree:
                        score_right += 1
                        break
                    score_right += 1
                    right_index += 1
                while top_index > -1 and col[top_index] < tree:
                    if col[top_index] >= tree:
                        score_right += 1
                        break
                    score_top += 1
                    top_index -= 1
                while bot_index < len(row):
                    if col[bot_index] >= tree:
                        score_bot += 1
                        break
                    score_bot += 1
                    bot_index += 1
                total_score = score_left * score_right * score_top * score_bot
                score.append(total_score)
print(score)
print(max(score))