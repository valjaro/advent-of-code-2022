input = [l.strip() for l in open('day 12\input.txt').readlines()]

import string
alphabet = list(string.ascii_lowercase)
DIRS = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}
def addt(x, y):
    if len(x) == 2:
        return (x[0] + y[0], x[1] + y[1])
def dist(x, y):
    return max(abs(x[0]-y[0]), abs(x[1]-y[1]))
matrix = []
for i, line in enumerate(input):
    aux_list = []
    for j, letter in enumerate(line):
        if letter == 'S':
            starting_point = (i, j)
            aux_list.append(-1)
        elif letter == 'E':
            final_point = (i, j)
            aux_list.append(26)
        else:
            aux_list.append(alphabet.index(letter))
    matrix.append(aux_list)

# QItem for current location and distance
# from source location
class QItem:
	def __init__(self, row, col, dist):
		self.row = row
		self.col = col
		self.dist = dist

	def __repr__(self):
		return f"QItem({self.row}, {self.col}, {self.dist})"

def minDistance(grid):
	source = QItem(0, 0, 0)

	# Finding the source to start from
	for row in range(len(grid)):
		for col in range(len(grid[row])):
			if grid[row][col] == -1:
				source.row = row
				source.col = col
				break

	# To maintain location visit status
	visited = [[False for _ in range(len(grid[0]))]
			for _ in range(len(grid))]
	
	# applying BFS on matrix cells starting from source
	queue = []
	queue.append(source)
	visited[source.row][source.col] = True
	while len(queue) != 0:
		source = queue.pop(0)

		# Destination found;
		if (grid[source.row][source.col] == 26):
			return source.dist
        
		# moving down
		if isValid(source.row, source.col,source.row + 1, source.col, grid, visited):
			queue.append(QItem(source.row + 1, source.col, source.dist + 1))
			visited[source.row + 1][source.col] = True
        # moving right
		if isValid(source.row, source.col, source.row, source.col + 1, grid, visited):
			queue.append(QItem(source.row, source.col + 1, source.dist + 1))
			visited[source.row][source.col + 1] = True
        # moving up
		if isValid(source.row, source.col, source.row - 1, source.col, grid, visited):
			queue.append(QItem(source.row - 1, source.col, source.dist + 1))
			visited[source.row - 1][source.col] = True
		# moving left
		if isValid(source.row, source.col, source.row, source.col - 1, grid, visited):
			queue.append(QItem(source.row, source.col - 1, source.dist + 1))
			visited[source.row][source.col - 1] = True

	return -1
# checking where move is valid or not
def isValid(i, j, x, y, grid, visited):
    posible_values =  [0, 1]
    if ((x >= 0 and y >= 0) and
		(x < len(grid) and y < len(grid[0])) and
			((grid[x][y] - grid[i][j]) < 2) and (visited[x][y] == False)):
		    return True
    return False


if __name__ == '__main__':
	print(minDistance(matrix))