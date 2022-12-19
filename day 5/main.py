import numpy as np
import re
# PART 1 
with open('day 5\input.txt') as f:
    line = f.readline()
    matrix = []
    while line[0].isdigit() is False:
        line_list = []
        for i in range(1, len(line), 4):
            line_list.append(line[i])
        matrix.append(line_list)
        line = f.readline().strip()
    number_list = []
    # transpose_matrix = np.array(matrix).transpose()
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # for i in range(0, len(line), 4):
    #     number_list.append(line[i])
    # transpose_matrix.append(number_list)
    # matrix.append(number_list)
    while True:
        # read a single line
        line = f.readline()
        if not line:
            break
        else:
            if line != '\n':
                numbers = re.findall(r'\d+', line)
                move_number = int(numbers[0])
                first_colum = int(numbers[1]) - 1
                second_colum = int(numbers[2]) -1
                popped = 0
                elements_to_add = []
                elements_to_remove = []
                i = 0
                while popped < move_number:
                    if result[first_colum][i] != ' ':
                        elements_to_add.append(result[first_colum][i])
                        result[first_colum][i] = ' '
                        popped += 1
                    i += 1
                added = 0
                index = len(result[second_colum]) - 1
                while added < move_number:
                    res = any(' ' in ele for ele in result[second_colum])
                    if res:
                        if result[second_colum][index] == ' ':
                            result[second_colum][index] = elements_to_add[0]
                            elements_to_add.remove(elements_to_add[0])
                            added += 1
                    else:
                        for number in elements_to_add:
                            result[second_colum].insert(0, number)
                        added = move_number
                    index -= 1

print(result)
                
