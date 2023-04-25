import math

def get_column(A, index):
	result = []
	for row in A:
		result.append(row[index])
	return result
	
def show_sheet(A):
	for row in A:
		line = "{:<5} " * len(row)
		line = line[:-1]
		print(line.format(*[str(round(i, 5))+' |' for i in row]))
		print('--------------------------------------------------------------------------------------')
	
	
def simplex_step(A, row_index, column_index):
	main_elem = A[row_index][column_index]
	A[row_index] = [elem / main_elem for elem in A[row_index]]
	for i in range(len(A)):
		if i != row_index:
			coef = -1 * A[i][column_index]
			A[i] = [A[row_index][y] * coef + A[i][y] for y in 
	range(len(A[i]))]
	return A
def find_index_by_column(A, main_row_idx):

	main_row = A[main_row_idx][:count_of_variables]
	last_row = A[-1][:count_of_variables]
	temp_array = []
	for i in range(len(main_row)):
		if main_row[i] < 0:
			temp_array.append(abs(last_row[i] / main_row[i]))
		else:
			temp_array.append(math.inf)
	main_column_idx = temp_array.index(min(temp_array))
	if min(temp_array) == math.inf:
		print(A[-1][-1])
		print(resultX)
		exit(1)
	return main_column_idx
	
def find_index_by_row(A, main_column_idx):
	main_column = get_column(A, main_column_idx)[:-1]
	last_column = get_column(A, len(A[0]) - 1)
	temp_array = []
	for i in range(len(main_column)):
		if main_column[i] != 0:
			if last_column[i] / main_column[i] >= 0:
				temp_array.append(last_column[i] / main_column[i])
			else:
				temp_array.append(math.inf)
		else:
			temp_array.append(math.inf)
	main_row_idx = temp_array.index(min(temp_array))
	if min(temp_array) == math.inf:
			print(A[-1][-1])
			print(resultX)
			exit(1)
	return main_row_idx
	
findMAX = True
M = 10000

A = [
[1, 1],
[-3, -1],
[-1, -5],
[1, 0],
[0, 1]
]

b = [4, -4, -4, 3, 3]
size = len(b)
count_of_variables = len(A[0])
c = [-3, -3]

for i in range(size):
	for y in range(size):
		if i == y:
			A[i].append(1)
		else:
			A[i].append(0)
			
last_row = [i for i in c]

for _ in range(len(b)):
	A[_].append(b[_])
	last_row.append(0)
	
last_row.append(0)

A.append(last_row)

index = count_of_variables

tempRES = []
resultX = []

for i in range(count_of_variables + len(b)):
	tempRES.append('X' + str(i + 1))
	if i >= count_of_variables:
		resultX.append('X' + str(i + 1))

show_sheet(A)
print(tempRES, resultX)

condition = True
while condition:
	last_column = get_column(A, len(A[0]) - 1)[:-1]
	if findMAX:
		if min(last_column) < 0:
			main_row_idx = last_column.index(min(last_column))
			main_column_idx = find_index_by_column(A, main_row_idx)
		else:
			last_row = A[-1][:-1]
			if min(last_row) < 0:
				main_column_idx = last_row.index(min(last_row))
				main_row_idx = find_index_by_row(A, main_column_idx)
			else:
				break
	else:
		if min(last_column) < 0:
			main_row_idx = last_column.index(min(last_column))
			main_column_idx = find_index_by_column(A, main_row_idx)
		else:
			last_row = A[-1][:-1]
			if max(last_row) > 0:
				main_column_idx = last_row.index(max(last_row))
				main_row_idx = find_index_by_row(A, main_column_idx)
			else:
				break
				
	resultX[main_row_idx] = tempRES[main_column_idx]
	simplex_step(A, main_row_idx, main_column_idx)
	
	show_sheet(A)
	
print(A[-1][-1])
print(resultX)
